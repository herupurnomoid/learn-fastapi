from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Database URL - you can set this as an environment variable
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://heru:Heru123.@localhost/mydatabase")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a configured "Session" class
session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

