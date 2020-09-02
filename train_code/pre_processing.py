from sklearn import preprocessing 
import logging
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import pandas as pd



logger = logging.getLogger("train_path")

f_handler = logging.FileHandler('log_records/file_pre.log')###############################
#f_handler = logging.FileHandler('file_pre.log')
f_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')#set the format
f_handler.setFormatter(formatter)

logger.addHandler(f_handler)

class pre_processing:
    """this class train contain all methods required for the main.py"""
    null_list=[]

    
    def preprocessing(self):
        """this function used for pre-processing purpose of original data"""
        try:
            #handle null value
            #a.input1()#######################################################
            logger.warning("starting of pre-processing function")
            logger.warning("1st we perform handling of null data")
            null_list=self.null_list
            data=self.data
            #data=a.data###############################################
            #null_list=a.null_list#######################################
            for i in range (0,len(null_list)):
                data[null_list[i]]=data[null_list[i]].fillna(data[null_list[i]].mean())            
                #data['H3MeK4_N']=data['H3MeK4_N'].fillna(data['H3MeK4_N'].mean())##########################  c1
                #handle catogorial values
            logger.warning("2nd we convert catogorial data into integer")
            label_encoder = preprocessing.LabelEncoder() 
            data['MouseID']=label_encoder.fit_transform(data['MouseID'])################################### c2
            #data.drop(['MouseID'],axis=1,inplace=True)###################################################### c3
            data['Genotype']= label_encoder.fit_transform(data['Genotype']) 
            data['Treatment']= label_encoder.fit_transform(data['Treatment']) 
            data['Behavior']= label_encoder.fit_transform(data['Behavior'])   
            data['class']= label_encoder.fit_transform(data['class']) 
            #print(data.tail())
            #print(data.shape)
            #print(data.isnull().sum())
            #handle outlire
            logger.warning("3rd we handle outlire ")
            for i in range(1,len(data.columns)-5):
                IQR=data[data.columns[i]].quantile(0.75)-data[data.columns[i]].quantile(0.25)
                upper_bridge=data[data.columns[i]].quantile(0.75)+(IQR*1.5)
                data.loc[data[data.columns[i]]>=upper_bridge,data.columns[i]]=upper_bridge
                logger.warning("data preprocessing completed")
            print(data.tail())
            print(data.shape)
            
            #scaler=StandardScaler()
            #scaler.fit(data)
            #scaled_data=scaler.transform(data)
            #pca=PCA(n_components=20)
            #pca.fit(scaled_data)
            #data_p=pca.transform(scaled_data)
            
            #data_pca=pd.DataFrame(data_p)

            
            #print(data_pca.tail())
            #print(data_p.shape)
            #self.data=data_p
            
            
            
            
            
            
            
            
            
            
        except ValueError:
            logger.error("Error Occurred! %s" %ValueError)
        except KeyError:
            logger.error("Error Occurred! %s" %KeyError)
        except Exception as e:
            logger.error("Error Occurred! %s" %e)

      



    
    def input_preprocessing(self,input_data):
        """this function used for pre-processing purpose of test data which given by user"""
        try:
        
            logger.warning("starting of pre-processing processes for user input")
            #handle null values
            null_list=self.null_list
            data=input_data
            for i in range (0,len(null_list)-1):
                data[null_list[i]]=data[null_list[i]].fillna(data[null_list[i]].mean())            
                data['H3MeK4_N']=data['H3MeK4_N'].fillna(data['H3MeK4_N'].mean())  
            #handle catogorial values
            label_encoder = preprocessing.LabelEncoder() 
            data['MouseID']=label_encoder.fit_transform(data['MouseID']) 
            data['Genotype']= label_encoder.fit_transform(data['Genotype']) 
            data['Treatment']= label_encoder.fit_transform(data['Treatment']) 
            data['Behavior']= label_encoder.fit_transform(data['Behavior'])   
            data['class']= label_encoder.fit_transform(data['class']) 
            #handle outlire
            for i in range(1,len(data.columns)-5):
                IQR=data[data.columns[i]].quantile(0.75)-data[data.columns[i]].quantile(0.25)
                upper_bridge=data[data.columns[i]].quantile(0.75)+(IQR*1.5)
                data.loc[data[data.columns[i]]>=upper_bridge,data.columns[i]]=upper_bridge     
                
            data.to_csv('data/train/file111.csv')
            logger.warning("data preprocessing of input data is completed and store pre-proceesed input data into file111.csv file")

        except ValueError:
            logger.error("Error Occurred! %s" %ValueError)
        except KeyError:
            logger.error("Error Occurred! %s" %KeyError)
        except Exception as e:
            logger.error("Error Occurred! %s" %e)

#b = pre_processing()
#b.preprocessing()
     