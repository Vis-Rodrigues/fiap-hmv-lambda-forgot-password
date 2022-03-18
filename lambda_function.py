from hmv.forgot_password import forgot
from hmv.confirm_forgot_password import confirm_forgot
from utils.utils import get_body, logger_info


def lambda_handler(event, context):
    route = get_route(event)
    body = get_body(event['body'])

    if route == '/fiap-hmv/v1/login/forgot-password':
        return forgot(body)
    elif route == '/fiap-hmv/v1/login/confirm-forgot-password':
        return confirm_forgot(body)


def get_route(event):
    resource: str = event.get('resource', None)
    if not resource:
        raise BaseException('The resource key was not found in event.')

    logger_info('Resource: {}'.format(resource))

    return resource
