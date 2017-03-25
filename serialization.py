import pickle
L=[10,20,[30,40],'Hello',{1:2},60]
fout = open ('mydata.serialized','w')
pickle.dump(L,fout)
fout.close()