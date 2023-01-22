import pyttsx3 
import pypdf as pf 

class InvalidPageNumber(Exception):
    def __init__(self, message="Page number provided is invalid."):
        self.message = message 
        super().__init__(self.message)

class Speaker():
    def __init__(self):
        self.engine = pyttsx3.init()
        self.voice = self.engine.getProperty('voices')
        
    def speak(self, text, gender="F", rate=130):
        if gender == "M":
            self.engine.setProperty('voice', self.voice[0].id)           
        else: 
            self.engine.setProperty('voice', self.voice[1].id)
        self.engine.setProperty('rate', rate)
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.stop()

class ReadDocument():
    def __init__(self, pdf: pf.PdfReader):
        self.pdf = pdf 
        self.pagelist = self.pdf.pages
        self.MAX_PAGE = len(self.pagelist) 
        self.speaker = Speaker()

    def readPageNumber(self, page):
        try:
            page_text = self.pagelist[page-1].extract_text()
        except Exception as e:
            raise InvalidPageNumber()
        self.speaker.speak(page_text)

    def readAllPages(self, start_page = 1, page_count = 100):
        for i in range(start_page, start_page+page_count):
            self.readPageNumber(i)

if __name__=='__main__':
    pdf = pf.PdfReader('library/ref_book.pdf') 
    doc = ReadDocument(pdf)
    doc.readAllPages(start_page=1, page_count=3)

    
        

               