from src.ML_PROJECT.logger import logging
from src.ML_PROJECT.exception import CustomException
from src.ML_PROJECT.components.data_ingestion import DataIngestion,DataIngestionConfig

import sys



if __name__=='__main__':
    logging.info("Execution ho gaya start bhai")

    try:
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys) 