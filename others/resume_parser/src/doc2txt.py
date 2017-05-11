#!/usr/bin/python

"""
pip install pypiwin32

It converts a .doc file to .txt and reads its contents
"""

import win32com.client as win32


fileName='Steven-Owens-machine_learning-resume.doc'
path=['e:', 'eclipse', 'workspace', 'resume_parser','src', fileName]

fName="\\\\".join(path)
#fName='e:\\eclipse\\workspace\\resume_parser\\src\\Steven-Owens-machine_learning-resume.doc'

ofile=fileName.split('.')[0] + '.txt'
opath="\\\\".join(path[:-1] + [ofile])

word = win32.gencache.EnsureDispatch('Word.Application')

word.Documents.Open(fName)

word.ActiveDocument.SaveAs(opath, FileFormat=win32.constants.wdFormatTextLineBreaks)

file_fd = open(opath)

for line in file_fd.readlines():
    print line

word.Documents.Close()
file_fd.close()

