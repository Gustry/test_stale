hub release create -m "Version $1" $1
qgis-plugin-ci release $1 --github-token $2 --create-plugin-repo