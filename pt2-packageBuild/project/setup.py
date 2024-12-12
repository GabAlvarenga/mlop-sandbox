
from setuptools import find_packages, setup


# Metadata of package
NAME = 'generic_script_laksdlka'
DESCRIPTION = 'generic scrip'
URL = 'https://github.com/GabAlvarenga/mlop-sandbox'
EMAIL = 'gaalvarenga@email.com'
AUTHOR = 'gaalvarenga'
REQUIRES_PYTHON = '>=3.7.0'


setup(
    name=NAME,
    version="0.0.1",
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(),
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
