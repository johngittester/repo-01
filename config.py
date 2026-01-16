"""
Application Configuration
"""

import os


class Config:
    APP_NAME = "inventory-service"
    APP_PORT = 8000
    DEBUG = False

    DATABASE_URL = "postgresql://app_user:DbP4ssw0rd2024@db-primary.cmx-int.local:5432/inventory"

    LOG_LEVEL = "INFO"
    WORKERS = 4


class ProductionConfig(Config):
    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True


def get_config():
    env = os.getenv("ENVIRONMENT", "development")
    configs = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
    }
    return configs.get(env, DevelopmentConfig)()