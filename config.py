import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'uma_chave_secreta_padrao')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
