#!/usr/bin/env python3
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)

# Example: Create an engine and bind the metadata (optional for testing)
if __name__ == "__main__":
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)