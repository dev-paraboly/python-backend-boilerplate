#! /bin/bash
LATEST_PUBLISHED_VERSION=$(npm show @paraboly/{{cookiecutter.app_name}}_sdk version)
CURRENT_VERSION=$(node --eval='const json_file=require("./openapi.json");console.log(json_file.info.version);')
if [ "$LATEST_PUBLISHED_VERSION" = "$CURRENT_VERSION" ]; then
    echo "Not a new version, ignoring"
else
    echo "Definetely a new version"
    npm publish
fi