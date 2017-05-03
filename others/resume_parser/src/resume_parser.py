"""
Parses the resume document present in .docx file 
and returns Candidate Name and its years of experience

Assumptions: 
	-- docx format 
	-- document starts with Candidate Name in first line
	-- Document contains years of experience as a numeric value

"""
import os
import shutil
import re
from docx import Document

### Experiment Area ###
#print dir(document)
#print document.paragraphs
#print document.tables 
#print dir(document.sections)
#print dir(document.sections.count)
#print document.element
#print document.part
#document.save('test.docx')

    
### Experiment Area ###


def get_years_exp(line_str):
    """
    second level of parsing to get specific years of experience
    """
    """
    get the sentence from paragraph 
    break that sentence in list of words
    try to get number of years from that list
    
    """
    #print line_str
    
    keywords = ['years', 'experience']
    sentences = line_str.split('.')
    found = False
    
    wlist = []
    for sentence in sentences:
        for keyword in keywords:
            if sentence.find(keyword) is not -1:
                found = True
            else:
                found = False
        if found is True:
            #Sentence is found
            wlist = sentence.split()
            break
    if len(wlist) != 0:
        for word in wlist:
            #take care of scenarios like 8+ years of experience
            if word.find('+') != -1:
                word = word[:-1]
            if word.isdigit() is True:
                return word
    
    return None
    
def parse_para(line_str):
    """
    parses paragraph string to identify literals
    """
    keywords = ['years', 'experience']
    years = None
    
    if len(line_str) == 0:
        return years
    
    found = False
    for keyword in keywords:
        if line_str.lower().find(keyword) is not -1:
            found = True
        else:
            break;
    if found is True:
#        print line_str
        years = get_years_exp(line_str)
    
    return years
        

def read_resume(filename):
    """
    reads resume to get information 
    """
     
    document = Document(filename) 
    #document = Document('resume_goldsmith.docx')
    #document = Document('Steven-Owens-machine_learning-resume.doc')
    #document = Document('Abhi.t_Testing.docx')
    #document = Document('Aiswarya_Ramamurthi_Resume.doc')
    #document = Document('test.docx')
    
    
    
    """
    retval = False
    count = 0
    while count is not len(document.paragraphs):
        #print count, document.paragraphs[count].text
        retval = parse_para(document.paragraphs[count].text)
        if retval is True:
            break
        count +=1
    """
    name_found = False
    full_name = ''
    for para in document.paragraphs:
        ## Find full name
        if len(para.text) != 0 and name_found is False:
            full_name = '_'.join(para.text.split())
            #print full_name
            name_found = True
            continue
            
        years = parse_para(para.text)
        if years is not None:
            break   

    retlist = []
    if years is not None:
        #print 'Experience Found', years, full_name
        retlist.append(full_name)
        retlist.append(years)
    else:
        print 'Not able to find experience info'
    
    #returns [full_name, years] or []
    return retlist

def output_resume(dirpath, filename, retlist):
    """
    
    """
    #create directory if it does not exist
    output_dir = 'output\\' + dirpath
    #vne::tbd:: It can be moved globally for performance optimization
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    fname = '_'.join(retlist + ['.docx'])
    
    src = '\\'.join([dirpath, filename])
    dst = '\\'.join([output_dir, fname])
    #Remove unwanted characters from filename
    dst= re.sub('[\-\\|/:(){}<>]', '', dst)
    print 'vne::', src, dst
    
    #shutil.copy(src, dst)
    shutil.move(src, dst)
    
def browse_files(base_dir):
    """
    browses directory to identify files
    """
    retlist = []
    for (dirpath, dirnames, filenames) in os.walk(base_dir):
        #print 'processing directory: ', dirpath
        if len(filenames) != 0:
            #print filenames
            for filename in filenames:
                extension = os.path.splitext(filename)[1]
                if extension.lower() == '.docx':
                    fname = '\\'.join([dirpath, filename])
                    #print 'processing file: ', fname
                    try:
                    #if True:
                        retlist = read_resume(fname)
                        if len(retlist) != 0: 
                            #get designation 
                            print 'processing file: ', fname
                            designation = dirpath.split('\\')[-1]
                            designation = '_'.join(designation.split())
                            #print 'desig: ', designation
                            output_resume(dirpath, filename, [designation] + retlist)
                    except:
                        print 'Exception Occured: ', fname



base_dir = 'resumes'
browse_files(base_dir)

#read_resume('resumes\\Artificial Intelligence\\AnandAndrew_J2EEJava_LeadResume.docx')
#read_resume('resume_goldsmith.docx')
#print os.walk('resumes')
