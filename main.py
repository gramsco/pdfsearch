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


def askForOutput(question):
  yes = ["y", "yes"]
  no = ["n", "no"]
  isGoodAnswer = False
  while isGoodAnswer == False:
    answer = input(question)
    if (answer in yes):
      return True
    if (answer in no):
      return False

def leave():
  print("~ bye")
  exit()

path = os.getcwd()
argLen = len(sys.argv)

# if no argv, merges all the file in the current directory
if argLen == 1:
  where = './'
  query = ''

#if path but no query, merges all the file in the specified directory
elif argLen == 2:
  if(askForOutput("No query specified. Query all files? ")):
    where = os.path.join(path, sys.argv[1])
    query = ''
  else:
    leave()
    
#standard behavior: looks for the query in every pdf file and merge the results
else:
  where = os.path.join(path, sys.argv[1])
  query = sys.argv[2]

directory = os.fsencode(where)

if not os.path.exists(os.path.join(where, 'pdfquery_results')):
    os.makedirs(os.path.join(where,'pdfquery_results'))

def queryPDFs(query):
  pages = []
  print()
  print("> Looking for " + '"' + query + '"')
  for file in os.listdir(directory):
    filename = os.fsdecode(file)
    
    if filename.endswith(".pdf"):
        print()
        print(" || " + filename + " || ")
        print()
        pdfFile = open(os.path.join(where, filename), 'rb')
        try:
          reader = PyPDF2.PdfFileReader(pdfFile)
          for pageNum in range(reader.numPages):
              page = reader.getPage(pageNum)
              contentPage = page.extractText()
              find = contentPage.find(query)
              if find != -1:
                print("\t -> match on page " + str(pageNum))
                pages.append(page)

        except:
          print(filename + "can't be added, sorry :(")

  return pages      
        
writer = PyPDF2.PdfFileWriter()
pages = queryPDFs(query)

if len(pages) == 0:
  print("no match, sorry :(")
  exit()

print()

if askForOutput("Do you want to create a file? "):
  if len(pages) != 0:
    for page in pages:
      writer.addPage(page)

  outputfile = open(os.path.join(where, 'pdfquery_results/' + query + ".pdf"), 'wb')
  writer.write(outputfile)
  print()
  print('\t––––––––––––––––––––––––––––––––')
  print("\t" + query + ".pdf" + " created!")
  print('\t––––––––––––––––––––––––––––––––')
  print()
  outputfile.close()

leave()
