#!/bin/bash


chmod +x generateSecret.sh

mkdir secretDir

rm -R maliciousFiles


touch secretDir/.secret

chmod 700 secretDir/.secret
#need to change to 600 -5
chmod -x secretDir/.secret

mv important.link important.link.bad
#need to unlink the file -5
ln -s secretDir/.secret important.link
#you need to run the generatesecret.sh -5
