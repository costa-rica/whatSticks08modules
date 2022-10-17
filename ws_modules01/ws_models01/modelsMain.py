from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import relationship, backref, sessionmaker
from .modelsBase import Base, sess, engine
from .modelsApple import Apple_health_steps, Apple_health_export
from .modelsLocations import Locations, Weather_history, User_location_day
from .modelsOura import Oura_token, Oura_sleep_descriptions
from .modelsUsers import Users, Posts, Postshtml, Postshtmltagchars, User_notes
from ws_config01 import ConfigDev, ConfigProd

config = ConfigDev()


from flask_login import LoginManager

login_manager= LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


@login_manager.user_loader
def load_user(any_name_for_id_obj):# any_name_for_id_obj can be any name because its an arg that is the user id.
    # This is probably created somewhere inside flask_login when the user gets logged in. But i've not been able to track it.
    return sess.query(Users).filter_by(id = any_name_for_id_obj).first()


#Build db
if 'users' in inspect(engine).get_table_names():
    print('db already exists')
else:
    Base.metadata.create_all(engine)
    print('NEW db created.')



