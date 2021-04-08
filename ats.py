import pyttsx3
import PyPDF2

pdf = input("enter the pdf file:")
book = open(pdf,"rb")

if book.name.lower().endswith(".pdf"):
    pdfReader = PyPDF2.PdfFileReader(book)
else:
    print("Sorry, only pdf files are accepted!!!")
pages = pdfReader.numPages
print("total pages in this pdf is "+ str(pages))
speaker = pyttsx3.init()

#voice
voices = speaker.getProperty("voices")
# print(voices)
speaker.setProperty("voice",voices[1].id)
speaker.setProperty("rate",150)


pg_Str = int(input("enter the starting page:"))
pg_End = int(input("enter the ending page:"))
for num in range(pg_Str,pg_End+1):
    page =pdfReader.getPage(num)
    text = page.extractText()
    speaker.say(text)
speaker.runAndWait()





