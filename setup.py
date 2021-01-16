from setuptools import find_packages, setup

setup(
    name='redworthapp',
    version='1.1.1',
    packages=find_packages(),
    py_modules=['redworthapp.apiApp1', 'redworthapp.apiApp2', 'redworthapp.apiAppSignIn', 'redworthapp.requestCheck', 'redworthapp.databaseConnection', 'redworthapp.databaseConnectionTest'],
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
