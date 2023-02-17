from fastapi import APIRouter, HTTPException
from services import tree_service
from models.technologies import Technologies
from models.buildings import Buildings
from models.products import Products

router = APIRouter()

# edit user's technologies info
@router.put("/kingdom/tree/technologies")
async def building_root(request: Technologies, param: str):
    # 1. Check Request
    try:
        params = Technologies(
            clocktower=request.clocktower,
            mataccel1=request.mataccel1,
            prodaccel1=request.prodaccel1,
            mataccel2=request.mataccel2,
            prodaccel2=request.prodaccel2,
            wood=request.wood,
            bean=request.bean,
            sugar=request.sugar,
            biscuit=request.biscuit,
            berry=request.berry,
            milk=request.milk,
            wool=request.wool,
            smithy=request.smithy,
            jemstore=request.jemstore,
            workshop=request.workshop,
            bakery=request.bakery,
            restaurant=request.restaurant,
            pottery=request.pottery,
            flowershop=request.flowershop,
            milkplant=request.milkplant,
            dollshop=request.dollshop,
            oakplant=request.oakplant,
            patisserie=request.patisserie,
            jewelry=request.jewelry
        )
        params = {'user_id': param, 'technologies': params}
    except:
        raise HTTPException(status_code=400, detail="Bad Request")

    # 2. Execute Bussiness Logic
    response = await tree_service.edit_technology(params)

    # 3. Response
    return response

# edit user's building info
@router.put("/kingdom/tree/buildings")
async def building_root(request: Buildings, param: str):
    # 1. Check Request
    try:
        params = Buildings(
            wood=request.wood,
            bean=request.bean,
            sugar=request.sugar,
            biscuit=request.biscuit,
            berry=request.berry,
            milk=request.milk,
            wool=request.wool,
            smithy=request.smithy,
            jemstore=request.jemstore,
            workshop=request.workshop,
            bakery=request.bakery,
            restaurant=request.restaurant,
            pottery=request.pottery,
            flowershop=request.flowershop,
            milkplant=request.milkplant,
            dollshop=request.dollshop,
            oakplant=request.oakplant,
            patisserie=request.patisserie,
            jewelry=request.jewelry
        )
        params = {'user_id': param, 'buildings': params}
    except:
        raise HTTPException(status_code=400, detail="Bad Request")

    # 2. Execute Bussiness Logic
    response = await tree_service.edit_building(params)

    # 3. Response
    return response

# edit user's product info
@router.put("/kingdom/tree/products")
async def product_root(request: Products, param: str):
    # 1. Check Request
    try: 
        params = Products(
            wood=request.wood,
            bean=request.bean,
            sugar=request.sugar,
            biscuit=request.biscuit,
            berry=request.berry,
            milk=request.milk,
            wool=request.wool,
            axe=request.axe,
            pickax=request.pickax,
            saw=request.saw,
            shovel=request.shovel,
            tongs=request.tongs,
            hammer=request.hammer,
            jellybean_jam=request.jellybean_jam,
            sweetjelly_jam=request.sweetjelly_jam,
            dalgona_jam=request.dalgona_jam,
            pomegranate_jam=request.pomegranate_jam,
            tokberry_jam=request.tokberry_jam,
            birddoll=request.birddoll,
            lamp=request.lamp,
            clock=request.clock,
            dreamcatcher=request.dreamcatcher,
            ryebread=request.ryebread,
            jampie=request.jampie,
            pocachia=request.pocachia,
            donut=request.donut,
            castella=request.castella, 
            croissant=request.croissant,
            jellystew=request.jellystew,
            burger=request.burger,
            pasta=request.pasta,
            omeletrice=request.omeletrice,
            pizzajelly=request.pizzajelly,
            jellybean_meal=request.jellybean_meal,
            flower_pot=request.flower_pot,
            glass_plate=request.glass_plate,
            colored_marble=request.colored_marble,
            bowl=request.bowl,
            candy_flower=request.candy_flower,
            happy_flower=request.happy_flower,
            flower_bundle=request.flower_bundle,
            flower_basket=request.flower_basket,
            bouquet=request.bouquet,
            wreath=request.wreath,
            cream=request.cream,
            butter=request.butter,
            cheese=request.cheese,
            latte=request.latte,
            bubbletea=request.bubbletea,
            ade=request.ade,
            cushion=request.cushion,
            bearjelly_doll=request.bearjelly_doll,
            dragonfruit_dool=request.dragonfruit_dool,
            root_beer=request.root_beer,
            redberry_juice=request.redberry_juice,
            wild_bottle=request.wild_bottle,
            spooky_muffin=request.spooky_muffin,
            strawberry_cake=request.strawberry_cake,
            chiffon_cake=request.chiffon_cake,
            ring=request.ring,
            brooch=request.brooch,
            crown=request.crown
        )
        params = {'user_id': param, 'products': params}
    except:
        raise HTTPException(status_code=400, detail="Bad Request")

    # 2. Execute Bussiness Logic
    response = await tree_service.edit_product(params)

    # 3. Response
    return response
