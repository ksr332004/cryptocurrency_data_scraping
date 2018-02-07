import json
from utils.logger import logger


class BadRequest(Exception):

    def __init__(self, message):
        error = dict()
        error['errorType'] = "BadRequest"
        error['httpStatus'] = 400
        error['message'] = message
        logger.warning(str(error))

        super(BadRequest, self).__init__(json.dumps(error))


class Unauthorized(Exception):

    def __init__(self, message):
        error = dict()
        error['errorType'] = "Unauthorized"
        error['httpStatus'] = 401
        error['message'] = message
        logger.error(str(error))
        super(Unauthorized, self).__init__(json.dumps(error))


class Forbidden(Exception):

    def __init__(self, message):
        error = dict()
        error['errorType'] = "Forbidden"
        error['httpStatus'] = 403
        error['message'] = message
        logger.error(str(error))
        super(Forbidden, self).__init__(json.dumps(error))


class ServiceUnavailable(Exception):

    def __init__(self, message):
        error = dict()
        error['errorType'] = "ServiceUnavailable"
        error['httpStatus'] = 503
        error['message'] = message
        logger.warning(str(error))
        super(ServiceUnavailable, self).__init__(json.dumps(error))