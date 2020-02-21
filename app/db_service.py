import base64

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, BLOB, LargeBinary, BINARY
from .config import Config
from cryptography.fernet import Fernet

engine = create_engine(Config.SQLALCHEMY_DATABASE_URI, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

f = Fernet(Config.FERNET_KEY)


class Users(Base):
    __tablename__ = 'users'
    users_id = Column(Integer, primary_key=True)
    user_name = Column(String(80), unique=True, nullable=False)
    user_password = Column(Integer, unique=True, nullable=False)

    def __init__(self, name=None, password=None):
        self.user_name = name
        self.user_password = password

    def printInfo(self):
        decode_password = f.decrypt(self.user_password)
        return 'Info -> {} // {}'.format(self.user_name, decode_password.decode("utf-8"))


def init_db():
    Base.metadata.create_all(bind=engine)


def get_users():
    return Users.query.all()


def create_user(name=None, password=None):
    new_password = f.encrypt(password.encode())
    u = Users(name, new_password)
    db_session.add(u)
    db_session.commit()
