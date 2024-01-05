!bin/bash
#Check if File is exist already if not Download secretGGenerator archive
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
#set read/write permissions for secret file that was created.
  chmod 600 secretDir/.secret
#remove important.link
  rm -rf important.link
#run script generateSecret.sh with bash tool
  /bin/bash generateSecret.sh
# secret file content
  cat secretDir/.secret

