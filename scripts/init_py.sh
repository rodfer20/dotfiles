#!/bin/sh

if [ -z "$1" ];then
    echo "[!] Error: failed to parse arg1"
    exit 1
fi
cp -r /home/trevalkov/templates/python3-package "$PWD/$1"
#ROOT="$1"
#INIT_MAIN="$1/__init__.py"

#MAIN="$1/main.py"

#SETUP="$1/setup.py"

#TESTS_DIR="$1/tests"
#INIT_TESTS="$1/tests/__init__.py"

#TESTS="$1/tests/tests.py"

#mkdir $ROOT
#touch $INIT_MAIN

#touch $MAIN
#chmod 770 $MAIN
#echo -e "#!/usr/bin/python3\n\n\ndef main():\n    return 0\n\n\nif __name__ == '__main__':\n    exit(main())\n" >> $MAIN

#touch $SETUP
#chmod 770 $SETUP
#echo -e "from setuptools import setup\nfrom setuptools import find_packages\n\n\nsetup(\n    name='$1',\n    version='0.0.0',\n    description='$1',\n    author='trevalkov',\n    author_email='sussurreiro@gmail.com,\n    url='https://github.com/trevalkov/$1',\n    packages=find_packages(),\n)" >> $SETUP

#mkdir $TESTS_DIR
#touch $INIT_TESTS

#touch $TESTS
#chmod 770 $TESTS
#echo -e "import pytest\n\n\ndef test():\n    return 0\n\n\nif __name__=='__main__':\n    exit(test())\n"  >> $TESTS
