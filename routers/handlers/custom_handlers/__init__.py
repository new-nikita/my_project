from aiogram import Router


from .rating import rating_router
from .high import highprice_router
from .low import lowprise_router
from .range_price import range_price_router
from .history import help_router

router = Router(name=__name__)

router.include_router(rating_router)
router.include_router(highprice_router)
router.include_router(lowprise_router)
router.include_router(range_price_router)
router.include_router(help_router)