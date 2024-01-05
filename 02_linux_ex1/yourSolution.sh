!bin/bash
#Seting Variables for archive , dir , secret etc...
arch=secretGenerator.tar.gz
secret_gen=generateSecret.sh
secretdir=secretDir
secret=secretDir/.secret
if
#Check if File is exist already if not Download secretGGenerator archive
  test -e $archive; then
    echo "file already exist"
 # else wget https://github.com/ronhadad22/DevOpsNov23/blob/main/02_linux_ex1/secretGenerator.tar.gz (NOT WORKED LAST TIME)
 #Download file didn't worked last time , link can be updated and line uncomented if needed
  tar -xvf $arch #Extract the Archive
#change work directory to src that was extracted from the archive and Change generateSecret.sh file to executable
    cd ./src && sudo chmod u+x $secret_gen
  mkdir $secretdir #create new directory named secretDr
    rm -rf maliciousFiles/ #remove folder named maliciousFiles
    # create new hiden file named secret inside secretDirectory,set read/write permissions
  touch $secret && chmod 600 $secret
    rm -rf important.link #remove important.link#remove important.link
  bin/bash/ $secret_gen #run script generateSecret.sh with bash tool
fi
echo $secret #Show secret file content

#Seting Variables for archive , dir , secret etc...
#Check if File is exist already if not Download secretGGenerator archive
#Download file
#  wget https://github.com/ronhadad22/DevOpsNov23/blob/main/02_linux_ex1/secretGenerator.tar.gz (not worked last time)
#Extract the Archive
#  tar -xvf secretGenerator.tar.gz
#change work directory to src that was extracted from the archive
#  cd src
#Change generateSecret.sh file to executable
#   sudo chmod u+x generateSecret.sh
#create new directory named secret dir
#  mkdir secretDir
#remove folder named maliciousFiles
#  rm -rf maliciousFiles/
#create new hiden file named secret inside secretDirectory
#  touch secretDir/.secret
#set read/write permissions for secret file that was created.
#  chmod 600 secretDir/.secret
#remove important.link
#  rm -rf important.link
#run script generateSecret.sh with bash tool
#  /bin/bash generateSecret.sh
# secret file content
#  cat secretDir/.secret


