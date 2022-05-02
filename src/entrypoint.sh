#!/bin/sh

# Inputs from environment variables
#
# REPO_NAME: name of the repository in the format <user name>/<repo name>
#
# AUTH_TOKEN: authentication token to allow content to be pushed
#
# USER_NAME: Username for use with the AUTH_TOKEN
#
# USER_EMAIL: Email address of the user. Utilized as part of the commit action

env

if [ -z "${REPO_NAME}" ]; then
  echo "REPO_NAME environment variable not set. Using the current repo GITHUB_REPOSITORY."
  REPO_NAME="${GITHUB_REPOSITORY}"
fi

# clone the wiki
cd /checkoutdir

git clone "https://${AUTH_TOKEN}@github.com/${REPO_NAME}.wiki.git"

echo "USER_NAME = ${USER_NAME}"
echo "USER_EMAIL = ${USER_EMAIL}"
echo "AUTH_TOKEN = ${AUTH_TOKEN}"

REPO_WIKI=$(basename "${REPO_NAME}")".wiki"

cd "${REPO_WIKI}"

git config user.name "${USER_NAME}"
git config user.email "${USER_EMAIL}"

# run the script to produce a new page index in Home.md
python /generate_wiki_page_index.py --insert "/checkoutdir/${REPO_WIKI}"

# commit and push the change back to the repo
git add Home.md
rm Home.md.old
git commit -m "Auto-generate wiki page index."
git push

