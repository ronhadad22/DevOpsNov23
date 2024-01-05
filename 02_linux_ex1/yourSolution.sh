#!/bin/bash

# Set variables for archive, directory, and secret
arch=secretGenerator.tar.gz
secret_gen=generateSecret.sh
secretdir=./src/secretDir
secret=./src/secretDir/.secret

# Download secretGenerator archive if it doesn't exist
wget -N https://github.com/ronhadad22/DevOpsNov23/blob/main/02_linux_ex1/secretGenerator.tar.gz

# Extract the archive
tar -xvf $arch

# Change working directory to src and make generateSecret.sh executable
cd src
sudo chmod u+x $secret_gen

# Create new directory named secretDir
mkdir -p $secretdir

# Remove folder named maliciousFiles
rm -rf maliciousFiles/

# Create new hidden file named .secret inside secretDir and set read/write permissions
touch $secret && chmod 600 $secret

# Remove file named important.link
rm -f important.link

# Run generateSecret.sh script with bash tool
./$secret_gen

# Show contents of .secret file
cat $secret