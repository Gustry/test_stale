#!/bin/sh

setup_git() {
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
}

commit_website_files() {
  git checkout master
  git add src/i18n/*.qm
  git commit --message "Update translations from Transifex version : $TRAVIS_TAG"
}

upload_files() {
  git remote add origin-push https://"${GH_TOKEN}"@github.com/"${TRAVIS_REPO_SLUG}".git > /dev/null 2>&1
  git push --quiet --set-upstream origin-push gh-pages
}

setup_git
commit_website_files
upload_files
