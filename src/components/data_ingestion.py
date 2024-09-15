import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd 

from sklearn.model_selection import train_test_split
from dataclasses import dataclass

class DataIngestConfig:
    training_data_path:str=os.path.join("files","train.csv")
    testing_data_path:str=os.path.join("files","test.csv")
    raw_data_path:str=os.path.join("files","data.csv")
    
@dataclass
class DataIngestion:
    def __init__(self):
        self.ingestion=DataIngestConfig()
        
    def initiate_data_ingestion(self):
        logging.info("Initializing data ingestion method")
        try:
            df=pd.read_csv('notebook/data/stud.csv')
            logging.info("dataset read complete")
            os.makedirs(os.path.dirname(self.ingestion.training_data_path),exist_ok=True)
            df.to_csv(self.ingestion.raw_data_path,index=False,header=True)
            logging.info("Train test split started")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion.training_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion.testing_data_path,index=False,header=True)
            logging.info("data ingestion completed")
            
            return(
                self.ingestion.training_data_path,
                self.ingestion.testing_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)
        
if __name__=="__main__":
    data_obj=DataIngestion()
    train_data,test_data=data_obj.initiate_data_ingestion()
    