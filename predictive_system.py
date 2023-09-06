# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file."""
import pickle 
import numpy as np
load_model=pickle.load(open("C:/migraine project/migraine.sav","rb"))


input_data_numpy=np.asarray(input_data)
input_reshape= input_data_numpy.reshape(1,-1)

prediction= load_model.predict(input_reshape)
print(prediction)

if (prediction[0]==0):
    print('yes')
elif(prediction[0]==1):
    print("f")
elif(prediction[0]==2):
    print("g")
elif(prediction[0]==3):
    print("h")
elif(prediction[0]==4):
    print("i")
elif(prediction[0]==5):
    print("j")
else:
    print("k")
