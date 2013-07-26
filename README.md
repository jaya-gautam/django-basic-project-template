# Django-basic-project-template

This Django project template is customized to our workflow. It can be used
as is or as a starting point to make your own template.

The `bc` branch contains a few specific settings and relies on some internal
tools. For a random stranger the `master` branch is a way to go.

## Make sure you have virtualenvwrapper configured (once)

Install virtualenvwrapper and deps with pip or your packagemanager.

    pip install virtualenvwrapper

Add something like this to .bashrc:

    export VIRTUALENV_DISTRIBUTE=true
    # virtualenvwrapper
    export WORKON_HOME=~/.virtualenvs
    export PROJECT_HOME=~/Workplace/Sources/web/django
    export VIRTUALENVWRAPPER_SCRIPT=/usr/bin/virtualenvwrapper.sh
    source /usr/bin/virtualenvwrapper_lazy.sh

Source it or launch a new shell.

## Django project setup

### Start new django project from template

    export PROJECT_NAME=yourprojectname
    mkproject $PROJECT_NAME
    git clone https://github.com/mikek/django-basic-project-template.git -b bc
    pip install `grep "^django[=><]" django-basic-project-template/requirements/common.txt`
    mkdir project
    django-admin.py startproject --template=django-basic-project-template -n Vagrantfile,.gitignore -e py,sh,cron $PROJECT_NAME project
    echo `pwd`/project > $VIRTUAL_ENV/.project
    ln -s development.py project/$PROJECT_NAME/settings/__init__.py
    rm -rf django-basic-project-template

### Integration with optional tools

This template integrates with a few optional tools

#### Fabric's fabfile.py based on webdev-fab project

Included `fabfile.py` has helpful comments.

#### Chef's kitchen to provision a host to be able to run Django project

[django-kitchen](https://github.com/mikek/django-kitchen) project provides
initial kitchen structure and example node configuration. You can place it
anywhere you like.

#### Vagrant setup to work on a project inside a VM

If you are working in a full featured UNIX-like environment with recent version
of Python installed - you can safely remove all Vagrant-related stuff:

    rm -rf Vagrant*

Otherwise, please refer to the included `Vagrantfile.README`.

## Work on existing project

To work on existing project - clone it in the same directory instead
of using project template.

The resulting structure should look like this:

    yourprojectname/
    |-- project/
    |   |-- .git
    |   |-- manage.py
    |   |-- fabfile.py
    [...]
    |   |-- yourprojectname/
    |   |   |-- apps/
    |   |   |-- core/
    |   |   |-- media/
    [...]

## Daily workflow

    workon yourprojectname
    pip install -r requirements/development.txt
    ./manage.py runserver

## Related links

 * [webdev-fab](https://github.com/mikek/webdev-fab)
 * [django-kitchen](https://github.com/mikek/django-kitchen)
 * [Vagrant](http://www.vagrantup.com)
