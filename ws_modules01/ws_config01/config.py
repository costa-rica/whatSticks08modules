import os
import json
from dotenv import load_dotenv

load_dotenv()


with open(os.path.join(os.environ.get('CONFIG_PATH'), os.environ.get('CONFIG_FILE_NAME'))) as config_file:
    config = json.load(config_file)


class ConfigBasic():

    def __init__(self):
        self.SECRET_KEY = config.get('SECRET_KEY')

        #Email stuff
        self.MAIL_SERVER = config.get('MAIL_SERVER_MSOFFICE')
        self.MAIL_PORT = config.get('MAIL_PORT')
        self.MAIL_USE_TLS = True
        self.MAIL_USERNAME = config.get('EMAIL')
        self.MAIL_PASSWORD = config.get('EMAIL_PASSWORD')
        #web Guest
        self.GUEST_EMAIL = config.get('GUEST_EMAIL')
        self.GUEST_PASSWORD = config.get('GUEST_PASSWORD')

        self.WSH_API_PASSWORD = config.get('WSH_API_PASSWORD')

        #Location
        self.LOCATION_API_KEY = config.get('LOCATION_API_KEY')
        self.LOCATION_API_URL_BASE = config.get('LOCATION_API_URL_BASE')

        #Oura
        self.OURA_API_URL_BASE = config.get('OURA_API_URL_BASE')
        
        #Visual crossing - weather history
        self.VISUAL_CROSSING_TOKEN = config.get('VISUAL_CROSSING_TOKEN')
        self.VISUAL_CROSSING_BASE_URL = config.get('VISUAL_CROSSING_BASE_URL')
        self.DAYS_HIST_LIMIT_STD = 30

        #APPLE_HEALTH
        self.APPLE_HEALTH_CAT_NAMES = config.get('APPLE_HEALTH_CAT_NAMES')

        ############################################
        # Directory Paths
        self.WS_ROOT = os.environ.get('WS_ROOT')
        self.WS_ROOT_DB = os.environ.get('WS_ROOT_DB')

        #### Previously in child config classes ####
        # DB references 
        self.SQL_URI = f"sqlite:///{self.WS_ROOT_DB}ws08.db"

        #Blog
        self.WORD_DOC_DIR = f"{self.WS_ROOT_DB}word_docs"

        #DF for each data item
        self.DF_FILES_DIR = f"{self.WS_ROOT_DB}df_files"

        #Admin
        self.DB_DOWNLOADS = f"{self.WS_ROOT_DB}db_downloads"
        #Apple health
        self.APPLE_HEALTH_DIR = f"{self.WS_ROOT_DB}apple_health"

        #### Sub project directories ###
        self.APPLE_SUBPROCESS_DIR = f"{self.WS_ROOT}apple_service"
        self.SCHED_LOGS_DIR = f"{self.WS_ROOT}scheduler/"
        self.WEB_LOGS_DIR = f"{self.WS_ROOT}web/logs"
        self.API_LOGS_DIR = f"{self.WS_ROOT}api/logs"


class ConfigLocal(ConfigBasic):
    
    def __init__(self):
        super().__init__()

    DEBUG = True
    TEMPLATES_AUTO_RELOAD = False
    SCHED_CONFIG_STRING = "ConfigLocal"
    USERS_TESTING_OURA = True
    WSH_API_URL_BASE = config.get('WSH_API_URL_BASE_LOCAL')


class ConfigDev(ConfigBasic):

    def __init__(self):
        super().__init__()

    DEBUG = True
    SQL_URI = config.get('SQL_URI_DEVELOPMENT')
    TEMPLATES_AUTO_RELOAD = True
    SCHED_CONFIG_STRING = "ConfigDev"
    USERS_TESTING_OURA = False
    WSH_API_URL_BASE = config.get('WSH_API_URL_BASE_DEVELOPMENT')


class ConfigProd(ConfigBasic):
        
    def __init__(self):
        super().__init__()

    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
    SCHED_CONFIG_STRING = "ConfigProd"
    USERS_TESTING_OURA = False
    WSH_API_URL_BASE = config.get('WSH_API_URL_BASE_PRODUCTION')
