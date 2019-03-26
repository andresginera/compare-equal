#!/bin/bash

if test -e $HOME/miniconda/bin; then
    echo "miniconda already installed.";
else
    echo "Installing miniconda.";
    rm -rf $HOME/miniconda;
    mkdir -p $HOME/download;
    if [[ -d $HOME/download/miniconda.sh ]]; then rm -rf $HOME/download/miniconda.sh; fi;
    wget https://repo.continuum.io/miniconda/Miniconda2-latest-Linux-x86_64.sh -O $HOME/download/miniconda.sh;
    bash $HOME/download/miniconda.sh -b -p $HOME/miniconda;
fi