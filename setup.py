from setuptools import find_packages, setup

setup(
    name='redworthapp',
    version='1.0.8',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)
