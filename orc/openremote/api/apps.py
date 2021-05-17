from django.apps import AppConfig
import html
import pathlib
import os


class ApiConfig(AppConfig):
    predictor = None
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
