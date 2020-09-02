from flask import Flask, render_template, request, redirect, url_for
import numpy as np
import pickle
import pandas as pd
from sklearn.metrics import accuracy_score
import logging
#import flask_monitoringdashboard as dashboard
from train_code.input import input
from train_code.pre_processing import pre_processing
from validation import validation
from train_code.model import model

logger = logging.getLogger("train_path")

f_handler = logging.FileHandler('log_records/file.log')
f_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')#set the format
f_handler.setFormatter(formatter)

logger.addHandler(f_handler)







app=Flask(__name__)
#dashboard.bind(app)


pickle_in = open("modules/DecisionTreeClassifier.pkl","rb")
classifier=pickle.load(pickle_in)


pickle_in1 = open("modules/KNeighborsClassifier.pkl","rb")
classifier1=pickle.load(pickle_in1)

pickle_in2 = open("modules/RandomForestClassifier.pkl","rb")
classifier2=pickle.load(pickle_in2)












@app.route('/')
def home():
    logger.warning("welcome to home page")
    return render_template('home.html')
 

@app.route('/', methods=['POST'])
def upload_file():   
    try:
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            path = "data/test/"+uploaded_file.filename
            uploaded_file.save(path) # here we can try to save data in upload folder##############################upload in specifi 
            validation_check = validation()
            column_names, noofcolumns=validation_check.valuesFromSchema()
            valid= validation_check.validateColumnLength(path,noofcolumns)
            print(valid)
            if valid == 0:
                return render_template('error.html')
            else:
                return redirect(url_for('home')) # going to home page only
        else:
                return redirect(url_for('home')) # going to home page only
    except ValueError:
        logger.error("Error Occurred! %s" %ValueError)
    except KeyError:
        logger.error("Error Occurred! %s" %KeyError)
    except Exception as e:
        logger.error("Error Occurred! %s" %e)
      
@app.route('/train',methods=['GET','POST'])
def train():                                         # IT SHOULD BE RETRAIN
    try:
        logger.warning("starting og trainning ")
        #data = pd.read_excel('Data_Cortex_Nuclear.xls') # take original data
        df=pd.read_csv('data/test/test.csv')                      
        data1=df.drop(df.columns[0], axis = 1)
        #print(data1.shape)# user data
        logger.warning("data loading completed ")
        
        #original data loaded into a1.data
        a1=input()
        a1.input1()
        #print(a1.data.shape)
        #original data pre-processing
        b=pre_processing()
        b.data=a1.data
        b.null_list=a1.null_list   ###again 
        b.preprocessing()
        
        b.input_preprocessing(data1)# data1 is user data
        
        #print(b.data.tail())
        
        #model building
        c=model()
        c.data=b.data#its preprocess data
        c.data_original=a1.data
        c.model()
        logger.warning("data pre-processing completed ")
        logger.warning("all 3 models succesfully trained")
        return redirect(url_for('home')) # going to home page only 
    except ValueError:
        logger.error("Error Occurred! %s" %ValueError)
    except KeyError:
        logger.error("Error Occurred! %s" %KeyError)
    except Exception as e:
        logger.error("Error Occurred! %s" %e)

@app.route('/predict',methods=['GET','POST'])
def predict():
    try:
        logger.warning("starting of pre-processing of new data ")
        #df=pd.read_csv('test.csv')                      # take test dayta              # first test data was there
        #data2=df.drop(df.columns[0], axis = 1)
        #a.input_pre(data2)
        logger.warning("data pre-processing done and stored in file111.csv")
        df1=pd.read_csv('data/test/file111.csv')
        data1=df1.drop(df1.columns[0], axis = 1)
        dataa=data1.drop(['class'], axis = 1) 
        id=df1.MouseID
        id1=id.to_numpy()
        my_prediction=classifier.predict(dataa)
        dict1=[]
        for i in range (0,len(id1)-1):
            dict1.append(dict(id=id1[i],class1=my_prediction[i]))
            logger.warning(" prediction done using DecisionTreeClassifier ")
        return render_template('resultDecisionTreeClassifier.html',prediction = dict1) 
    except ValueError:
        logger.error("Error Occurred! %s" %ValueError)
    except KeyError:
        logger.error("Error Occurred! %s" %KeyError)
    except Exception as e:
        logger.error("Error Occurred! %s" %e)
        
@app.route('/predict1',methods=['GET','POST'])
def predict1():
    
    logger.warning("starting of prediction path using KNeighborsClassifier ")
    #logger.warning("starting of pre-processing of new data ")
    #df=pd.read_csv('test.csv'
    #data2=df.drop(df.columns[0], axis = 1)
    #a.input_pre(data2)
    #logger.warning("data pre-processing done and stored in file111.csv")
    df1=pd.read_csv('data/test/file111.csv')  
    #data=df.drop(df.columns[0], axis = 1) 
    data1=df1.drop(df1.columns[0], axis = 1)
    dataa=data1.drop(['class'], axis = 1) 
    id=df1.MouseID
    id1=id.to_numpy()
    my_prediction=classifier1.predict(dataa)
    print(my_prediction)
    dict2=[]
    print(dict2)
    for i in range (0,len(id1)-1):
        dict2.append(dict(id=id1[i],class1=my_prediction[i]))
        logger.warning(" prediction done using KNeighborsClassifier ")
    return render_template('resultKNeighborsClassifier.html',prediction = dict2,data = dataa) 

        
@app.route('/predict2',methods=['GET','POST'])

def predict2():
    try:
        logger.warning("starting of prediction path using RandomForestClassifier ")
        logger.warning("starting of pre-processing of new data ")
        #df=pd.read_csv('test.csv')                      # take test dayta              # first test data was there
        #data2=df.drop(df.columns[0], axis = 1)
        #a.input_pre(data2)
        logger.warning("data pre-processing done and stored in file111.csv")
        df1=pd.read_csv('data/test/file111.csv') 
        #data=df.drop(df.columns[0], axis = 1)  
        data1=df1.drop(df1.columns[0], axis = 1)
        dataa=data1.drop(['class'], axis = 1) 
        id=df1.MouseID
        id1=id.to_numpy()
        my_prediction=classifier2.predict(dataa)
        dict3=[]
        for i in range (0,len(id1)-1):
            dict3.append(dict(id=id1[i],class1=my_prediction[i]))
            logger.warning(" prediction done using RandomForestClassifier ")
        return render_template('resultRandomForestClassifier.html',prediction = dict3,data = dataa) 
        
    except ValueError:
        logger.error("Error Occurred! %s" %ValueError)
    except KeyError:
        logger.error("Error Occurred! %s" %KeyError)
    except Exception as e:
        logger.error("Error Occurred! %s" %e)


@app.route('/about')
def about():
    logger.warning(" reading about problem statement ")
    return render_template('about.html')    

@app.route('/problem')
def problem():
    logger.warning(" reading about problem statement ")
    return render_template('problem.html')  

@app.route('/dashboard')
def dashboard():
    logger.warning(" reading about problem statement ")
    return redirect(url_for('dashboard')) # going to home page only 


@app.errorhandler(404)
def error404(error):
    return render_template('error.html')

if __name__=='__main__':
    app.run(host='0.0.0.0',port=8000)
    
#,host='0.0.0.0',port=8000    
