

git init
git pull https://github.com/ronhadad22/DevOpsNov23.git
cd 02_linux_ex1
tar -xzvf secretGenerator.tar.gz
cd src
cp generateSecret.sh ../
cd ..
mkdir secretDir
cd secretDir
touch .secret
chmod 600 .secret
cd ..
chmod +x generateSecret.sh
./generateSecret.sh
cat secretDir/.secret
