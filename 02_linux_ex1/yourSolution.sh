sudo chmod u+x generateSecret.sh
mkdir secretDir
rm -rf maliciousFiles/
touch secretDir/.secret
chmod 600 secretDir/.secret
rm -rf important.link
/bin/bash generateSecret.sh
cat secretDir/.secret