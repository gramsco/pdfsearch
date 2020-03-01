import PyPDF2
import os
import sys

""" TODO :

  - work on argv system to allow user to :
      \select the folder
      \select a specific file, several files
      \select a query, several queries
      \select the output location
      \select a no output possibility
  - maybe work on a Bold system but seems a bit hard...

"""

directory = os.fsencode('./')

if not os.path.exists('pdfquery_results'):
    os.makedirs('pdfquery_results')

query = sys.argv[1]

def queryPDFs(query):
  pages = []
  print("looking for " + query)
  for file in os.listdir(directory):
    filename = os.fsdecode(file)
    
    if filename.endswith(".pdf"):
        print(" -> " + filename + " found.")
        pdfFile = open(filename, 'rb')
        try:
          reader = PyPDF2.PdfFileReader(pdfFile)
          for pageNum in range(reader.numPages):
              page = reader.getPage(pageNum)
              contentPage = page.extractText()
              find = contentPage.find(query)
              if find != -1:
                print("Match on page " + str(pageNum))
                pages.append(page)
              else:
                print("Page : " + str(pageNum))
        except:
          print(filename + "can't be added, sorry")

  return pages      
        
writer = PyPDF2.PdfFileWriter()
pages = queryPDFs(query)

def askForOutput():
  yes = ["y", "yes"]
  no = ["n", "no"]
  isGoodAnswer = False
  while isGoodAnswer == False:
    answer = input("Do you want to create a file? ")
    if (answer in yes):
      return True
    if (answer in no):
      return False

if askForOutput():
  if len(pages) != 0:
    for page in pages:
      writer.addPage(page)

  outputfile = open('./pdfquery_results/' + query + ".pdf", 'wb')
  writer.write(outputfile)
  outputfile.close()
