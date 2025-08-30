from fastapi import HTTPException


class UserNotFoundHttpException(HTTPException):
    def __init__(self):
        message = "user not found"
        super().__init__(status_code=400, detail=message)

class InternalServerErrorHttpException(HTTPException):
    def __init__(
        self,
        msg: str = "",
    ):
        if msg in [None, ""]:
            msg = "internal server error"
        super().__init__(status_code=500, detail=msg)