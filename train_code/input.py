import pandas as pd
import logging

logger = logging.getLogger("train_path")

f_handler = logging.FileHandler('log_records/file_input.log')##############################
#f_handler = logging.FileHandler('file_input.log')
f_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')#set the format
f_handler.setFormatter(formatter)

logger.addHandler(f_handler)


class input:
    """this class train contain input function for loading the data"""
    null_list=[]
    accuracy=[]
    
    def input1(self):
        """input function is used to read original file from the project folder + some basic data profilling """
        try:
            logger.warning("starting of input function")
            data = pd.read_excel('data/train/Data_Cortex_Nuclear.xls')
            cat_features=[i for i in data.columns if data.dtypes[i]=='object'] 
            for i in range (0,data.isnull().sum().shape[0]-1):
                if(data.isnull().sum()[i]>0):
                    self.null_list.append(data.isnull().sum().index[i])
                    self.data=data
                    self.cat_features=cat_features
                    logger.warning("we got categorial column {} and null column {}".format(len(cat_features),len(self.null_list)))
        except ValueError:
            logger.error("Error Occurred! %s" %ValueError)
        except KeyError:
            logger.error("Error Occurred! %s" %KeyError)
        except Exception as e:
            logger.error("Error Occurred! %s" %e)

      
        
		
                                                        		      
    
# = input()
