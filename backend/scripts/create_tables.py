import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app.core.database import engine, Base
from app.models.user import User  # Import all models

Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully!")
