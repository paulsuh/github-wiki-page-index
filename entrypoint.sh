#!/bin/sh

# Inputs from environment variables
#
# REPO_NAME: https URL used to clone the wiki
#
# AUTH_TOKEN: authentication token to allow content to be pushed
#
# USERNAME: Username for use with the AUTH_TOKEN
#
# USER_EMAIL: Email address of the user. Utilized as part of the commit action


# clone the wiki
cd /checkoutdir

git clone "https://${AUTH_TOKEN}@github.com/${REPO_NAME}.wiki.git"

ls

cd $(basename "${REPO_NAME}.wiki")

git config user.name "${USERNAME}"
git config user.email "${USER_EMAIL}"

# run the script to produce a new file list in Home.md
python /generate_wiki_file_index.py --insert "/checkoutdir/$(basename "${REPO_NAME}.wiki")"

# commit and push the change back to the repo
git add Home.md
git commit -m "Auto-generate wiki file list."
git push

