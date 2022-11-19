import os
import json

if os.environ.get('TERM_PROGRAM')=='Apple_Terminal':
    with open('/Users/nick/Documents/_config_files/config_ws08_20221119.json') as config_file:
        config = json.load(config_file)
elif os.environ.get('COMPUTERNAME')=='NICKSURFACEPRO4':
    with open(r"C:\Users\Costa Rica\Documents\_configs\config_ws20221119.json") as config_file:
        config = json.load(config_file)
else:
    with open(r"/home/nick/config_ws08_20221119_ubuntu.json") as config_file:
        config = json.load(config_file)


class ConfigDev:
    DEBUG = True
    SECRET_KEY = config.get('SECRET_KEY')
    SQL_URI = config.get('SQL_URI')
    TEMPLATES_AUTO_RELOAD = True

    #Email stuff
    MAIL_SERVER = config.get('MAIL_SERVER_MSOFFICE')
    MAIL_PORT = config.get('MAIL_PORT')
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.get('EMAIL')
    MAIL_PASSWORD = config.get('EMAIL_PASSWORD')
    #web Guest
    GUEST_EMAIL = config.get('GUEST_EMAIL')
    GUEST_PASSWORD = config.get('GUEST_PASSWORD')
    #WSH API
    # WSH_API_URL_BASE = config.get('WSH_API_URL_BASE')
    WSH_API_URL_BASE = "http://localhost:5001"
    WS_API_URL_BASE_DEV = config.get('WS_API_URL_BASE_DEV')
    WSH_API_PASSWORD = config.get('WSH_API_PASSWORD')
    #Location
    WEATHER_API_KEY = config.get('WEATHER_API_KEY')
    WEATHER_API_URL_BASE = config.get('WEATHER_API_URL_BASE')
    #Oura
    OURA_API_URL_BASE = config.get('OURA_API_URL_BASE')

    #Visual crossing - weather history
    VISUAL_CROSSING_TOKEN = config.get('VISUAL_CROSSING_TOKEN')
    VISUAL_CROSSING_BASE_URL = config.get('VISUAL_CROSSING_BASE_URL')
    DAYS_HIST_LIMIT_STD = config.get('DAYS_HIST_LIMIT_STD')
    #Blog
    WORD_DOC_DIR = config.get('WORD_DOC_DIR')
    # APPLE Health
    APPLE_HEALTH_DIR = config.get('APPLE_HEALTH_DIR')
    APPLE_SUBPROCESS_DIR = config.get('APPLE_SUBPROCESS_DIR')
    #DF for each data item
    DF_FILES_DIR = config.get('DF_FILES_DIR')
    #Admin
    DB_DOWNLOADS = config.get('DB_DOWNLOADS')


class ConfigProd:
    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = config.get('SECRET_KEY')
    SQL_URI = config.get('SQL_URI')
    #Email stuff
    MAIL_SERVER = config.get('MAIL_SERVER_MSOFFICE')
    MAIL_PORT = config.get('MAIL_PORT')
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.get('EMAIL')
    MAIL_PASSWORD = config.get('EMAIL_PASSWORD')
    #web Guest
    GUEST_EMAIL = config.get('GUEST_EMAIL')
    GUEST_PASSWORD = config.get('GUEST_PASSWORD')
    #WSH API
    WSH_API_URL_BASE = config.get('WSH_API_URL_BASE')
    WS_API_URL_BASE_DEV = config.get('WS_API_URL_BASE_DEV')
    WSH_API_PASSWORD = config.get('WSH_API_PASSWORD')
    #Location
    WEATHER_API_KEY = config.get('WEATHER_API_KEY')
    WEATHER_API_URL_BASE = config.get('WEATHER_API_URL_BASE')
    #Oura
    OURA_API_URL_BASE = config.get('OURA_API_URL_BASE')
    #Visual crossing - weather history
    VISUAL_CROSSING_TOKEN = config.get('VISUAL_CROSSING_TOKEN')
    VISUAL_CROSSING_BASE_URL = config.get('VISUAL_CROSSING_BASE_URL')
    DAYS_HIST_LIMIT_STD = config.get('DAYS_HIST_LIMIT_STD')
    #Blog
    WORD_DOC_DIR = config.get('WORD_DOC_DIR')
    # APPLE Health
    APPLE_HEALTH_DIR = config.get('APPLE_HEALTH_DIR')
    APPLE_SUBPROCESS_DIR = config.get('APPLE_SUBPROCESS_DIR')
    #DF for each data item
    DF_FILES_DIR = config.get('DF_FILES_DIR')
    #Admin
    DB_DOWNLOADS = config.get('DB_DOWNLOADS')