import boto3
from utils.utils import return_response, get_secret_hash, get_environ, logger_error, logger_info


def confirm_forgot(event):
    client = boto3.client('cognito-idp')

    try:

        response = client.confirm_forgot_password(
            ClientId=get_environ('client_id'),
            SecretHash=get_secret_hash(event['email']),
            Username=event['email'],
            ConfirmationCode=event['code'],
            Password=event['password']
        )
        logger_info(response)

        return return_response(200, 'Senha alterada com sucesso.', response)

    except client.exceptions.UserNotFoundException as e:
        logger_error(str(e))
        return return_response(404, 'Usuário inexistente.')

    except client.exceptions.ExpiredCodeException as e:
        logger_error(str(e))
        return return_response(422, 'Código de validação expirado.')

    except client.exceptions.UserNotConfirmedException as e:
        logger_error(str(e))
        return return_response(422, 'Usuário não confirmado.')

    except client.exceptions.InvalidPasswordException as e:
        logger_error(str(e))
        return return_response(422, 'A senha não atende aos requisitos mínimos.')

    except client.exceptions.CodeMismatchException as e:
        logger_error(str(e))
        return return_response(422, 'Código de validação inválido.')

    except Exception as e:
        logger_error(str(e))
        return return_response(500, "Ocorreu um erro, por favor, tente novamente.")
