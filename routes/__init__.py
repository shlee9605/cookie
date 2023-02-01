from fastapi import APIRouter

from routes import user
from routes import tree

router = APIRouter()

# router config
router.include_router(user.router)
router.include_router(tree.router)


