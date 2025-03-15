# Template file to create all the files automatically

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = 'text-summarizer'

list_of_files = [
    ".github/workflows/.gitkeep", # .gitkeep t's a convention to keep empty directories in git
    f"src/{project_name}/__init__.py", # constructor to handle the local package
    f"src/{project_name}/components/__init__.py", 
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constatnts/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
]  
    
# windows uses bw slash so to handle that we use pathlib it detects the os and provides path acc to req of os

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath) # it will return filedir and filename from the path

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)  # it will create the directory if it does not exist
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    if not (os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as file:
            logging.info(f"Creating empty file: {filepath}")
            file.write("")

    else:
        logging.info(f"{filename} already exists")

# to add new files to the project just add the file path / folder path to the list_of_files