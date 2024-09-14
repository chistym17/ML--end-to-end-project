from setuptools import find_packages,setuptools
from typing import List

E_dot='-e .'

def get_all_requirements(file_name:str)->List[str]:
    requirements=[]
    with open(file_name) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        
        if E_dot in requirements:
            requirements.remove(E_dot)
    return requirements        


setup(
name='mlproject-end to end',
version='1',
author='chisty',
author_email='chistym17@gmail.com',
packages=find_packages(),
install_requires=get_all_requirements('requirements.txt')

)