from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split 
from sklearn import tree
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import pickle
import logging
#from input import input
#from pre_processing import pre_processing
#a=input()
#b=pre_processing()

logger = logging.getLogger("train_path")

f_handler = logging.FileHandler('log_records/file_model.log')
#f_handler = logging.FileHandler('file_model.log')###################################################
f_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')#set the format
f_handler.setFormatter(formatter)

logger.addHandler(f_handler)





class model:
    
    def ma(self):
        print("hi")
    
    def model(self):
        """this function used for building all three models"""
        
        try:

            logger.warning("model creation part started")
            data=self.data
            #a.input1()######################################################
            #data1=a.data##################################################
            #b.preprocessing()
            #data=b.data
            x=data.iloc[:,0:81]
            y=data.pop('class')
            #print(x.head())
            #print(x.shape)
            #print(y.head())
            #print(y.shape)
            norm = MinMaxScaler().fit(x)
            new_x = norm.transform(x)
            X_train, X_test, y_train, y_test = train_test_split(new_x, y, test_size = 0.25)
            
            logger.warning("model for DecisionTreeClassifier is created")
            dt = tree.DecisionTreeClassifier()
            model = dt.fit(X_train, y_train)
            prad = model.predict(X_test)
            final=accuracy_score(y_test, prad)
            print("DecisionTreeClassifier")
            print(final)        
            pickle_out = open("modules/DecisionTreeClassifier.pkl","wb")
            pickle.dump(model, pickle_out)
            pickle_out.close()
            
            logger.warning("model for KNeighborsClassifier is created")
            model1 = KNeighborsClassifier(n_neighbors=3)
            model1.fit(X_train, y_train)
            prad1=model1.predict(X_test)
            final1=accuracy_score(y_test, prad1)
            print("KNeighborsClassifier")
            print(final1)  
            pickle_out = open("modules/KNeighborsClassifier.pkl","wb")
            pickle.dump(model1, pickle_out)
            pickle_out.close()
            
            
            
            logger.warning("model for RandomForestClassifier is created")
            model2 = RandomForestClassifier(max_depth=2, random_state=0)
            model2.fit(X_train, y_train)
            prad2=model2.predict(X_test)
            final2=accuracy_score(y_test, prad2)   
            print("RandomForestClassifier")
            print(final2)  
            pickle_out = open("modules/RandomForestClassifier.pkl","wb")
            pickle.dump(model2, pickle_out)
            pickle_out.close()
            
            print("---------------------------------------------------------------------------------------------------------")
        

            logger.warning("all 3 model gets created and stored in modules folder succesfully")

        except ValueError:
            logger.error("Error Occurred! %s" %ValueError)
        except KeyError:
            logger.error("Error Occurred! %s" %KeyError)
        except Exception as e:
            logger.error("Error Occurred! %s" %e)


#ca=model()
#ca.maa()
