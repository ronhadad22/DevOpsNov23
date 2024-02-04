
# creating git repository
git init
# pulling pulling the repository from github 
git pull https://github.com/ronhadad22/DevOpsNov23.git
#why to involve git?? -5
cd 02_linux_ex1
# unpacking the compressed file 
tar -xzvf secretGenerator.tar.gz
cd src
# move generateSecret.sh from src folder (created by default in src)
cp generateSecret.sh ../
cd ..
# creating folder with name secret Dir (generateSecret.sh searching for the directory secretDir)
mkdir secretDir
cd secretDir
# creating file with name .secret (generateSecret.sh searching for the directory/.secret )
touch .secret
# changing permissions to 600 to pass if in script generateSecret.sh
chmod 600 .secret
cd ..
# adding permission execute to generateSecret.sh to pass permission problem
#what about the important.link?? -5
chmod +x generateSecret.sh
# runing generateSecret.sh to generate Secret
./generateSecret.sh
# display the Secret that generated in secretDir/.secret   
cat secretDir/.secret
