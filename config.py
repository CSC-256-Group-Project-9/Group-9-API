"""
Manage Database configuration settings

@author Anthony Epps
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

db = "postgresql://default:8jqOyM4wZvVH@ep-red-dust-14163675-pooler.us-east-1.postgres.vercel-storage.com:5432/verceldb"
#db = "postgresql://postgres:postgres@localhost:5432/group-9-api"
engine = create_engine(db)  
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
