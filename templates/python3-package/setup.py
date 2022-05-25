from setuptools import setup
from setuptools import find_packages


setup(
    name='python3_package',
    version='0.0.0',
    description='template python3 package',
    author='trevalkov',
    author_email='trevalkov@protonmail.com',
    url='https://github.com/trevalkov/python3_package',
    packages=find_packages(exclude=('tests*', 'testing*')),
    py_modules=['lib'],
    entry_points={
        'console_scripts': [
            'mainpy = main.main:main',
            'testpy = test.test:test',
        ]
    }
    )
