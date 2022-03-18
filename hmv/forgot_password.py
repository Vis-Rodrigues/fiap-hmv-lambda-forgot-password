import boto3
from utils.utils import return_response, get_secret_hash, get_environ, logger_info, logger_error


def forgot(event):
    client = boto3.client('cognito-idp')

    try:
        response = client.forgot_password(
            ClientId=get_environ('client_id'),
            SecretHash=get_secret_hash(event['email']),
            Username=event['email']
        )

        logger_info(response)

        return return_response(200, 'Código para redefinir a senha enviado com sucesso.')

    except client.exceptions.UserNotFoundException as e:
        logger_error(str(e))
        return return_response(404, 'Usuário inexistente.')

    except client.exceptions.CodeDeliveryFailureException as e:
        logger_error(str(e))
        return return_response(422, 'Erro ao enviar código de verificação.')

    except client.exceptions.UserNotConfirmedException as e:
        logger_error(str(e))
        return return_response(422, 'Usuário ainda não confirmado.')

    except Exception as e:
        logger_error(str(e))
        return return_response(500, "Ocorreu um erro, por favor, tente novamente.")
