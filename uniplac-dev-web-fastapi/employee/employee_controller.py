from fastapi import APIRouter

router = APIRouter()


@router.get('/employees', tags=["employees"])
async def get_employees():
    return {"msg": "Hello from get employees"}


@router.get('/employees/{id}', tags=["employees"])
async def get_employee(id: int):
    return {"msg": "Hello from get employee"}


@router.post('/employees', tags=["employees"])
async def create_employee():
    return {"msg": "Hello from post employees"}


@router.put('/employees/{id}', tags=["employees"])
async def update_employee(id: int):
    return {"msg": "Hello from put employees"}
