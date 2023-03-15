import sys
import os
import time
from dotenv import load_dotenv
from comtypes.client import CreateObject

load_dotenv()
path_to_files = os.path.normpath(os.getenv('MYPATH'))
list_of_files = os.listdir(path_to_files)

wdFormatPDF = 17  # explain this
target_directory = os.path.abspath(path_to_files)

word = CreateObject('Word.Application')
word.Visible = False
for file in list_of_files:
    in_file = os.path.join(target_directory, file)
    filename, _ = os.path.splitext(file)
    filename_pdf = f'{filename.replace(" ", "_")}.pdf'        
    out_file = os.path.join(target_directory, filename_pdf)    
    doc = word.Documents.Open(in_file)
    time.sleep(3)
    doc.SaveAs(out_file, FileFormat=wdFormatPDF)
    doc.Close()
    print(f'{filename_pdf} was generated succesfully')
word.Quit()