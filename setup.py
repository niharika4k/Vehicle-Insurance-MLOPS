#This will let you to setup src foleder and setup packages. It will let u to install local packages into virtual env

from setuptools import setup, find_packages

setup(
    name="src",
    version="0.0.1",
    author="Vikash Das",
    author_email="vikashdas770@gmail.com",
    packages=find_packages()
)