from odmantic import Model, Field, EmbeddedModel
from enum import Enum

class product_open(str, Enum):
    true = "O"
    false = "X"

class Product_Detail(EmbeddedModel):
    supplies: product_open = Field(default="X")
    demands: product_open = Field(default="X")

class Products(Model):
    wood: Product_Detail
    bean: Product_Detail
    sugar: Product_Detail
    biscuit: Product_Detail
    berry: Product_Detail
    milk: Product_Detail
    wool: Product_Detail
    axe: Product_Detail
    pickax: Product_Detail
    saw: Product_Detail
    shovel: Product_Detail
    pile: Product_Detail
    tongs: Product_Detail
    hammer: Product_Detail
    jellybean_jam: Product_Detail
    sweetjelly_jam: Product_Detail
    dalgona_jam: Product_Detail
    pomegranate_jam: Product_Detail
    tokberry_jam: Product_Detail
    birddoll: Product_Detail
    lamp: Product_Detail
    clock: Product_Detail
    dreamcatcher: Product_Detail
    ryebread: Product_Detail
    jampie: Product_Detail
    pocachia: Product_Detail
    donut: Product_Detail
    castella: Product_Detail
    croissant: Product_Detail
    jellystew: Product_Detail
    burger: Product_Detail
    pasta: Product_Detail
    omeletrice: Product_Detail
    pizzajelly: Product_Detail
    jellybean_meal: Product_Detail
    flower_pot: Product_Detail
    glass_plate: Product_Detail
    colored_marble: Product_Detail
    bowl: Product_Detail
    candy_flower: Product_Detail
    happy_flower: Product_Detail
    flower_bundle: Product_Detail
    flower_basket: Product_Detail
    bouquet: Product_Detail
    wreath: Product_Detail
    cream: Product_Detail
    butter: Product_Detail
    cheese: Product_Detail
    latte: Product_Detail
    bubbletea: Product_Detail
    ade: Product_Detail
    cushion: Product_Detail
    bearjelly_doll: Product_Detail
    dragonfruit_dool: Product_Detail
    root_beer: Product_Detail
    redberry_juice: Product_Detail
    wild_bottle: Product_Detail
    spooky_muffin: Product_Detail
    strawberry_cake: Product_Detail
    chiffon_cake: Product_Detail
    ring: Product_Detail
    brooch: Product_Detail
    crown: Product_Detail