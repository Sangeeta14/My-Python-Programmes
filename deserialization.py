import pickle
fin = open ('mydata.serialized','r')
L=pickle.load(fin)
print L
fin.close()