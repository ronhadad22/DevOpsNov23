#!/bin/bash

# Step 1: Remove "maliciousFiles" directory if it exists
if [ -d maliciousFiles ]; then
    echo "Removing existing maliciousFiles directory..."
    rm -r maliciousFiles
fi

# Create a directory named "secretDir" (if it doesn't exist) and move into it
mkdir -p secretDir && cd secretDir || exit 1

# Step 2: Check if the ".secret" file already exists
if [ -e .secret ]; then
    # Display an error message and exit if the file exists
    echo "Error: .secret already exists. Aborting."
    exit 1
fi

# Step 3: Check if the file "CONTENT_TO_HASH" exists in the parent directory
if [ ! -e ../CONTENT_TO_HASH ]; then
    # Display an error message and exit if the file doesn't exist
    echo "Error: CONTENT_TO_HASH not found. Aborting."
    exit 1
fi

# Step 4: Create an empty file named ".secret"
# Step 5: Calculate the MD5 hash of the contents of "CONTENT_TO_HASH" and store it in ".secret"
touch .secret && echo "$(md5sum ../CONTENT_TO_HASH)" > .secret

# Step 6: Set the file permissions of ".secret" to read and write for the owner only
chmod 600 .secret

# Step 7: Display a success message
echo "Done! Your secret was stored in secretDir/.secret"