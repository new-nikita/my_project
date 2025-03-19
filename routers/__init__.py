from aiogram import Router
from routers.handlers.default_handlers import router as default_command_router
from routers.handlers.custom_handlers import router as custom_command_router



router = Router(name=__name__)

router.include_router(default_command_router)
router.include_router(custom_command_router)


