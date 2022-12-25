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
git clone https://github.com/costa-rica/whatSticks08modules.git
```

<b><font size=4>Step 2</font></b>
Edit .env 


Found in whatSticks08modules/ws_modules01/ws_config01/ directory.

.env [what it will probably look like]
```
CONFIG_PATH="/home/nick/"
CONFIG_FILE_NAME="config_ws08_shared.json"
CONFIG_TYPE='dev'
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

* Note: req_ws08web.txt files use the ws-modules01 from git not the one you've just downloaded. To use the .env file you just endited in step 2, you'll need to either:

   - reinstall ws_modules01 with the one you've cloned and edited the .env by navigating into whatSticks08modules/ws_modules01/ws_config01/ 

         pip install -e .

  _<b>OR</b>_

  - edit/replace the .env file in your venv ws08web/src/ws-modules01/ws_modules01/ws_config01/.env with the one you edited in step 2.

:point_right: **Repeat for ws08api**

#
## What my file structure looks like on dev machine

This might be best for you if you want to make one directory to keep everything. The database gets big quickly with apple health data so if you want to put that somewhere else no problem just make sure the config.json file has the right WS_ROOT_DB

```
.
├── applications
│   ├── api
│   ├── apple_service
│   └── web
├── config_ws08_20221225.json
├── databases
│   └── ws08
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
