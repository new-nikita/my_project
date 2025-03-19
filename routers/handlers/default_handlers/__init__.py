from aiogram import Router

from .start import start_router
from .help import help_router


router = Router(name=__name__)

router.include_router(start_router)
router.include_router(help_router)
