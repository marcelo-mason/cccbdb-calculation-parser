from html.parser import HTMLParser


class HTMLTableParser(HTMLParser):
    def __init__(
        self
    ):

        HTMLParser.__init__(self)

        self._in_td = False
        self._in_th = False
        self._current_table = []
        self._current_row = []
        self._current_cell = []
        self.tables = []
        self.ignore = False

    def handle_starttag(self, tag, attrs):
        if tag == 'td':
            self._in_td = True
            self.extracting = True
        if tag == 'th':
            self._in_th = True
            if (len(attrs) > 0):
                if (attrs[0][0] == 'rowspan'):
                    self.ignore = True

        if tag == "a" and self._in_td:
            self._current_cell.append(attrs[0][1])

    def handle_data(self, data):
        if self._in_td or self._in_th:
            if self.ignore is False:
                self._current_cell.append(data.strip())

    def handle_endtag(self, tag):
        if tag == 'td':
            self._in_td = False
        elif tag == 'th':
            self._in_th = False

        if tag in ['td', 'th']:
            if self.ignore is False:
                self._current_row.append(self._current_cell[::-1])
            self._current_cell = []
            self.ignore = False
        elif tag == 'tr':
            self._current_table.append(self._current_row)
            self._current_row = []
        elif tag == 'table':
            self.tables.append(self._current_table)
            self._current_table = []
