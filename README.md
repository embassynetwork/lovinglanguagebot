# About

A loving language bot to support experiments around language usage in slack. 

# Requirements

* developed with python 3.6. probably works with other versions of python 3+. 
  * to make a virtual env with a specific version of python: `mkvirtualenv --python=/usr/bin/python3.6 <name>`. Your python paths may vary.  
* `pip install -r requirements.txt`

# Setup

This bot requires the environment variables `LOVING_LANGUAGE_SLACK_TOKEN` and
`LOVING_LANGUAGE_BOT_ID` to be set. One way to reliably do this is to use a
virtual env (which is recommended regardless) and then symlink the postactivate
hook to a local version. Like so:

* create and activate your virtualenv (`mkvirtualenv <name>` and then `workon <name>`)
* in your loving language bot directory: `mkdir .env` 
  * --> this is in the `.gitignore` file so will not be committed. do NOT commit these values as this allows anyone to control your bot. 
* copy the file `postactivate.example` to the `.env` drectory and remove the `.example`, so that the file is just named `postactivate`. 
* edit the file to fill in the values of the environment variables, which you should get from an admin on your slack team. 
* make a symlink from the default postactivate hook to your custom one:
  `ln -s /path/to/repo/.env/postactivate $VIRTUAL_ENV/bin/postactivate`
  * this presumes that your postactivate hook is otherwise empty. if there are other things you have or want in there, then merge them with your local version. 

Make sure to add/invite your bot to any channels you want it to participate in. 

# Running

$ `workon <virtual env name>`

$ `./loving.py`

