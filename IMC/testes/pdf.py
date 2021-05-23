#usando o pypdf2
from PyPDF2 import PdfFileReader


def text_extractor(path):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        number_of_pages = pdf.getNumPages()
        print('pagina? ', number_of_pages)
        # get the first page
        page = pdf.getPage(number_of_pages)
        print(page)
        print('Page type: {}'.format(str(type(page))))
        text = page.extractText()
        return text


if __name__ == '__main__':
    path = 'Portal-Poupatempo.pdf'
    text = text_extractor(path)

    pos = text.find("Nome:")
    print(pos)
