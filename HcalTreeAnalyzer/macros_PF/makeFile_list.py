import os
from glob import glob

K0L_path = '/cms/data/store/user/bcaraway/condor/outputs_2018/*K0L*.root'
files = glob(K0L_path)
outPut_txt = "filelist_K0L_10M.txt"
file_list = open(outPut_txt,"w")

for name in files:
    if os.path.getsize(name) > 10000:
        file_list.write("gsiftp://kodiak-se.baylor.edu/"+name+"\n")

file_list.close()
print "Output: "+outPut_txt
