from http import HTTPStatus

from werkzeug.exceptions import HTTPException

from src.com.gsk.qed import Constant

"""InvalidInputException can be used for any generic exception"""


class InvalidInputException(HTTPException):
    code = HTTPStatus.NOT_FOUND
    description = Constant.BAD_REQUEST
    name = 'InvalidInputException'
    response = None

    def __init__(self,  message, error_code, response=None):
        self.code = error_code
        self.description = message
        self.response = response


"""MetaException can be used if specific exception does not match"""

