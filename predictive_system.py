# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file."""
import pickle 
import numpy as np
github_raw_url = 'https://raw.githubusercontent.com/aryaananya03/migraine/main/migraine.sav'

# Fetch the raw content of the file from GitHub
response = requests.get(github_raw_url)

# Check if the request was successful
if response.status_code == 200:
    # Load the model from the content
    load_model = pickle.loads(response.content)
else:
    # Handle the case where the request was not successful
    print("Failed to fetch the model file from GitHub.")


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
