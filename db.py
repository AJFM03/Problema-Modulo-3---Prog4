from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Configuración de la conexión a MariaDB
# Ajusta usuario, contraseña, host, puerto y base de datos según tu instalación

DATABASE_URL = "mysql+pymysql://usuario:password@localhost:3306/biblioteca_db"

# Crear engine
engine = create_engine(DATABASE_URL, echo=True)

# Sesión de base de datos
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

# Base para modelos
Base = declarative_base()
