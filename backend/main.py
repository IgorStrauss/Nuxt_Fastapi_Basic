from datetime import datetime, timedelta
from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt

app = FastAPI()

SECRET_KEY = "secret_key_jwt_test"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

origins = [
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def create_jwt_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username


@app.post("/token")
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(form_data.username, form_data.password)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    # Crie um token JWT válido para o usuário autenticado
    token_data = {"sub": user["name"]}
    token = create_jwt_token(token_data)

    return {"access_token": token, "token_type": "bearer"}


def authenticate_user(username: str, password: str):
    for user in users:
        if user["name"] == username and user.get("password") == password:
            return user
    return None


# Lista estática de usuários(mock)
users = [
    {
        "id": 1,
        "name": "Patricia",
        "password": "password_patricia",
        "email": "patricia@email.com",
    },
    {
        "id": 2,
        "name": "yasmin",
        "password": "password_yasmin",
        "email": "yasmin@email.com",
    },
    {
        "id": 3,
        "name": "Victoria",
        "password": "password_victoria",
        "email": "victoria@email.com",
    },
    {
        "id": 4,
        "name": "Natalia",
        "password": "password_natalia",
        "email": "natalia@email.com",
    },
    {
        "id": 5,
        "name": "Bruna",
        "password": "password_bruna",
        "email": "bruna@email.com",
    },
]


@app.get("/")
def index():
    return {"message": "Igor Marques - Teste de API com FastAPI e JWT"}


# Rota protegida por autenticação JWT
@app.get("/api/users", response_model=List[dict])
def list_users(current_user: str = Depends(get_current_user)):
    return users


# Rota protegida por autenticação JWT
@app.get("/api/users/{user_id}", response_model=dict)
def detail_user(user_id: int, current_user: str = Depends(get_current_user)):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found with that ID")
