from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return list of requirement
    '''

    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        [req.replace("\n", "") for req in requirements]

setup(
    name='studml',
    version='0.0.1',
    author='Krish',
    author_email='msgkrish192@gmail.com',
    package=find_packages(),
    install_requires=get_requirements('requirements.txt')

)