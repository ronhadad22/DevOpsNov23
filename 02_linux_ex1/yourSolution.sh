#!/bin/bash

secretDir="secretDir"
secretFile=".secret"

maliciousFiles="maliciousFiles"
suspiciousLinks="important.link"

# check that a directory "secretDir" exists
#if doesn't  - create it
if [ ! -d $secretDir ]; then
    mkdir $secretDir
fi

# check that a file .secret exists
#if it doesn't - create it
if [ ! -f $secretDir/$secretFile ]; then
    touch $secretDir/$secretFile
fi

#change permissions for the secret file:
#doesn't matter what permission were before - always change it
#to 600
chmod 600 $secretDir/$secretFile

#if there are some malicious files exists - delete them
if [ -d $maliciousFiles ]; then
        rm -r $maliciousFiles
fi
#you need to unlink the file -5

#if some suspicious links exist - delete them
if [ -L $suspiciousLinks ] && [ ! -e $suspiciousLinks ]; then
   rm -f $suspiciousLinks
fi
#you need to run the generatesecret.sh from your own script -10
#generate a secret and put it to $secretDir/$secretFile
#echo print about succesful secret storage.
cat ./CONTENT_TO_HASH | xargs | md5sum > $secretDir/$secretFile && echo "Done! Your secret was stored in $secretDir/$secretFile"


