
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

setup(
    name='PyBoltzTestData',  # Required
    packages=['PyBoltzTestData'],
    version='1.0.0',  # Required
    description='Simple project made to export data',  # Optional
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*, <4',
    install_requires=['tables', 'numpy==1.16.1'],  # Optional
    package_data={  # Optional
        'PyBoltzTestData': ['*.csv','*.npy','*.h5','Tests.npy'],
    },
)