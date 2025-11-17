"""
Configuración de la aplicación de Login Seguro
Implementa las mejores prácticas de seguridad según OWASP
"""
import os
from datetime import timedelta
from pathlib import Path

# Directorio base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent.parent


class Config:
    """Configuración principal de la aplicación"""
    
    # === CONFIGURACIÓN BÁSICA ===
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'
    
    # === BASE DE DATOS ===
    # SQLite local para simplicidad (en producción usar PostgreSQL/MySQL)
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL', 
        f'sqlite:///{BASE_DIR / "secure_login.db"}'
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = DEBUG
    
    # === SEGURIDAD DE SESIONES ===
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_KEY_PREFIX = 'session:'
    PERMANENT_SESSION_LIFETIME = timedelta(hours=24)
    
    # === COOKIES DE SEGURIDAD ===
    # IMPORTANTE: En producción con HTTPS, estas flags DEBEN estar activas
    SESSION_COOKIE_SECURE = False  # En producción: True (requiere HTTPS)
    SESSION_COOKIE_HTTPONLY = True  # Previene acceso desde JavaScript (XSS)
    SESSION_COOKIE_SAMESITE = 'Lax'  # Protección CSRF ('Strict' es más seguro)
    
    # === JWT TOKENS ===
    JWT_SECRET_KEY = SECRET_KEY
    JWT_ALGORITHM = 'RS256'  # Algoritmo asimétrico recomendado
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=15)  # Token de acceso corto
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=7)  # Token de refresco largo
    
    # Rutas para las claves RSA (se generarán automáticamente si no existen)
    JWT_PRIVATE_KEY_PATH = BASE_DIR / 'keys' / 'private_key.pem'
    JWT_PUBLIC_KEY_PATH = BASE_DIR / 'keys' / 'public_key.pem'
    
    # === ARGON2 CONFIGURATION (OWASP Recommendations) ===
    ARGON2_TIME_COST = 2  # Iteraciones
    ARGON2_MEMORY_COST = 19456  # KiB (19 MiB)
    ARGON2_PARALLELISM = 1  # Threads
    ARGON2_HASH_LENGTH = 32  # bytes
    ARGON2_SALT_LENGTH = 16  # bytes
    
    # === RATE LIMITING ===
    # Protección contra ataques de fuerza bruta
    RATELIMIT_STORAGE_URL = 'memory://'
    RATELIMIT_DEFAULT = "100 per hour"
    RATELIMIT_LOGIN = "5 per minute"  # Login más restrictivo
    RATELIMIT_REGISTER = "3 per hour"
    RATELIMIT_PASSWORD_RESET = "3 per hour"
    
    # === EMAIL CONFIGURATION (MOCK) ===
    # NOTA: En un entorno real, aquí iría la configuración del servicio de email
    # Servicios recomendados: SendGrid, AWS SES, Mailgun, SMTP de Google
    # Ejemplo con SendGrid:
    # EMAIL_PROVIDER = 'sendgrid'
    # SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')
    # FROM_EMAIL = 'noreply@tudominio.com'
    EMAIL_MOCK = True  # Si es True, los emails se imprimen en consola
    EMAIL_FROM = 'noreply@securelogin.local'
    EMAIL_VERIFICATION_TOKEN_EXPIRES = timedelta(hours=24)
    EMAIL_PASSWORD_RESET_TOKEN_EXPIRES = timedelta(hours=1)
    
    # === VALIDACIÓN DE CONTRASEÑAS ===
    PASSWORD_MIN_LENGTH = 8
    PASSWORD_REQUIRE_UPPERCASE = True
    PASSWORD_REQUIRE_LOWERCASE = True
    PASSWORD_REQUIRE_DIGITS = True
    PASSWORD_REQUIRE_SPECIAL = True
    
    # === AUDITORÍA Y LOGS ===
    AUDIT_LOG_FILE = BASE_DIR / 'logs' / 'audit.log'
    AUDIT_LOG_RETENTION_DAYS = 90  # GDPR/Privacidad: retención limitada
    
    # === CORS (si se necesita frontend separado) ===
    CORS_ORIGINS = os.getenv('CORS_ORIGINS', 'http://localhost:3000').split(',')
    
    # === POLITICAS DE PRIVACIDAD ===
    # Minimización de datos: solo almacenamos lo esencial
    COLLECT_USER_AGENT = True  # Para auditoría de sesiones
    COLLECT_IP_ADDRESS = True  # Para auditoría y rate limiting
    ANONYMIZE_LOGS_AFTER_DAYS = 90  # Anonimización automática de logs antiguos
    
    @staticmethod
    def init_app(app):
        """Inicialización adicional de la aplicación"""
        # Crear directorios necesarios
        (BASE_DIR / 'keys').mkdir(exist_ok=True)
        (BASE_DIR / 'logs').mkdir(exist_ok=True)
        (BASE_DIR / 'flask_session').mkdir(exist_ok=True)


class DevelopmentConfig(Config):
    """Configuración para desarrollo"""
    DEBUG = True
    SQLALCHEMY_ECHO = True


class ProductionConfig(Config):
    """Configuración para producción"""
    DEBUG = False
    
    # En producción, estas configuraciones DEBEN venir de variables de entorno
    SESSION_COOKIE_SECURE = True  # Requiere HTTPS
    SESSION_COOKIE_SAMESITE = 'Strict'  # Máxima protección CSRF
    
    # HTTPS/TLS Configuration (manejado por proxy reverso como nginx)
    # NOTA: El servidor Flask no maneja TLS directamente en producción
    # Se usa un proxy reverso (nginx/Apache) con certificados Let's Encrypt
    # Configuración ejemplo de nginx:
    # server {
    #     listen 443 ssl http2;
    #     ssl_certificate /etc/letsencrypt/live/tudominio.com/fullchain.pem;
    #     ssl_certificate_key /etc/letsencrypt/live/tudominio.com/privkey.pem;
    #     ssl_protocols TLSv1.2 TLSv1.3;
    # }
    PREFERRED_URL_SCHEME = 'https'


class TestingConfig(Config):
    """Configuración para tests"""
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    WTF_CSRF_ENABLED = False
    RATELIMIT_ENABLED = False


# Selección de configuración según entorno
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig
}


def get_config():
    """Obtiene la configuración según la variable de entorno"""
    env = os.getenv('FLASK_ENV', 'development')
    return config.get(env, config['default'])