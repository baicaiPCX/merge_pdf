
import os
import glob
from PyPDF2 import PdfFileMerger
import argparse

import tkinter as tk
from tkinter import filedialog

def extract_pdf_from_files(files):
        pdf_files=[]
        for e in files:
                if not os.path.exists(e):
                        print(f"Warning:{e} is not exist.")
                        continue
                if os.path.isdir(e):
                        temp_pdf_files=glob.glob(os.path.join(e,"*.pdf"))
                        pdf_files=pdf_files+temp_pdf_files
                else:
                        if e.endswith(".pdf") or e.endswith(".PDF"):
                                pdf_files.append(e)
        return pdf_files

def main(files,target_path):
        pdf_lst = extract_pdf_from_files(files)
        pdf_lst.sort()
        file_merger = PdfFileMerger()

        for pdf in pdf_lst:
                print(pdf)
                file_merger.append(pdf)

        if os.path.exists(target_path):
                print(f"Error:{target_path} is exist.")
                return
        file_merger.write(target_path)


if __name__=="__main__":
        if 0:
                parse=argparse.ArgumentParser()
                parse.add_argument("files",nargs="+",default=False)
                parse.add_argument("--target","-t",type=str,default="merge.pdf")
                arg=parse.parse_args()
                main(arg.files,arg.target)
        else:
                root=tk.Tk()
                root.withdraw()
                files=filedialog.askopenfilenames()
                if files is None or files=="":
                        pass
                else:
                        main(files,"merge.pdf")