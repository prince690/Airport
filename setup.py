from setuptools import find_packages,setup
from typing import List

def get_requirement(file_path:str)->List[str]:
    require=[]
    with open(file_path)  as file_obj:
        require=file_obj.readlines()
        require=[req.replace('\n','') for req in require]
        if '-e .' in require:
            require.remove('-e .')
    return require

setup(
    name='Aircraft sensor',
    author='Prince',
    email='ptks9930@gmail.com',
    version='0.0.1',
    package=find_packages(),
    install_requires=get_requirement('requirement.txt')
)