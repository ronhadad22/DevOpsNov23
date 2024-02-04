#Create a secretDir for the Secret to be generated. 
mkdir secretDir

#Remove the "maliciousFiles" folder before continuing
rm -rf maliciousFiles

#Create file .secret inside "secretDir"
touch ./secretDir/.secret 

#Edit file permissions for .secret
chmod -R 600 ./secretDir/.secret

#Copying the content of .secret to README file
cat .secret >> /home/dan/linux/ex_linux1/DevOpsNov23/02_linux_ex1/README 
#what about the important link?? -5
#you need to run the generatesecret.sh -5
#Wubba
