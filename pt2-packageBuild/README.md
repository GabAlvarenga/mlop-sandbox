# Example Package

project
└── project
    ├── __init__.py
    └── main.py

# Virtual Environments

```
python -m venv venv python=3.10
.\pt2-packageBuild\venv\Scripts\activate
pip install setuptools twine
python setup.py sdist
twine upload --repository-url https://test.pypi.org/legacy/ \
  dist/hello_world_akjshya-0.0.1.tar.gz

pip install -i https://test.pypi.org/simple/ hello-world-akjshya==0.0.1

# another example
python setup.py sdist
twine upload --repository-url https://upload.pypi.org/legacy/ \dist/generic_script_laksdlka-0.0.1.tar.gz
```

generic_script_laksdlka-0.0.1.tar.gz