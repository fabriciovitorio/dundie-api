from fastapi import APIRouter

from .user import router as user_router

main_router = APIRouter()
# paramentro redirect_slashes, default true, faz funcionar passando ou nao o / no final da url, se quiser tirar para forçar colocar a / para funcionar precisa colocar false   

main_router.include_router(user_router, prefix="/user", tags=["user"])
