from sqlalchemy import create_engine, inspect
# from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
#     Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
# from datetime import datetime
from ws_config01 import ConfigDev, ConfigProd, ConfigLocal
# import json
import os


machine = os.uname()[1]

match machine:
    case 'Nicks-Mac-mini.lan' | 'NICKSURFACEPRO4':
        config = ConfigLocal()
    case 'devbig01':
        config = ConfigDev()
    case 'speedy100':
        config = ConfigProd()

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
