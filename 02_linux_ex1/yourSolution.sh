#/bin/bash.sh
tar xfv secretGenerator.tar.gz
cd src
mkdir secretDir
cd secretDir
touch .secret
chmod 600 .secret
cd ..
rm -rf maliciousFiles
rm -rf important.link
#/bin/bash generatesecret.sh
