from PyPDF2 import PdfReader;

class FileReader:
    def readFile(self, filePath):
        print('readFile called')
        fileText=[]
        reader = PdfReader(filePath)
        
        numberOfPages = len(reader.pages)
        print('Number of pages in the pdf : ' + str(numberOfPages))
        if numberOfPages > 0:
            for page in reader.pages:
                pageText = page.extract_text()
                fileText.append(pageText)
            return "".join(fileText);
        else:
            print('Provided file is empty.')
            return ''