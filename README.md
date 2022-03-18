# fiap-hmv-lambda-forgot-password
[![Generic badge](https://img.shields.io/badge/Linguagem-Python-yellow.svg)](https://www.python.org/)
[![Generic badge](https://img.shields.io/badge/AWS-Lambda-orange.svg)](https://aws.amazon.com/pt/lambda/)

Projeto que expõe APIs para trocar a senha dos usuários no Cognito da aplicação do HMV. O serviço está exposto por um AWS Lambda.

Para instalar as dependências:
> pip install -r requirements.txt

### :exclamation: Atualizar o código no lambda
Execute o comando abaixo para gerar o **hmv-signup.zip** e depois faça o upload no lambda pelo console da AWS
> zip -r hmv-forgot-password.zip * -x ".git*" -x "README.md" -x coverage.xml -x "venv/*" -x ./package -x "tests/*" -x "test/*" -x Dockerfile -x docker-compose.yml -x ./examples -x functions.json
