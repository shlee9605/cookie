from odmantic import Model, Field
from datetime import datetime
from typing import Optional

from models.products import Products
from models.buildings import Buildings
from models.technologies import Technologies

class Users(Model):
    user_id: str = Field(index=True, unique=True)
    pass_word: str
    year: int
    deletedAt: datetime = Field(default=None, nullable=True)
    products: Optional[Products]
    buildings: Optional[Buildings]
    technologies: Optional[Technologies]
    # products:  Products = Reference()
    # buildings: Buildings = Reference()
