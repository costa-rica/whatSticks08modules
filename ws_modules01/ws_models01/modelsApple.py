# from colorama import Fore
from .modelsBase import Base
from sqlalchemy import Column, Integer, String, Text, Float, DateTime, ForeignKey, \
    Date
from datetime import datetime

class Apple_health_steps(Base):
    __tablename__ = 'apple_health_steps'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey("users.id"))
    date_time = Column(Text)
    steps_count = Column(Integer)
    time_stamp_utc = Column(DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f'Apple_health_steps(id: {self.id}, user_id: {self.user_id},' \
            f'date_time: {self.date_time}, steps_count: {self.steps_count})'
    