#/bin/bash.sh
tar xfv secretGenerator.tar.gz
#go to directory
cd src
#creat adirectory secretDir
mkdir secretDir
#go to secretDir
cd secretDir
#creat file .secrer
touch .secret
#authoriz reed  write permission
chmod 600 .secret
#go back to src
cd ..
#delete mliciousFiles
rm -rf maliciousFiles
#delete important.link
rm -rf important.link
#generatesecret.sh
