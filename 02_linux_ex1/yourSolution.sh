#!/bin/bash

# Set variables for archive, directory, and secret

export secret_gen=./src/secretDir/generateSecret.sh
export source=./src
export secretdir=/src/secretDir
export secret=./src/secretDir/.secret
export arch=secretGenerator.tar.gz

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