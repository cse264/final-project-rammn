git add *

git add -f ./config.json
git add -f ./RAMMN/static/*
git add -f ./RAMMN/templates/*

git commit -m "Deploying to heroku"

git push heroku master