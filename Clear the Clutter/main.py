import os

# createIfNotExist function which makes folder if not created
def createIfNotExist(folder):
   if not os.path.exists(folder):
      os.mkdir(folder)

def extractFileCat(dictCat):
   return [file for file in files if os.path.splitext(file)[1].lower() in file_extensions[dictCat]]

def move(folderName, files):
   for file in files:
      os.replace(file, f"{folderName}/{file}")


if __name__ == "__main__":

   # Listing all the files
   files = os.listdir()
   files.remove("main.py")

   # Creating folder if not exists
   createIfNotExist("Images")
   createIfNotExist("Text Files")
   createIfNotExist("Documents")
   createIfNotExist("Media")
   createIfNotExist("Code Files")
   createIfNotExist("Others")

   # All Extensions
   file_extensions = {
      "ImageExtensions" : [".jpg", ".png", ".jpeg", ".gif", ".webp"],
      "TextExtensions" : [".txt", ".log"],
      "DocsExtensions" : [".docs", ".doc", ".docx", ".pptx", ".xlsx", ".csv"],
      "MediaExtensions" : [".mp4", ".mp3", ".vlf"],
      "CodeExtensions" : [".c", ".cpp", ".js", ".html", ".css", ".java"]
   }

   # Extracting Files for particular category
   images = extractFileCat("ImageExtensions")
   textf = extractFileCat("TextExtensions")
   docs = extractFileCat("DocsExtensions")
   medias = extractFileCat("MediaExtensions")
   codes = extractFileCat("CodeExtensions")

   #Other Files Logic
   others = []
   f2 = images + textf + docs + medias + codes
   for file in files:
      if file not in f2 and os.path.isfile(file):
         others.append(file)

# Adding all the files on its respective folder
move("Images", images)
move("Text Files", textf)
move("Documents", docs)
move("Media", medias)
move("Code Files", codes)
move("Others", others)

