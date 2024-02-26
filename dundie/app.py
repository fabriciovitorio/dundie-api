#uvicorn dundie.app:app --reload

from fastapi import FastAPI
from .routes import main_router


app = FastAPI(
    title="dundie",
    version="0.1.0",
    description="dundie is a rewards API",
)

app.include_router(main_router)

######### Codigo usado sem a ingestao de dependencia
# from dundie.db import engine
# from dundie.models import User
# from sqlmodel import Session, select
# from dundie.models.user import UserResponse

# @app.get("/", response = UserResponse)
# def hello():
#     with Session(engine) as session:
#         return session.exec(select(User)).first()

######### Codigo usado a ingestao de dependencia. Desta forma o codigo do exec do session vai ser executado dentro do db na funcao get_session, entao toda view ja tem o engine para acessar o banco

# from dundie.db import ActiveSession
# from dundie.models import User
# from sqlmodel import Session, select
# from dundie.models.user import UserResponse

# @app.get("/", response = UserResponse)
# def hello(session: Session = ActiveSession):
#     return session.exec(select(User)).first()
