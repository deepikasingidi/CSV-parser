class CustomCsvReader:
    """
    Streaming CSV reader implemented as an iterator.
    Handles quoted fields, escaped quotes, and embedded newlines.
    """

    def __init__(self, file_obj, delimiter=",", quotechar='"'):
        self.file = file_obj
        self.delimiter = delimiter
        self.quotechar = quotechar
        self.buffer = ""

    def __iter__(self):
        return self

    def __next__(self):
        row = []
        field = ""
        in_quotes = False

        while True:
            char = self.file.read(1)

            # End of file
            if char == "":
                if field or row:
                    row.append(field)
                    return row
                raise StopIteration

            # Quote handling
            if char == self.quotechar:
                next_char = self.file.read(1)
                if in_quotes and next_char == self.quotechar:
                    field += self.quotechar
                else:
                    in_quotes = not in_quotes
                    if next_char:
                        self.file.seek(self.file.tell() - 1)

            # Delimiter handling
            elif char == self.delimiter and not in_quotes:
                row.append(field)
                field = ""

            # Newline handling
            elif char == "\n" and not in_quotes:
                row.append(field)
                return row

            else:
                field += char
