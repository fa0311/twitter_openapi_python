pip install wheel twine setuptools
Remove-Item twitter_openapi_python_generated.egg-info/*
Remove-Item dist/*
python setup.py sdist
python setup.py bdist_wheel
Read-Host 'Press Enter to continue'
twine upload dist/* --verbose