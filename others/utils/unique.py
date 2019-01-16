

""" 
Logic to find out unique elements in a file 
"""

seen = set()
with open('port.txt') as infile:
    with open('output.txt', 'w') as outfile:
        for line in infile:
            if line not in seen:
                outfile.write(line)
                seen.add(line)

"""
with open('port.txt','r') as f:                                                                                                                                    
    distinct_content=set(f.readlines())                                                                                                                            

to_file=""                                                                                                                                                         
for element in distinct_content:                                                                                                                                   
    to_file=to_file+element                                                                                                                                        
with open('output_file','w') as w:                                                                                                                                 
    w.write(to_file)

"""
