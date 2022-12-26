import os
import json
from dotenv import load_dotenv

load_dotenv()

# SET config based on .env file 
# CONFIG_TYPE = os.getenv('CONFIG_TYPE')


with open(os.path.join(os.environ.get('CONFIG_PATH'), os.environ.get('CONFIG_FILE_NAME'))) as config_file:
    config = json.load(config_file)



class ConfigBasic():

    SECRET_KEY = config.get('SECRET_KEY')
    BASIC_CONFIG_KEY = "This Key"

    WS_ROOT = os.environ.get('WS_ROOT')
    WS_ROOT_DB = os.environ.get('WS_ROOT_DB')

    ############################################
    #### Previously in child config classes ####

    # DB references 
    SQL_URI = f"sqlite:///{WS_ROOT_DB}ws08.db"

    #Blog
    WORD_DOC_DIR = f"{WS_ROOT_DB}word_docs"

    #DF for each data item
    DF_FILES_DIR = f"{WS_ROOT_DB}df_files"

    #Admin
    DB_DOWNLOADS = f"{WS_ROOT_DB}db_downloads"
    #Apple health
    APPLE_HEALTH_DIR = f"{WS_ROOT_DB}apple_health"

    #### Sub project directories ###
    APPLE_SUBPROCESS_DIR = f"{WS_ROOT}apple_service"
    SCHED_LOGS_DIR = f"{WS_ROOT}scheduler/"
    WEB_LOGS_DIR = f"{WS_ROOT}web/logs"
    API_LOGS_DIR = f"{WS_ROOT}api/logs"

    ##############################################



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
    LOCATION_API_KEY = config.get('LOCATION_API_KEY')
    LOCATION_API_URL_BASE = config.get('LOCATION_API_URL_BASE')

    #Oura
    OURA_API_URL_BASE = config.get('OURA_API_URL_BASE')
    
    #Visual crossing - weather history
    VISUAL_CROSSING_TOKEN = config.get('VISUAL_CROSSING_TOKEN')
    VISUAL_CROSSING_BASE_URL = config.get('VISUAL_CROSSING_BASE_URL')
    DAYS_HIST_LIMIT_STD = 30

    #APPLE_HEALTH
    APPLE_HEALTH_CAT_NAMES = config.get('APPLE_HEALTH_CAT_NAMES')

    



class ConfigLocal(ConfigBasic):
    
    def __init__(self):
        super().__init__()

        self.DEBUG = True
        self.TEMPLATES_AUTO_RELOAD = False
        self.SCHED_CONFIG_STRING = "ConfigLocal"
        self.USERS_TESTING_OURA = True
        self.WSH_API_URL_BASE = config.get('WSH_API_URL_BASE_LOCAL')

        # ### DB references ###
        # self.SQL_URI = f"sqlite:///{self.WS_ROOT_DB}ws08.db"
        # self.WORD_DOC_DIR = f"{self.WS_ROOT_DB}word_docs"#Blog
        # self.DF_FILES_DIR = f"{self.WS_ROOT_DB}df_files"#DF for apple health, oura, weath, dash, etc.,
        # self.DB_DOWNLOADS = f"{self.WS_ROOT_DB}db_downloads"#Admin

        # #Apple health
        # self.APPLE_HEALTH_DIR = f"{self.WS_ROOT_DB}apple_health"

        # #### Sub project directories ###
        # self.APPLE_SUBPROCESS_DIR = f"{self.WS_ROOT}apple_service"
        # self.SCHED_LOGS_DIR = f"{self.WS_ROOT}scheduler/"
        # self.WEB_LOGS_DIR = f"{self.WS_ROOT}web/logs"
        # self.API_LOGS_DIR = f"{self.WS_ROOT}api/logs"


class ConfigDev(ConfigBasic):
    def __init__(self):
        super().__init__()
    DEBUG = True
    SQL_URI = config.get('SQL_URI_DEVELOPMENT')
    TEMPLATES_AUTO_RELOAD = True
    SCHED_CONFIG_STRING = "ConfigDev"
    USERS_TESTING_OURA = False
    WSH_API_URL_BASE = config.get('WSH_API_URL_BASE_DEVELOPMENT')

    # WS_ROOT_DB = config.get('WS_ROOT_DB')
    # WS_ROOT = config.get('WS_ROOT')

    # ### DB references ###
    # SQL_URI = f"sqlite:///{WS_ROOT_DB}ws08.db"

    # #Blog
    # WORD_DOC_DIR = f"{WS_ROOT_DB}word_docs"

    # #DF for each data item
    # DF_FILES_DIR = f"{WS_ROOT_DB}df_files"

    # #Admin
    # DB_DOWNLOADS = f"{WS_ROOT_DB}db_downloads"
    # #Apple health
    # APPLE_HEALTH_DIR = f"{WS_ROOT_DB}apple_health"

    # #### Sub project directories ###
    # APPLE_SUBPROCESS_DIR = f"{WS_ROOT}apple_service"
    # SCHED_LOGS_DIR = f"{WS_ROOT}scheduler/"
    # WEB_LOGS_DIR = f"{WS_ROOT}web/logs"
    # API_LOGS_DIR = f"{WS_ROOT}api/logs"



class ConfigProd(ConfigBasic):
    DEBUG = False
    TESTING = False
    PROPAGATE_EXCEPTIONS = True
    SCHED_CONFIG_STRING = "ConfigProd"
    USERS_TESTING_OURA = False
    WSH_API_URL_BASE = config.get('WSH_API_URL_BASE_PRODUCTION')


    # WS_ROOT_DB = config.get('WS_ROOT_DB')
    # WS_ROOT = config.get('WS_ROOT')

    # ### DB references ###
    # SQL_URI = f"sqlite:///{WS_ROOT_DB}ws08.db"

    # #Blog
    # WORD_DOC_DIR = f"{WS_ROOT_DB}word_docs"

    # #DF for each data item
    # DF_FILES_DIR = f"{WS_ROOT_DB}df_files"
    
    # DB_DOWNLOADS = f"{WS_ROOT_DB}db_downloads"#Admin
    # APPLE_HEALTH_DIR = f"{WS_ROOT_DB}apple_health"


    # #### Sub project directories ###
    # APPLE_SUBPROCESS_DIR = f"{WS_ROOT}apple_service"
    # SCHED_LOGS_DIR = f"{WS_ROOT}scheduler/"
    # WEB_LOGS_DIR = f"{WS_ROOT}web/logs"
    # API_LOGS_DIR = f"{WS_ROOT}api/logs"

