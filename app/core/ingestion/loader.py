import pandas as pd
from app.logger import logging
from app.Exception import MyException
import sys

class DataIngestion:
    def __init__(self,file_path):
        self.file_path=file_path
        
        
    def load_data(self):
        """
        load data into memory

         
        """
        logging.info("data Loaded into RAM")
        try:
            df=pd.read_csv(self.file_path)
            logging.info("return data as dataframe")
            return df
            
        except Exception as e:
            raise MyException(e,sys)
        
        
        
        
    