# logic for creating folder structure for the project

import os 
from pathlib import Path #package for handling filepath related issues
import logging #to log values during runtime

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')

project_name="textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/configuration.py",
    "config/config.yaml",
    "params.yaml"
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"

]

for filepath in list_of_files:
    path=Path(filepath) #this path function gives path based on the operaring system like \-linux ,.windows-/
    filedir,filename=os.path.split(path)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"creating directory: {filedir} for the file :{filename}")
    
    if(not os.path.exists(filepath)) or (os.path.getsize(filepath)==0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"creating file: {filepath}")
    
    else:
        logging.info(f"{filepath} already exists")