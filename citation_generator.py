# citation_generator.py

class CitationGenerator:

    def ieee(self, author, title, year):

        return f'{author}, "{title}," {year}.'

    def apa(self, author, title, year):

        return f'{author} ({year}). {title}.'

    def mla(self, author, title, year):

        return f'{author}. "{title}." {year}.'

    def harvard(self, author, title, year):

        return f'{author}, {year}. {title}.'