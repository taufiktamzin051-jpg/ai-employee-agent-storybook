```python
from sqlalchemy import create_engine
from src.models.db_models import Base

def init_db():
    engine = create_engine("postgresql://storybook_user:storybook_password@localhost:5432/storybook_db")
    Base.metadata.create_all(engine)
    print("✅ Database initialized")

if __name__ == "__main__":
    init_db()
```
