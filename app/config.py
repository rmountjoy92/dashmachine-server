class DefaultConfig:
    DEBUG = False
    TESTING = False
    JSON_SORT_KEYS = False


class DevelopmentConfig(DefaultConfig):
    ENV = "development"
    DEBUG = True
    TESTING = True


config = {"default": DefaultConfig, "development": DevelopmentConfig}
