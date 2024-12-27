import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO)

project="Airplane_sensor"

list_of_files=[
    f"src/{project}/__init__.py",
    f"src/{project}/component/__init__.py",
    f"src/{project}/component/data_injection.py",
    f"src/{project}/component/data_transformer.py",
    f"src/{project}/component/model_trainer.py",
    f"src/{project}/component/model_monitoring.py",
    f"src/{project}/pipeline/__init__.py",
    f"src/{project}/pipeline/trainer_pipeline.py",
    f"src/{project}/pipeline/Prediction_pipeline.py",
    f"src/{project}/logger.py",
    f"src/{project}/utils.py",
    f"src/{project}/exception.py",
    "Dockerfile",
    "main.py",
    "requirement.txt",
    "setup.py",
    "app.py"

]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")