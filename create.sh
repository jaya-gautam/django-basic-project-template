#!/bin/bash

if [[ "$#" -ne 1 ]]; then
    echo "Usage: $0 new_project_name"
    exit 1
fi

source `which virtualenvwrapper.sh`

export PROJECT_NAME=$1
mkproject $PROJECT_NAME
git clone https://github.com/mikek/django-basic-project-template.git
pip install `grep "^django[=><]" django-basic-project-template/requirements/common.txt`
mkdir project
django-admin.py startproject --template=django-basic-project-template -n Vagrantfile,.gitignore -e py,sh,cron $PROJECT_NAME project
echo `pwd`/project > $VIRTUAL_ENV/.project
ln -s development.py project/$PROJECT_NAME/settings/__init__.py
rm -rf django-basic-project-template
