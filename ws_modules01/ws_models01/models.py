from sqlalchemy import create_engine, inspect
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from datetime import datetime
from ws_config01 import ConfigDev, ConfigProd, ConfigLocal
from flask_login import UserMixin, LoginManager
import json
import os


print('******* -- ws_models01 models.py --')
