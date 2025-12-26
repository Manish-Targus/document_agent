# Decompiled with PyLingual (https://pylingual.io)
# Internal filename: /home/anton/document_agent/server/models/user.py
# Bytecode version: 3.12.0rc2 (3531)
# Source timestamp: 2025-12-22 12:15:47 UTC (1766405747)

from typing import List, Optional
from sqlmodel import SQLModel, Field, Column
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy import String

class User(SQLModel, table=True):
    __tablename__ = 'users'
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(unique=True, index=True, nullable=False)
    name: str = Field(nullable=False)
    designation: Optional[str] = Field(default=None)
    keywords: List[str] = Field(sa_column=Column(ARRAY(String)))
    password: str = Field(nullable=False)

    class Config:
        arbitrary_types_allowed = True