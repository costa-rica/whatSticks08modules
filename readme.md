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

.env 
_(what my home working machine .env looks like)_
```
WS_ROOT = "/Users/nick/Documents/whatSticks08/"
WS_ROOT_DB = "/Users/nick/Documents/_databases/ws08/"
CONFIG_PATH="/Users/nick/Documents/_config"
CONFIG_FILE_NAME="config_ws08_20221226.json"
CONFIG_TYPE='local'
```
- WS_ROOT: root of project folder
- WS_ROOT_DB: root of project folder
- CONFIG_PATH: enter path to the config file I will send you. This goes anywhere your local computer.
- CONFIG_FILE_NAME: probably config_ws08.json - or whatever you want to call it.
- CONFIG_TYPE: local for your machine. other options are 'dev' and 'prod'.

:point_right: See folder structure below for additional clarity

<b><font size=4>Step 3</font></b>

Make ws08web and ws08api virtual environments
```
pyhton -m venv ws08web
source ws08web/bin/activate
```
<b><font size=4>Step 4</font></b>
Install packages from req_ws08web.txt and req_ws08api.txt files
```
pip install -r req_ws08web.txt
```

* Note: req_ws08web.txt files use the ws-modules01 from git not the one you've just downloaded. To use the .env file you just endited in step 2, you'll need to either:

   - reinstall ws_modules01 with the one you've cloned (and edited the .env) by navigating into whatSticks08modules/ws_modules01/ws_config01/ 

         pip install -e .

  _<b>OR</b>_

  - edit/replace the .env file in your venv ws08web/src/ws-modules01/ws_modules01/ws_config01/.env with the one you edited in step 2.

:point_right: **Repeat for ws08api**

#
## file structure
This folder structure is from the development server, dedicated to running What Sticks. Depending on my updates the .env file you get from here might not reflect this exactly becuase I've named things differently on my home working computer.

<u>.env mappings as they reflect folder structure below:</u>
- "." -> CONFIG_PATH
- "applications" -> WS_ROOT
- "databases" -> WS_ROOT_DB

```
.                         <------ CONFIG_PATH
├── applications          <------ WS_ROOT
│   ├── api
│   ├── apple_service
│   └── web
├── databases             <------ WS_ROOT_DB
│   └── ws08
│       ├── db_downloads
│       ├── df_files
│       └── ws08.db
├── environments
│   ├── whatSticks08modules
│   ├── ws08api
│   └── ws08web
└── config_ws08_20221225.json
```
