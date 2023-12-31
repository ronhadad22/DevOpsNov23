mkdir secretDir
cd maliciousFiles/
rm amIMaliciousOrNot.whoKnows
rm someFileIsLinkingToMe.BeAware
cd ..
rmdir maliciousFiles/
touch .secret
mv .secret secretDir/
cd secretDir
chmod 600 .secret