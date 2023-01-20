## How to deploy package into PyPi
```bash
python setup.py sdist
twine upload dist/datalake_utils-version.tar.gz
```