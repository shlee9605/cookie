from odmantic import Model, Field
from typing import Optional

from models.products import Products
from models.buildings import Buildings

class Users(Model):
    user_id: str = Field(index=True, unique=True)
    products: Optional[Products]
    buildings: Optional[Buildings]