# dirPath = this file's directory path
dirPath="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"

# creating 'secretDir' directory
if [ ! -d "$dirPath/secretDir" ]; then
  echo "'secretDir' directory does not exist. Creating 'secretDir' directory."
  mkdir "$dirPath/secretDir"
else
  echo "'secretDir' directory found."
fi

# removing 'maliciousFiles' directory
if [ -d "$dirPath/maliciousFiles" ]; then
  echo "The directory 'maliciousFiles' contains some malicious files... Removing 'maliciousFiles' directory."
  rm -rf "$dirPath/maliciousFiles"
else
  echo "No malicious files found."
fi

# remove broken link
if [ -L "$dirPath/important.link" ] && [ ! -e "$dirPath/important.link" ]; then
  echo "Secret can not be generated when broken file link exists. Removing 'important.link'."
  rm "$dirPath/important.link"
else
  echo "No broken links found."
fi

# creating '.secret' file
if [ ! -f "$dirPath/secretDir/.secret" ]; then
  echo "The directory 'secretDir' must contain a file named '.secret' in which the secret will be stored."
  echo "Creating '/secret' file."
  touch "$dirPath/secretDir/.secret"
  else
  echo "'secretDir' directory found."
fi

# setting '.secret's permissions to 600
OCTAL_PERMISSIONS=$(stat -c "%a" "$dirPath/secretDir/.secret")
if [ "$OCTAL_PERMISSIONS" != "600" ]; then
  echo "The file 'secretDir/.secret' must have read and write permission only."
  echo "Changing it's permissions to 600."
  chmod 600 "$dirPath/secretDir/.secret"
else
  echo "'.secret' permissions verified."
fi

# generating the secret, and writing it into '.secret' file.
cat "$dirPath/CONTENT_TO_HASH" | xargs | md5sum > "$dirPath/secretDir/.secret"
echo "Done! Your secret was stored in secretDir/.secret"