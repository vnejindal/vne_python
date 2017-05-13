"""
Dumps resumes text into csv file

Prerequisites: 
pip install pypiwin32
pip install python-docx
"""
import os
from docx import Document
import win32com.client as win32


# List of output files that got converted successfully
def convert_doc_file(file_name):
    """
    This function converts .doc file to its .txt format
    returns outfile .txt file name with absolute path
    """
    
    ofile_name=file_name.split('.')[0] + '.txt'
    #print 'processing:', file_name, ofile_name
    
    word = win32.gencache.EnsureDispatch('Word.Application')
    word.Documents.Open(file_name)
    try:
        word.ActiveDocument.SaveAs(ofile_name, FileFormat=win32.constants.wdFormatTextLineBreaks)
    except: 
        ofile_name = ''
        print 'could not convert .doc to .txt', file_name
    
    word.Documents.Close()
    return ofile_name

def strip_characters(input_string):
    """
    Deletes characters from input string
    """
#    input_string = input_string.strip()
    input_string = input_string.strip('\n')
    input_string = input_string.strip('\t')
    input_string = input_string.replace('\n', ' ')
    input_string = input_string.replace('\t', ' ')
    
    return input_string

def process_resume(filename, extension):
    """
    reads a resume to get information
    filename: Full path of file 
    extension: file extension  
    
    returns returns file contents in a string
    """
    file_contents = ''
    
    if extension == '.docx':
        document = Document(filename) 
        for para in document.paragraphs:
            file_contents += strip_characters(para.text)
    elif extension == '.doc':
        """
        Convert .doc to .txt
        read .txt line by line
        """
        ofile_name = convert_doc_file(filename)
        if len(ofile_name) != 0:
            file_fd = open(ofile_name)
            for line in file_fd.readlines():
                file_contents += strip_characters(line)      
            file_fd.close()
                    
    return file_contents

def process_resumes(base_dir, output_file, delimiter):
    """
    Processes resume files placed at 'base_dir'
    
    browses directory to identify files
    """
    if not os.path.exists(base_dir):
        print 'base directory doest not exist:', base_dir
        return

    cur_dir = os.getcwd().split('\\')
    
    foutput = open(output_file, "a+")
    
    for (dirpath, dirnames, filenames) in os.walk(base_dir):
        #print 'processing directory: ', dirpath
        if len(filenames) != 0:
            #print filenames
            for filename in filenames:
                extension = os.path.splitext(filename)[1]
                if extension.lower() == '.docx' or extension.lower() == '.doc':
                    fname = '\\\\'.join(cur_dir + [dirpath, filename]) #Full filename
                    print 'processing file: ', fname
                    try:
                    #if True:
                        file_contents = process_resume(fname, extension.lower())
                        if len(file_contents) != 0:
                            foutput.write(fname + delimiter + file_contents + '\n')
                            foutput.flush()
                            
                    except:
                        print 'Exception Occured: ', fname

    foutput.close()



base_dir = 'resumes'
output_file = 'output.csv'
delimiter = '$#$'
process_resumes(base_dir, output_file, delimiter)
