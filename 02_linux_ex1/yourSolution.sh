!bin/bash
#  wget https://github.com/ronhadad22/DevOpsNov23/blob/main/02_linux_ex1/secretGenerator.tar.gz
archive = 'secretGenerator.tar.gz'
secret_gen = 'generateSecret.sh'
dir = 'secretDir'
secret = 'secretDir/.secret'
if
  test -e $archive; then
    echo "file already exist"
  tar -xvf $archive
    cd ./src && sudo chmod u+x $secret_gen
  mkdir $dir
    rm -rf maliciousFiles/
  touch $secret && chmod 600 $secret
    rm -rf important.link
  bin/bash/ $secret_gen && echo $secret
fi
#Download file
#Check if File is exist already if not Download secretGGenerator archive
#  wget https://github.com/ronhadad22/DevOpsNov23/blob/main/02_linux_ex1/secretGenerator.tar.gz (not worked last time)
#Extract the Archive
#  tar -xvf secretGenerator.tar.gz
#change work directory to src that was extracted from the archive
#  cd src
#Change yourSolution file to executable
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

