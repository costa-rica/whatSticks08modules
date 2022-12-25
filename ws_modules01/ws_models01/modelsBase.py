from sqlalchemy import create_engine, inspect
# from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
#     Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
# from datetime import datetime
from ws_config01 import ConfigDev, ConfigProd, ConfigLocal
# import json
import os

if os.environ.get('CONFIG_TYPE')=='local':
    config = ConfigLocal()
    print('* modelsBase: Development - Local')
elif os.environ.get('CONFIG_TYPE')=='dev':
    config = ConfigDev()
    print('* modelsBase: Development')
elif os.environ.get('CONFIG_TYPE')=='prod':
    config = ConfigProd()
    print('* modelsBase: Configured for Production')

########################################################
## Check/make key directories here becuase
## This is one of the first files to fire
if not os.path.exists(os.path.join(config.WS_ROOT_DB)):
    os.makedirs(os.path.join(config.WS_ROOT_DB))

if not os.path.exists(os.path.join(config.DB_DOWNLOADS)):
    os.makedirs(os.path.join(config.DB_DOWNLOADS))

if not os.path.exists(os.path.join(config.DF_FILES_DIR)):
    os.makedirs(os.path.join(config.DF_FILES_DIR))

if not os.path.exists(os.path.join(config.WORD_DOC_DIR)):
    os.makedirs(os.path.join(config.WORD_DOC_DIR))

if not os.path.exists(os.path.join(config.APPLE_HEALTH_DIR)):
    os.makedirs(os.path.join(config.APPLE_HEALTH_DIR))
##########################################################

Base = declarative_base()
engine = create_engine(config.SQL_URI, echo = False, connect_args={"check_same_thread": False})
Session = sessionmaker(bind = engine)
sess = Session()

#Build db
if 'users' in inspect(engine).get_table_names():
    print('db already exists')
else:
    Base.metadata.create_all(engine)
    print('NEW db created.')
