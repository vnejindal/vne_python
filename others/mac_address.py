


'''
It generates list of unique mac address prefixed by 'prefix' param. Just a set of loops with string concats 
'''


def get_mac_address():
  

  nentries = 125000;
  prefix = '84:78:8B';

#Samsung: 00:23:C2  
#Apple: 84:78:8B
#LG: E8:5B:5B     
  
  file_name = 'mac_list_' + prefix + '.csv'
  final_count = 0
  ninc = 1;
  hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F'];

  fp_mac_list = open(file_name , "a+")
  print "Name of the file: ", fp_mac_list.name
  print "Closed or not : ", fp_mac_list.closed

  for i0 in range(0,15): 
    l0 = hex_list[i0];
    for i1 in range(0,15):
      l1 = hex_list[i1];
      O1 = ':' + l0 + l1;
 #     print O1;
      for i2 in range(0, 15): 
        l2 = hex_list[i2];
        for i3 in range(0, 15): 
          l3 = hex_list[i3];
          O2 = ':' + l2 + l3;
          for i4 in range(0, 15): 
            l4 = hex_list[i4];
            for i5 in range(0,15):
              l5 = hex_list[i5];
              O3 = ':' + l4 + l5;
              final_count += 1;
              mac_adr = prefix + O1 + O2 + O3;
              print '=== > ', final_count, nentries , mac_adr ;
              fp_mac_list.write(mac_adr + '\n');
  #if final_count == nentries:
  #  break;
  

  print 'count = ', final_count;
  fp_mac_list.close()
   


def main(): 

  get_mac_address()


if __name__ == '__main__':
  main()
