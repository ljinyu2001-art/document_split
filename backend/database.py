from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base


# 修改这里
MYSQL_USER = "root"
MYSQL_PASSWORD = "123456"

# 虚拟机IP
MYSQL_HOST = "192.168.110.118"

MYSQL_PORT = "3306"

MYSQL_DB = "mysql"


DATABASE_URL = (
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}"
    f"@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)


engine = create_engine(
    DATABASE_URL,
    echo=True
)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


Base = declarative_base()



# 获取数据库连接

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()