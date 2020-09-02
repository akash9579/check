#from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split 
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle
import logging
from input import input
from pre_processing import pre_processing
import pandas as pd
import numpy as np


logger = logging.getLogger("train_path")

#f_handler = logging.FileHandler('log_records/file_model.log')
f_handler = logging.FileHandler('file_model.log')###################################################
f_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')#set the format
f_handler.setFormatter(formatter)

logger.addHandler(f_handler)





class model:
    
    def ma(self):
        print("hi")
    
    def model(self):
        """this function used for building all three models"""
        #logger.warning("model creation part started")
        #data=self.data
        a=input()
        b = pre_processing()
        a.input1()######################################################
        data1=a.data##################################################
        print(data1.shape)
        b.preprocessing()
        dataaa=b.data
        data=pd.DataFrame(dataaa)
        print(data)
        #print(data.type)
        x=data.iloc[:,0:81]
        y=data1.pop('class')
        print(x.head())
        print(x.shape)
        print(y.head())
        print(y.shape)
        #norm = MinMaxScaler().fit(x)
        #new_x = norm.transform(x)
        #X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = 0.25)
        
        #logger.warning("model for DecisionTreeClassifier is created")
        #dt = tree.DecisionTreeClassifier()
        #model = dt.fit(X_train, y_train)
        #prad = model.predict(X_test)
        #final=accuracy_score(y_test, prad)
        #print("DecisionTreeClassifier")
        #print(final)        
        #pickle_out = open("mod1/DecisionTreeClassifier.pkl","wb")
        #pickle.dump(model, pickle_out)
        #pickle_out.close()
            

ca=model()
ca.ma()
ca.model()
