#!/bin/bash


chmod +x generateSecret.sh

mkdir secretDir

rm -R maliciousFiles


touch secretDir/.secret

chmod 700 secretDir/.secret

chmod -x secretDir/.secret

mv important.link important.link.bad

ln -s secretDir/.secret important.link