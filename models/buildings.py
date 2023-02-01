from odmantic import Field, Model

class Buildings(Model):
    wood: int = Field(default=0, lt=3, ge=0)
    bean: int = Field(default=0, lt=3, ge=0)
    sugar: int = Field(default=0, lt=3, ge=0)
    biscket: int = Field(default=0, lt=3, ge=0)
    berry: int = Field(default=0, lt=3, ge=0)
    milk: int = Field(default=0, lt=3, ge=0)
    wool: int = Field(default=0, lt=3, ge=0)
    smithy: int = Field(default=0, lt=3, ge=0)
    jemstore: int = Field(default=0, lt=3, ge=0)
    workshop: int = Field(default=0, lt=3, ge=0)
    bakery: int = Field(default=0, lt=3, ge=0)
    restaurant: int = Field(default=0, lt=3, ge=0)
    pottery: int = Field(default=0, lt=3, ge=0)
    flowershop: int = Field(default=0, lt=3, ge=0)
    milkplant: int = Field(default=0, lt=3, ge=0)
    cafe: int = Field(default=0, lt=3, ge=0)
    dollshop: int = Field(default=0, lt=3, ge=0)
    oakplant: int = Field(default=0, lt=3, ge=0)
    patisserie: int = Field(default=0, lt=3, ge=0)
    jewelry: int = Field(default=0, lt=3, ge=0)
    

    # class Config:
    #     collection = "books"
