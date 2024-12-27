from src.Airplane_sensor.logger import logging
from src.Airplane_sensor.exception import CustomException
from src.Airplane_sensor.component.data_injection import DataIngestion
import sys
if __name__=="__main__":
    try:
        data_injetion=DataIngestion()
        data_injetion.initiate_data_ingestion()
        
    except Exception as e:
        raise CustomException(e,sys)
    logging.info("to check if it's working or not")