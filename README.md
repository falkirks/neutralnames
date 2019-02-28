neutralnames
============

This is a tool for generating random gender neutral names using the lists on https://nonbinary.wiki. 


## Usage
```bash
$ pip install -r requirements.txt
$ python crawl.py       # downloads names to "names.txt"
$ python app.py         # serves a barebones app for getting names
$ python transform.py   # creates a lua module for mediawiki for a name generator
```

## Deploying to heroku
If you want to deploy to heroku, it is best to add the "buildpack-run" buildpack as it will allow the name list to be generated as part of the build. Or you could remove `names.txt` from the `.gitignore`.
```bash
$ heroku buildpacks:add https://github.com/weibeld/heroku-buildpack-run
```