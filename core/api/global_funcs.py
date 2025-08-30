from functools import wraps
import logging
from fastapi import HTTPException
from .api_exceptions import InternalServerErrorHttpException



logger = logging.getLogger(__name__)

def exception_handler(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except HTTPException as e:
            logger.error(f"Произошла ошибка в эндпоинте {func.__name__}: {e}", exc_info=True)
            raise e
        except Exception as e:
            logger.error(f"Произошла ошибка в эндпоинте {func.__name__}: {e}", exc_info=True)
            raise InternalServerErrorHttpException(msg=str(e))

    return wrapper