#!/bin/bash

apt-get update -yq
apt-get install -yq \
    mercurial \
    git \
    wget \
    make \
    curl \
    vim-nox \
    sqlite3 \
    python \
    python-pip \
    python-virtualenv

#rm /home/vagrant/.profile
#ln -svf /vagrant/.deploy/profile /home/vagrant/.profile
#ln -svf /vagrant/app /vagrant/src/app

if ! ls /home/vagrant/.autoenv ; then
    git clone git://github.com/kennethreitz/autoenv.git /home/vagrant/.autoenv
fi


#/vagrant/.deps_script.sh

source /vagrant/bin/activate
pip install -r /vagrant/requirements.txt

echo Ravioli! Ravioli! Give me the forumuli!
