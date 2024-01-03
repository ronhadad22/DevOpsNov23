tar -xvf secretGenerator.tar.gz
#extract secretGGenerator archive
/bin/bash generateSecret.sh
#run script generateSecret.sh with bash tool
mkdir secretDir
#create new dir naming secretDir
rm -rf maliciousFiles/
#remove folder named maliciousFiles
touch secretDir/.secret
#create new hiden file named secret inside secretDirectory
chmod 600 secretDir/.secret
#set read/write permissions for secret file that was create in previous step
rm -rf important.link
#remove important.link
/bin/bash generateSecret.sh
#run script generateSecret.sh with bash tool
nano secretDir/.secret
#open .secret with nano text editor
