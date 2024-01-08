#!/bin/bash
GREEN='\033[0;32m' #seting variable for color
arch=secretGenerator.tar.gz
# Download secretGenerator archive if it doesn't exist(NOT WORKED LAST TIME )
#wget -N https://github.com/ronhadad22/DevOpsNov23/blob/main/02_linux_ex1/secre>
# Extract the archive and aplly permissions on file generateSecret.sh inside fo>
tar -xvf $arch && cd ./src && sudo chmod u+x generateSecret.sh
#remove malisious Files and important links
rm -rf maliciousFiles && rm -rf important.link
#create new dir named secretDir with the new hidden file secret that have only >
mkdir secretDir && touch secretDir/.secret && chmod 600 secretDir/.secret
#Run script called generateSecret
./generateSecret.sh
#clear output
clear
#Show as output file secret that was created on previous steps
echo -e "${GREEN}your secret is : " && cat secretDir/.secret
