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


class CustomCsvWriter:
    """
    Custom CSV writer.
    Handles quoting, escaping quotes, and newlines correctly.
    """

    def __init__(self, file_obj, delimiter=",", quotechar='"'):
        self.file = file_obj
        self.delimiter = delimiter
        self.quotechar = quotechar

    def _escape_field(self, field):
        field = str(field)

        needs_quotes = (
            self.delimiter in field
            or self.quotechar in field
            or "\n" in field
        )

        if self.quotechar in field:
            field = field.replace(self.quotechar, self.quotechar * 2)

        if needs_quotes:
            field = f'{self.quotechar}{field}{self.quotechar}'

        return field

    def writerow(self, row):
        escaped = [self._escape_field(field) for field in row]
        line = self.delimiter.join(escaped)
        self.file.write(line + "\n")

    def writerows(self, rows):
        for row in rows:
            self.writerow(row)
