from setuptools import find_packages, setup

from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open('requirements.txt') as file_obj:
        requirements = file_obj.readlines()
        [req.replace("\n","") for req in requirements]
        

        del requirements[-1]

    return requirements


setup(
    name = 'DoorDashProject',
    version = '0.0.1',
    author = "Big Josh",
    author_email = 'otoojoshua616@gmail.com',
    packages= find_packages(),
    install_require = get_requirements('requirements.txt')
)