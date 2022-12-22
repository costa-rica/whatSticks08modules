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
# print('Are we in modelsBase?')
# if os.uname()[1] == 'Nicks-Mac-mini.lan' or os.uname()[1] == 'NICKSURFACEPRO4':
#     print('--- CASE thingy should fire ---')
#     config = ConfigLocal()
# elif 'dev' in os.uname()[1]:
#     print('** This should fire ****')
#     config = ConfigDev()
# elif 'prod' in os.uname()[1] or os.uname()[1] == 'speedy100':
#     config = ConfigProd()
# machine = os.uname()[1]

# match machine:
#     case 'Nicks-Mac-mini.lan' | 'NICKSURFACEPRO4':
#         config = ConfigLocal()
#     case 'devbig01':
#         config = ConfigDev()
#     case 'speedy100':
#         config = ConfigProd()

Base = declarative_base()
engine = create_engine(config.SQL_URI, echo = False, connect_args={"check_same_thread": False})
Session = sessionmaker(bind = engine)
sess = Session()

# #Build db
# if 'users' in inspect(engine).get_table_names():
#     print('db already exists')
# else:
#     Base.metadata.create_all(engine)
#     print('NEW db created.')
