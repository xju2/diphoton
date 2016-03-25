#!/bin/bash
script_name=$BASH_SOURCE
currentDir=$PWD

#setup root
RootDir=/afs/cern.ch/atlas/project/HSG7/root/root_v6-04-02/x86_64-slc6-gcc49/
cd $RootDir
source bin/thisroot.sh
source $RootDir/setup.sh
cd $currentDir

#set ws code env
export DiphotonCode=$(cd $(dirname "${script_name}") && pwd -P)
export PATH=$PATH:${DiphotonCode}/scripts
