#usage python2 overlap.py fastq1 fastq2 test_file new_fastq
from datetime import datetime
print datetime.now()

from sys import argv
script, fastq1, fastq2, test, fastq = argv
pair1=open(fastq1,"r")
pair2=open(fastq2,"r")
overlap_test=open(test,"w")
overlap_fastq=open(fastq,"w")

title1=[]
sequence1=[]
plus1=[]
quality1=[]
sequence2=[]
quality2=[]
  
l=0
for line1 in pair1.readlines():
  l=l+1
  line1=line1.rstrip()
  if l%4==1:
    title1.append(line1)
  elif l%4==2:
    sequence1.append(line1)
  elif l%4==3:
    plus1.append(line1)
  else:
    quality1.append(line1)
pair1.close()
l2=0
for line2 in pair2.readlines():
  l2=l2+1
  if l2%4==2 :
    line2=line2.rstrip()
    sequence2.append(line2)
  elif l2%4==0:
    quality2.append(line2)
pair2.close()

for n in range(0,len(sequence1)):
  a=sequence1[n]
  b=sequence2[n]
  qualitya=quality1[n]
  qualityb=quality2[n]
  rc_b=""
  quality_rc_b=""
  list1=range(0,len(b))
  list2=list1[::-1]
  for i in list2:
    quality_rc_b=quality_rc_b+qualityb[i]
    if b[i]=="A":
      rc_b=rc_b+"T"
    elif b[i]=="T":
      rc_b=rc_b+"A"
    elif b[i]=="C":
      rc_b=rc_b+"G"
    elif b[i]=="G":
      rc_b=rc_b+"C"
    elif b[i]=="N":
      rc_b=rc_b+"N"
    
  ok=0
  numberofsequence=0
  for x in range(0,len(a)-14):
    if ok==0 and a[x]!="N": 
      for y in range(0, len(rc_b)):
        if a[x:x+5]==rc_b[y:y+5] : 
          for z in range(0,len(a)-x-4):        
            if a[x:len(a)-z]==rc_b[y:len(a)-z-x+y]:

              if z<5:
                overlap=a[x:len(a)-z]
                length=len(overlap)
                ok=ok+1
                if length>=15:
                  start=x+1
                  end=z+1
                  numberofsequence=numberofsequence+1
                  if z==0 and y==0:
                    qualitya_overlap=qualitya[x:len(a)-z]            
                    
                    overlap_test.write(str(n)+" "+str(numberofsequence)+" "+overlap+" "+str(start)+" "+str(end)+" "+str(length)+"\n"+a+"\n"+b+"\n")
                    overlap_fastq.write(title1[n]+"\n"+overlap+"\n"+plus1[n]+"\n"+qualitya_overlap+"\n")                         
            
              break 
              
overlap_test.close()
overlap_fastq.close()

print datetime.now()