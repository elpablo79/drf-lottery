from rest_framework.exceptions import APIException
from rest_framework import status


class ContestCodeMissingException(APIException):
    def __init__(self):
        ContestCodeMissingException.status_code = status.HTTP_400_BAD_REQUEST
        ContestCodeMissingException.detail = {
            "error": {
                "status": f'{status.HTTP_400_BAD_REQUEST}',
                "title": 'Contest code missing',
                "detail": f'Specify contest code parameter.'
            }
        }


class ContestNotFoundException(APIException):
    def __init__(self, contest_code):
        ContestNotFoundException.status_code = status.HTTP_404_NOT_FOUND
        ContestNotFoundException.detail = {
            "error": {
                "status": f'{status.HTTP_404_NOT_FOUND}',
                "title": 'Contest not found',
                "detail": f'Contest code {contest_code} not found.'
            }
        }


class ContestNotActiveException(APIException):
    def __init__(self, contest_code):
        ContestNotActiveException.status_code = status.HTTP_422_UNPROCESSABLE_ENTITY
        ContestNotActiveException.detail = {
            "error": {
                "status": f'{status.HTTP_422_UNPROCESSABLE_ENTITY}',
                "title": 'Contest is not active',
                "detail": f'The contest with code {contest_code} is not active.'
            }
        }

