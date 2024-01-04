!bin/bash
#Check if File is exist already if not extract secretGGenerator archive
if
  test -e secretGenerator.tar.gz; then
    echo "file already exist"
fi
#Download file
  wget https://github.com/ronhadad22/DevOpsNov23/blob/main/02_linux_ex1/secretGenerator.tar.gz
#Extract the Archjve
  tar -xvf secretGenerator.tar.gz
#Enter to extracted folder
  cd src
#Change yourSolution file to executable
   sudo chmod u+x generateSecret.sh
#create new directory named secret dir
  mkdir secretDir
#remove folder named maliciousFiles
  rm -rf maliciousFiles/
#create new hiden file named secret inside secretDirectory
  touch secretDir/.secret


)
###
#/bin/bash generateSecret.sh
#run script generateSecret.sh with bash tool
#mkdir secretDir
#create new dir naming secretDir
#rm -rf maliciousFiles/
#remove folder named maliciousFiles
# secretDir/.secret
#create new hiden file named secret inside secretDirectory
#chmod 600 secretDir/.secret
#set read/write permissions for secret file that was create in previous step
#rm -rf important.link
#remove important.link
#/bin/bash generateSecret.sh
#run script generateSecret.sh with bash tool
#nano secretDir/.secret
#open .secret with nano text editor


