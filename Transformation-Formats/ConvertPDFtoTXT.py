# first method
# sudo apt install build-essential libpoppler-cpp-dev pkg-config python3-dev
# pip3 install pdftotext

import pdftotext
 
# Load your PDF
with open("/home/../1-b.pdf", "rb") as f:
    pdf = pdftotext.PDF(f)
 
# Save all text to a txt file.
with open('/home/.../1-a.txt', 'w') as f:
    f.write("\n\n".join(pdf))


# Second method ****
import PyPDF2

#create file object variable
#opening method will be rb
pdffileobj=open('/home/.../1-b.pdf','rb')

#create reader variable that will read the pdffileobj
pdfreader=PyPDF2.PdfFileReader(pdffileobj)

#This will store the number of pages of this pdf file
x=pdfreader.numPages

#create a variable that will select the selected number of pages
#pageobj=pdfreader.getPage(0)

listt= []
#create a loop that will select the all pages
for i in range(x):
    pageobj=pdfreader.getPage(i) 
    text=pageobj.extractText()
    listt.append(text)
    
#(x+1) because python indentation starts with 0.
#create text variable which will store all text datafrom pdf file
#text=pageobj.extractText()

#save the extracted data from pdf to a txt file
#we will use file handling here
#dont forget to put r before you put the file path
#go to the file location copy the path by right clicking on the file
#click properties and copy the location path and paste it here.
#put "\\your_txtfilename"
file1=open(r"/home/..../1-a.txt","a")
file1.writelines(listt)
