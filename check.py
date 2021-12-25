from models.base_model import BaseModel


new = BaseModel()
print(new.created_at)
print(new.updated_at)
print(new.__dict__)