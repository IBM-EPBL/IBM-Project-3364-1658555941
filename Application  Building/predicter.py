import re
import numpy as np
import os
from flask import Flask,request,render_template,redirect,url_for
import requests
from tensorflow import keras
from keras import models
from keras.models import Sequential
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
# from tensorflow.python.ops.gen_arrayPops import concat

model1=load_model('body.h5')
model2=load_model('level.h5')
class predicter:
    def predict(filepath):
        img=image.load_img(filepath,target_size=(224,224))
        x=image.img_to_array(img)
        x=np.expand_dims(x,axis=0)
        # img_data=preprocess_input(x)
        prediction1=np.argmax(model1.predict(x))
        prediction2=np.argmax(model2.predict(x))

        index1=['front','rear','side']
        index2=['minor','moderate','severe']

        result1=index1[prediction1]
        result2=index2[prediction2]
        print(result1,result2)

        if(result1=="front" and result2=="minor"):
            value = "3000 - 5000 INR"
        elif(result1=="front" and result2=="moderate"):
            value="6000 - 8000 INR"
        elif(result1=="front" and result2=="severe"):
            value="9000 - 11000 INR"
        elif(result1=="rear" and result2=="minor"):
            value="4000 - 6000 INR"
        elif(result1=="rear" and result2=="moderate"):
            value="7000 - 9000 INR"
        elif(result1=="rear" and result2=="severe"):
            value="11000 - 13000 INR"
        elif(result1=="side" and result2=="minor"):
            value="6000 - 8000 INR"
        elif(result1=="side" and result2=="moderate"):
            value="9000 - 11000 INR"
        elif(result1=="side" and result2=="severe"):
            value="12000 - 15000 INR"
        else:
            value= "16000 - 50000 INR"
        
        return value