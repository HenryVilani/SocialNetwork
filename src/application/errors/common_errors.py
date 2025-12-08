
from src.application.errors.base_errors import BaseError


class InternalError(BaseError):

    def __init__(self):
        super().__init__("internal_error")

class BodyParserError(BaseError):

    def __init__(self):
        super().__init__("body_parser_error")

class MethodError(BaseError):

    def __init__(self):
        super().__init__("method_error")

class ParamParserError(BaseError):
    
    def __init__(self):
        super().__init__("param_parser_error")

class ValueParserError(BaseError):
    
    def __init__(self):
        super().__init__("value_parser_error")