import re
rx = r'\d+(?=$)'
#rx = r'(?<=.)(\d*)'
with open('private/version.json', 'r') as fr:
    s = fr.readline() 
    res = s.split('.')   
    incp = int(res[2])+1
    res[2] = str(incp) 
    newVer = ".". join(res)    
    with open('private/version.json', 'w') as fw: 
        fw.write(newVer)   
