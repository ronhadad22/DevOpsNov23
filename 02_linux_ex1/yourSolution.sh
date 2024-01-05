#!/bin/bash
#Download file
#  wget https://github.com/ronhadad22/DevOpsNov23/blob/main/02_linux_ex1/secretGenerator.tar.gz (not worked last time)
#Extract the Archive
tar -xvf ./secretGenerator.tar.gz
#change work directory to src that was extracted from the archive
cd ./src
#Change generateSecret.sh file to executable
sudo chmod u+x generateSecret.sh
#create new directory named secret dir
mkdir secretDir
#remove folder named maliciousFiles
rm -rf maliciousFiles/
#create new hiden file named secret inside secretDirectory
touch secretDir/.secret
#set read/write permissions for secret file that was created.
chmod 600 secretDir/.secret
#remove important.link
rm -rf important.link
#run script generateSecret.sh with bash tool
/bin/bash generateSecret.sh
#show secret file content
cat secretDir/.secret

#CAUTION--UNDER CONSTRUCTION--CAUTION--UNDER COUNSTRUCTION----CAUTION--UNDER COUNSTRUCTION----CAUTION--UNDER COUNSTRUCTION--
#NOT WORK , PLEASE FOLLOW TO VERSION 1
# Set variables for archive, directory, and secret
export secret_gen=/src/secretDir/generateSecret.sh
export source=/src
export secretdir=/src/secretDir
export secret=/src/secretDir/.secret
arch=secretGenerator.tar.gz
# Download secretGenerator archive if it doesn't exist
wget -N https://github.com/ronhadad22/DevOpsNov23/blob/main/02_linux_ex1/secretGenerator.tar.gz
# Extract the archive
tar -xvf ${arch}
# Change working directory to src and make generateSecret.sh executable
cd ${source}
sudo chmod u+x ${secret_gen}
# Create new directory named secretDir
mkdir -p ${secretdir}
# Remove folder named maliciousFiles
rm -rf ./src/maliciousFiles/
# Create new hidden file named .secret inside secretDir and set read/write permissions
touch ${secret} && chmod 600 ${secret}
# Remove file named important.link
rm -f ./src/important.link
# Run generateSecret.sh script with bash tool
./${secret_gen}
# Show contents of .secret file
cat ${secret}


