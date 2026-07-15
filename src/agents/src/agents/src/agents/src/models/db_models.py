```python
from sqlalchemy import Column, String, Integer, Float, DateTime, Boolean, Text, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    email = Column(String, unique=True)
    age_group = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

class Story(Base):
    __tablename__ = "stories"
    id = Column(String, primary_key=True)
    title = Column(String)
    content = Column(Text)
    age_group = Column(String)
    quality_score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class UserEngagement(Base):
    __tablename__ = "user_engagement"
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))
    story_id = Column(String, ForeignKey("stories.id"))
    completed = Column(Boolean)
    rating = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)

class Recommendation(Base):
    __tablename__ = "recommendations"
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))
    story_id = Column(String, ForeignKey("stories.id"))
    score = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)

class Subscription(Base):
    __tablename__ = "subscriptions"
    id = Column(String, primary_key=True)
    user_id = Column(String, ForeignKey("users.id"))
    plan_type = Column(String)
    status = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
```
