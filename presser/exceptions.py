
class PresserError(Exception):
	pass

class PresserJavaScriptParseError(PresserError):
    pass

class PresserInvalidVineIdError(PresserError):
    pass

class PresserURLError(PresserError):
    pass

class Presser404Error(PresserError):
    pass

class PresserRequestError(PresserError):
    pass