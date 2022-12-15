import os
import json

machine = os.uname()[1]

match machine:
    case 'Nicks-Mac-mini.lan':
        # print('--- CASE thingy should fire ---')
        with open('/Users/nick/Documents/_config_files/config_ws08_20221215.json') as config_file:
            config = json.load(config_file)
    case 'devbig01' | 'speedy100':
        with open("/home/nick/config_ws08_20221215.json") as config_file:
            config = json.load(config_file)
    # case 'speedy100':
    #     with open("/home/nick/config_ws08_20221215.json") as config_file:
    #         config = json.load(config_file)
    case 'NICKSURFACEPRO4':
        with open(r"C:\Users\Costa Rica\Documents\_configs\config_ws20221215.json") as config_file:
            config = json.load(config_file)
        
# if os.environ.get('TERM_PROGRAM')=='Apple_Terminal':
#     with open('/Users/nick/Documents/_config_files/config_ws08_20221215.json') as config_file:
#         config = json.load(config_file)
# elif os.environ.get('COMPUTERNAME')=='NICKSURFACEPRO4':
#     with open(r"C:\Users\Costa Rica\Documents\_configs\config_ws20221215.json") as config_file:
#         config = json.load(config_file)
# else:
#     with open(r"/home/nick/config_ws08_20221215.json") as config_file:
#         config = json.load(config_file)


class ConfigBasic:
    SECRET_KEY = config.get('SECRET_KEY')
    BASIC_CONFIG_KEY = "This Key"

    #Email stuff
    MAIL_SERVER = config.get('MAIL_SERVER_MSOFFICE')
    MAIL_PORT = config.get('MAIL_PORT')
    MAIL_USE_TLS = True
    MAIL_USERNAME = config.get('EMAIL')
    MAIL_PASSWORD = config.get('EMAIL_PASSWORD')
    #web Guest
    GUEST_EMAIL = config.get('GUEST_EMAIL')
    GUEST_PASSWORD = config.get('GUEST_PASSWORD')

    WSH_API_PASSWORD = config.get('WSH_API_PASSWORD')
    #Location
    WEATHER_API_KEY = config.get('WEATHER_API_KEY')
    WEATHER_API_URL_BASE = config.get('WEATHER_API_URL_BASE')
    #Oura
    OURA_API_URL_BASE = config.get('OURA_API_URL_BASE')

    #Location
    WEATHER_API_KEY = config.get('WEATHER_API_KEY')
    WEATHER_API_URL_BASE = config.get('WEATHER_API_URL_BASE')
    
    #Visual crossing - weather history
    VISUAL_CROSSING_TOKEN = config.get('VISUAL_CROSSING_TOKEN')
    VISUAL_CROSSING_BASE_URL = config.get('VISUAL_CROSSING_BASE_URL')
    DAYS_HIST_LIMIT_STD = config.get('DAYS_HIST_LIMIT_STD')



class ConfigLocal(ConfigBasic):
    DEBUG = True
    SQL_URI = config.get('SQL_URI_LOCAL')
    TEMPLATES_AUTO_RELOAD = False

    WSH_API_URL_BASE = config.get('WSH_API_URL_BASE_LOCAL')

    #Blog
    WORD_DOC_DIR = config.get('WORD_DOC_DIR_LOCAL')
    # APPLE Health
    APPLE_HEALTH_DIR = config.get('APPLE_HEALTH_DIR_LOCAL')
    APPLE_SUBPROCESS_DIR = config.get('APPLE_SUBPROCESS_DIR_LOCAL')
    #DF for each data item
    DF_FILES_DIR = config.get('DF_FILES_DIR_LOCAL')
    #Admin
    DB_DOWNLOADS = config.get('DB_DOWNLOADS_LOCAL')



class ConfigDev(ConfigBasic):
    DEBUG = True
    SQL_URI = config.get('SQL_URI_DEVELOPMENT')
    TEMPLATES_AUTO_RELOAD = True

    #WSH API
    WSH_API_URL_BASE = config.get('WSH_API_URL_BASE_DEVELOPMENT')

    #Blog
    WORD_DOC_DIR = config.get('WORD_DOC_DIR')
    # APPLE Health
    APPLE_HEALTH_DIR = config.get('APPLE_HEALTH_DIR')
    APPLE_SUBPROCESS_DIR = config.get('APPLE_SUBPROCESS_DIR')
    #DF for each data item
    DF_FILES_DIR = config.get('DF_FILES_DIR')
    #Admin
    DB_DOWNLOADS = config.get('DB_DOWNLOADS')

class ConfigProd(ConfigBasic):
    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True

    SQL_URI = config.get('SQL_URI_PRODUCTION')
    WSH_API_URL_BASE = config.get('WSH_API_URL_BASE_PRODUCTION')
    #Blog
    WORD_DOC_DIR = config.get('WORD_DOC_DIR')
    # APPLE Health
    APPLE_HEALTH_DIR = config.get('APPLE_HEALTH_DIR')
    APPLE_SUBPROCESS_DIR = config.get('APPLE_SUBPROCESS_DIR')
    #DF for each data item
    DF_FILES_DIR = config.get('DF_FILES_DIR')
    #Admin
    DB_DOWNLOADS = config.get('DB_DOWNLOADS')