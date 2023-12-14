# Introdução ao uso Nuxt3 / FastAPI

### Tecnologias utilizadas
 - Python
 - FastAPI
 - Uvicorn
 - JWT
 - Nuxt3
 - Pinia
 - Tailwind
 - Bootstrap
 - Make

### Dados estáticos para login na aplicação Frontend
 - username -> Patricia
 - password -> password_patricia

 - username -> yasmin
 - password -> password_yasmin

## Para rodar a aplicação Backend
 - Acessar o diretorio backend e criar ambiente virtual.
 - ativar ambiente virtual
 - Instalar bibliotecas contidas no arquivo requirements.txt

```pip install -r requirements.txt```
 - Inicializar a aplicação

```make run```

### Rota index
```http://localhost:8000```

### Swagger
```http://localhost:8000/docs```

## Validação de usuário
Para validar um usuário, será preciso inserir alguns dados no header,
para autenticação, e receber um token como resposta.

 - username e password estão como: form-data
 - secret: JWT Bearer
 - Token: Bearer
No frontend, além destes passos, será preciso decodificar o token, onde terá
o username na resposta de autenticação.