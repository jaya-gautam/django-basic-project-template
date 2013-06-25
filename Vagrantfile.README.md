Brief instructions to launch django development environment
=====

Initial provisioning
-------

    vagrant up

Connect to provisioned vagrant box
-------

### From UNIX

Run:

    vagrant ssh

(If you want to connect with plain ssh command, look at the Windows section
below and find the actual vagrant's private key in vagrant source tree in
'keys' directory.)


#### From Windows

Try ro run:

    vagrant ssh

Look up vagrant key path, run:

    cp path/to/.vagrant.d/insecure_private_key ~/.ssh/vagrant_rsa

Add the following to ~/.ssh/config:

    Host vagrantbox
        HostName 127.0.0.1
        User vagrant
        Port 2222
        IdentityFile ~/.ssh/vagrant_rsa

Now you can run:

    ssh vagrantbox

Install project deps, migrate, check
-------

Create settings symbolic link on the host (shareed Virtualbox FS does not allow
symlinks):

    pushd path/to/settings
    ln -s development.py __init__.py
    # on Windows:
    # mklink __init__.py development.py
    popd

### Setup the guest

#### Make sure the guest can work with private repos

Copy your real private key (SECURITY-DUMB way if you can't keep this
vagrant box private):

    scp ~/.ssh/id_rsa{,.pub} vagrantbox:.ssh/
    ssh vagrantbox "chmod -R go-rwx ~/.ssh"

The other way is to make sure each private repo the project depends on uses
special deployment key: see
[example Bitbucket instructions](https://confluence.atlassian.com/x/I4CNEQ)

### Initial project setup

    chmod +x ./manage.py
    install_deps
    migrate

Alternatively you can upload database dump with pgadmin. Or do it by hand:

    export DB="${PWD##*/}"
    sudo -u postgres dropdb $DB
    sudo -u postgres createdb -E UTF8 -O $DB $DB
    sudo -u postgres pg_restore -d $DB /path/to/$DB.backup

### Make sure it works

    runserver

Do not forget the media/uploads if you need them. Now site should be
accessible from the host at `localhost:18000`, and PostgreSQL
server - at `localhost:15432`.

Running the environment
-------

    vagrant up --no-provision (DO NOT FORGET THAT OPTION!)
    vagrant ssh (or "ssh vagrantbox" from Windows)
    runserver

I want more handy aliases!
-----------

On host run something like this:

    echo "alias vagrant_up='vagrant up --no-provision'" >> ~/.bashrc
    source ~/.bashrc

Then you can just boot the host with

    vagrant_up
