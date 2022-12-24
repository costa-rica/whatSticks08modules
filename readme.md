# whatSticks08modules
<img src="https://github.com/costa-rica/whatSticks08/blob/github-main/web/app_package/static/images/wshLogo_300px_doodle02.png?raw=true" alt="what sticks logo" width="100"/>

Visit current working web at:
https://what-sticks.com

#
## Description

- This repo contains the config and database models for the whatSticks08 applications. In order to run whatSticks08 on your machine you'll need to add this module to your venv.
- Some hard coding is necessary in .env and config_ws08.json
- I will provide config_ws08.json
- Github repository for whatSticks08 found [here](https://github.com/costa-rica/whatSticks08)
#
## Installation


<b><font size=4>Step 1</font></b>
Download from Github
```
git install https://github.com/costa-rica/whatSticks08modules.git
```

<b><font size=4>Step 2</font></b>
Edit .env 

:point_right: __*IMPORTANT: edit .env before creating the venv*__


Found in whatSticks08modules/ws_modules01/ws_config01/ directory.

.env [what it will probably look like]
```
CONFIG_PATH="/Users/nick/Documents/_config_files"
CONFIG_FILE_NAME="config_ws08_20221222.json"
CONFIG_TYPE='local'
```
- CONFIG_PATH: enter path to the config file I will send you. This goes anywhere your local computer.
- CONFIG_FILE_NAME: probably config_ws08.json - or whatever you want to call it.
- CONFIG_TYPE: local for your machine. other options are 'dev' and 'prod'.

<b><font size=4>Step 3</font></b>
config json file

I will send a template (config_ws08.json) with everything preset. Here will be the key changes you'll need to make:

1. WS_ROOT_LOCAL: where the project file is (i.e. parent dir of run.py)
2. WS_ROOT_DB_LOCAL: location where database will be stored and other utility folders. Better not in app project folder. This will be what the SQL_URI reads

Note you can change WS_ROOT and WS_ROOT_DB to the same thing it won't matter if you are just running it on your machine.

<b><font size=4>Step 4</font></b>
Make ws08web and ws08api virtual environments
```
pyhton -m venv ws08web
source ws08web/bin/activate
```
<b><font size=4>Step 5</font></b>
Install packages from req_ws08web.txt and req_ws08api.txt files
```
pip install -r req_ws08web.txt
```
* Note: If there is a problem it might have to do with ws-modules01. In req_ws08web.txt file comment out the line starting with "-e git" like so "#-e git" or just remove. Then install manually by (while in ws08web venv) navigating to whatSticks08modules/ws_modules01/ws_config01/ 

        pip install -e .

  Make sure "ws-modules01" is in pip list


<b><font size=4>Step 6</font></b>
Make databases/ws08/ directory

ws08 can be anywhere, but it goes inside where ever you set the WS_ROOT_DB_LOCAL in your config.

<b><font size=4>Step 7</font></b>
Add appleHealthCatNames.txt in databases/ws08/apple_health/

appleHealthCatNames.txt
```
HKCategoryTypeIdentifier
HKDataType
HKQuantityTypeIdentifier
```
#
## More install info in case it helps

### config

This requires some hard coding in the .env and config_ws08.json file.
If you are contributing I will send a config_ws08.json for you to use with the keys to the various api's.

#### .env
```
CONFIG_PATH="/Users/nick/Documents/_config_files"
CONFIG_FILE_NAME="config_ws08_20221222.json"
CONFIG_TYPE='local'
```
- CONFIG_PATH: enter path to the config file I will send on your local computer
- CONFIG_FILE_NAME: probably config_ws08.json - or whatever you want to call it.
- CONFIG_TYPE: local for your machine. other options are 'dev' and 'prod'.



## What my file structure looks like on dev machine

This might be best for you if you want to make one directory to keep everything. The database gets big quickly with apple health data so if you want to put that somewhere else no problem just make sure the config.json file has the right WS_ROOT_DB

```
.
├── applications
│   ├── api
│   ├── apple_service
│   └── web
├── config_ws08_20221222.json
├── databases
│   └── ws08
│       ├── apple_health
│       │       └── appleHealthCatNames.txt [need to add manually]
│       ├── db_downloads
│       ├── df_files
│       └── ws08.db
├── environments
│   ├── whatSticks08modules
│   ├── ws08api
│   └── ws08web
└── whatSticks08
    ├── api
    ├── apple_service
    ├── scheduler
    └── web

```
