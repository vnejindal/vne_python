#!/usr/bin/python

import time


def analyse_records(d_file, x_file):
  """ Analyses dump file record with xdr file
  """
  
  f_dspdump = open(d_file)
  print f_dspdump
    
  f_xdr = open(x_file)
  print f_xdr 
  
  cnt_d = 0
  d_list = []
  for name in f_dspdump:
    d_list.append(name.strip())
    cnt_d += 1
  
  cnt_x = 0
  x_list = []
  for name in f_xdr:
    x_list.append(name.strip())
    cnt_x += 1
  
  print 'Records Len:', cnt_d, cnt_x - 1
 # print d_list[0]
  
  #x_rec = x_list[1].split(',')
  #index = 52
  #print x_rec[0], x_rec[index], x_rec[index+1], x_rec[index+2],x_rec[index+3]
  
  #d_rec = d_list[9].split(',')
  #print d_rec[1], d_rec[2], d_rec[3], d_rec[4],d_rec[5]
  
  #Counters 
  err_rec = 0
  fine_rec = 0
  umatch_rec = 0
  match_rec = 0
  
  mos_xin = 52
  mos_din = 2
  for d_in in d_list:
    d_rec = d_in.split(',')
    # Get xdr record for this record
    #print 'd_rec', d_rec
    x_rec = []
    rec_found = 0
    for x_in in x_list: 
      x_rec = x_in.split(',')
      if x_rec[0] == d_rec[1]:  # Check Call Key fields
        fine_rec += 1
        rec_found = 1
        x_list.remove(x_in) # VNE:: This line creates magic in execution time
        break
      else:
        err_rec += 1
        continue
    
    #print 'x_rec', x_rec
    if rec_found == 1:
      if d_rec[mos_din] != x_rec[mos_xin] or d_rec[mos_din+1] != x_rec[mos_xin+1] or d_rec[mos_din+2] != x_rec[mos_xin+2] or d_rec[mos_din+3].strip() != x_rec[mos_xin+3]:
        print d_rec[mos_din] , x_rec[mos_xin] 
        print d_rec[mos_din+1], x_rec[mos_xin+1] 
        print d_rec[mos_din+2], x_rec[mos_xin+2] 
        print d_rec[mos_din+3], x_rec[mos_xin+3]
        umatch_rec += 1 
      else:
        match_rec += 1
    
  #print 'Fine Rec  :', fine_rec
  #print 'Error Rec :', err_rec
  print 'Match Rec :', match_rec
  print 'Umatch Rec:', umatch_rec

def main():
  dsp_dumpfile = 'dspdump.csv'
  xdr_datafile = 'xdr_data.csv'
  #analyse_records(dsp_dumpfile, xdr_datafile)

  s_time = time.time()
  
  xdr_1 = 'xdr_3.csv'
  ddump_1 = 'dsp_dump_3.csv'
  analyse_records(ddump_1, xdr_1)
  
  print 'Time: ', time.time() - s_time
  
  xdr_2 = 'xdr_2.csv'
  ddump_2 = 'dsp_dump_2.csv'
  #analyse_records(ddump_2, xdr_2)
 
if __name__ == '__main__':
  main()

