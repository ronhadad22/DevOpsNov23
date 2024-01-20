#!/bin/bash

# check if 'secretDir' dir is missing. then create the dir.
if [ ! -d "secretDir" ]; then
  mkdir secretDir
  echo "'secretDir' directory created!"
  else
  echo "'secretDir' directory is already exists..."
fi

# check if 'maliciousFiles' dir is exist. then delete the dir.
if [ -d "maliciousFiles" ]; then
  rm -r maliciousFiles
  echo "'maliciousFiles' directory and its files were deleted. We're safe to go."
  else
  echo "'maliciousFiles' directory is not here anymore..."
fi

# check if '.secret' file is missing. then create the file and change its permissions.
if [ ! -f "secretDir/.secret" ]; then
  touch './secretDir/.secret'
  chmod 600 './secretDir/.secret'
  echo "'.secret' file created!"
  echo "'.secret' file permissions were changed to 600."
  else
  echo "'.secret' file is already exists..."
fi

# practice file linking understanding
if [ -L 'important.link' ] && [ ! -e 'important.link' ]; then
rm important.link
echo "'important.link' was linked to a malicious file and therefore deleted."
else
  echo "'important.link' is not here anymore..."
fi

md5sum > secretDir/.secret & echo "Done! Your secret was stored in secretDir/.secret"
cat ./CONTENT_TO_HASH