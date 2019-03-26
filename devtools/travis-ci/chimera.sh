#!/bin/bash

wget https://raw.githubusercontent.com/insilichem/pychimera/master/scripts/install_chimera.sh
if [[ ! -e $HOME/chimera/bin/chimera ]]
then
    bash install_chimera.sh
fi