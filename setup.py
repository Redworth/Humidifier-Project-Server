from setuptools import find_packages, setup

setup(
    name='redworthapp',
    version='1.0.6',
    packages=find_packages(),
    zip_safe=False,
    py_modules=['apiApp1', 'apiApp2', 'apiAppSignIn', 'databaseConnection', 'databaseConnectionTest', 'requestCheck', 'signInCheck', 'main']
    install_requires=[
        'flask',
    ],
)
