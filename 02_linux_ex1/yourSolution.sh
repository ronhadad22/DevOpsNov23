#!/bin/bash
#Setting Variables for folders and files
GREEN='\033[0;32m' #seting variable for color
arch=secretGenerator.tar.gz
source=./src
secretgen=generateSecret.sh
files=maliciousFiles
links=important.link
dir=secretDir
# Download secretGenerator archive if it doesn't exist(NOT WORKED LAST TIME )
#wget -N https://github.com/ronhadad22/DevOpsNov23/blob/main/02_linux_ex1/secre>
# Extract the archive and aplly permissions on file generateSecret.sh inside folder src
tar -xvf $arch && cd $source && sudo chmod u+x $secretgen
#remove malisious Files and important links
rm -rf $files && rm -rf $links
#create new dir named secretDir with the new hidden file secret that have only >
mkdir $dir && touch $dir/.secret && chmod 600 $dir/.secret
#Run script called generateSecret
./$secretgen
#clear output
clear
#Show as output file secret that was created on previous steps
echo -e "${GREEN}your secret is : " && cat $dir/.secret
