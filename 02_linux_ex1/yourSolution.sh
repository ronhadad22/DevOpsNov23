#!/bin/bash
arch=secretGenerator.tar.gz
# Download secretGenerator archive if it doesn't exist
#wget -N https://github.com/ronhadad22/DevOpsNov23/blob/main/02_linux_ex1/secretGenerator.tar.gz
# Extract the archive and aplly permisions on file generateSecret.sh inside folder src tath  part of the archive
tar -xvf $arch && cd ./src && sudo chmod u+x generateSecret.sh
#remove malisious Files and important links
rm -rf maliciousFiles && rm -rf important.link
#create new dir named secretDir with the new hidden file secret that have only w/r permisions
mkdir secretDir && touch secretDir/.secret && chmod 600 secretDir/.secret
#Run script called generateSecret
./generateSecret.sh
#clear output
clear
#Show as output file secret that was created on previous steps
echo "your secret is : " && cat secretDir/.secret

