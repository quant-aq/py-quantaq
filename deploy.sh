# https://python-poetry.org/docs/cli/#version

# Tag the version
if [ -z "$1" ]
    then 
        echo "Deploy failed"
elif [ "$1" = "patch" ]
    then 
        poetry version patch
elif [ "$1" = "minor" ]
    then 
        poetry version minor
elif [ "$1" = "major" ]
    then
        poetry version major
elif [ "$1" = "premajor" ]
    then
        poetry version premajor
elif [ "$1" = "preminor" ]
    then
        poetry version preminor
elif [ "$1" = "prepatch" ]
    then
        poetry version prepatch
elif [ "$1" = "prerelease" ]
    then
        poetry version prerelease
else
    echo "Deploy failed."
fi

# Tag
VERSION=`poetry version`
VERSION_BITS=(${VERSION//  })
NEW_TAG=${VERSION_BITS[1]}

# commit the changes
git add -A
git commit -m "Pushing a new release candidate"
git push 

git tag $NEW_TAG
git push --tags
echo "Tagged and pushed to GitHub"