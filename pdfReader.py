import pyttsx3
import PyPDF2
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path",help="Give the file path where pdf file is stored")
parser.add_argument("fromPage",type=int,help="From Which page you want to read")
parser.add_argument("toPage",type=int,help="The destination page where your reading ends")
parser.add_argument("speed", type=int, help="Specify the speed")


args = parser.parse_args()
book = open(args.path,'rb')
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("Starting  "+args.path+"  --------")
print("Total Page Number: ",pages)
print("\n")

speaker = pyttsx3.init()
rate = speaker.getProperty('rate')
voice = speaker.getProperty('voices')


for page in range(args.fromPage,args.toPage):
	voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0"
	speaker.setProperty('voice',voice_id)
	speaker.setProperty('rate',args.speed)
	print("Current Page: ",page)
	page = pdfReader.getPage(page)
	text = page.extractText()
	speaker.say(text)
	speaker.runAndWait()

print("Finished reading  -------------")