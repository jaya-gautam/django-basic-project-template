#!/bin/bash
#
# Script to set up a Vagrant box for Django project.
#

set -x

PGSQL_VERSION=9.1
DATA_DIR="/vagrant/Vagrantfile.provision"
AS_VAGRANT="/usr/bin/sudo -u vagrant"


export LANGUAGE=en_US.UTF8
export LANG=en_US.UTF8
export LC_ALL=en_US.UTF8
locale-gen en_US.UTF8
dpkg-reconfigure locales
echo "LANG=en_US.UTF8" > /etc/default/locale
echo "LANGUAGE=en_US.UTF8" >> /etc/default/locale
echo "LC_ALL=en_US.UTF8" >> /etc/default/locale

# Install essential packages
apt-get update -y
apt-get install -y build-essential \
  python python-dev python-setuptools python-pip \
  git mercurial mc wget curl \
  gettext libxml2 libxslt1-dev libjpeg-dev libpng-dev libfreetype6-dev \
  postgresql-$PGSQL_VERSION postgresql-contrib-$PGSQL_VERSION postgresql-plperl-$PGSQL_VERSION libpq-dev
apt-get clean
pip --quiet install virtualenvwrapper

# postgresql setup
install -m 0640 -o postgres -g postgres $DATA_DIR/pg_hba.conf /etc/postgresql/$PGSQL_VERSION/main/pg_hba.conf
#sed -i "s|\ =\ 'localhost'|\ =\ '*'|g" /etc/postgresql/$PGSQL_VERSION/main/postgresql.conf
echo "listen_addresses = '*'" >> /etc/postgresql/$PGSQL_VERSION/main/postgresql.conf
/etc/init.d/postgresql restart

# TODO: download and update to latest VBoxGuestAdditions.iso

#CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

$AS_VAGRANT -s -- cat $DATA_DIR/bashrc_additions >> /home/vagrant/.bashrc
$AS_VAGRANT -s -- cat $DATA_DIR/profile_additions >> /home/vagrant/.profile
$AS_VAGRANT -s -- cat $DATA_DIR/aliases_additions >> /home/vagrant/.bash_aliases


PROJECT_NAME=$1
if [ -z $2 ]; then
    DB_NAME=$PROJECT_NAME
else
    DB_NAME=$2
fi

DB_USER=$DB_NAME
VIRTUALENV_NAME=$PROJECT_NAME
PROJECT_DIR=/home/vagrant/projects/$PROJECT_NAME
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/$PROJECT_NAME

sudo -u postgres psql -c "CREATE ROLE $DB_USER LOGIN UNENCRYPTED PASSWORD '$DB_USER' NOSUPERUSER INHERIT NOCREATEDB NOCREATEROLE NOREPLICATION;"
sudo -u postgres /usr/bin/createdb --echo --locale=en_US.UTF8 --owner=$DB_USER $DB_NAME

rm -rf $VIRTUALENV_DIR
$AS_VAGRANT -s -- /usr/local/bin/virtualenv --distribute $VIRTUALENV_DIR
$AS_VAGRANT -s -- echo $PROJECT_DIR > $VIRTUALENV_DIR/.project
$AS_VAGRANT -s -- echo "workon $VIRTUALENV_NAME" >> /home/vagrant/.bashrc

# Django project initial setup
#$AS_VAGRANT -s -- /usr/bin/pip --quiet install -E $VIRTUALENV_DIR -r $PROJECT_DIR/requirements/development.txt
#chmod a+x $PROJECT_DIR/manage.py
#$AS_VAGRANT -i -- "source $VIRTUALENV_DIR/bin/activate && cd $PROJECT_DIR && ./manage.py syncdb --noinput && ./manage.py migrate"
