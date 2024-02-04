if test -d secretDir; then
   echo "Dir is exists"
else echo "Failed to generate secret. The directory 'secretDir' must exist before."
mkdir secretDir

fi

if test -d maliciousFiles; then
   echo "Failed to generate secret. The directory 'maliciousFiles' contains some malicious files... it must be removed before."
rm -rf maliciousFiles/
else echo "maliciousFiles has been removed"

fi

if test -f secretDir/.secret; then
   echo ".secret exists"
else echo "Failed to generate secret. The directory 'secretDir' must contain a file '.secret' in which the secret will be stored."

touch secretDir/.secret

fi

OCTAL_PERMISSIONS=$(stat -c "%a" secretDir/.secret)
if [ "$OCTAL_PERMISSIONS" = "600" ]; then
   echo "You have read and write permmissions only"
else echo "Failed to generate secret. The file 'secretDir/.secret' must have read and write permission only."
chmod 600 secretDir/.secret

fi

if [ -L 'important.link' ] && [ ! -e 'important.link' ]; then
  echo "Failed to generate secret. Secret can not be generated when broken file link exists. Please do something..."
  exit 1
else echo " important.link does not exists"
#you forget to unlink the file
fi


cat ./CONTENT_TO_HASH | xargs | md5sum > secretDir/.secret && echo "Done! Your secret was stored in secretDir/.secret"

#you need to run the generatesecret.sh from another script
