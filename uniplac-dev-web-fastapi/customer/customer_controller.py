from fastapi import APIRouter

router = APIRouter()


@router.get('/customers', tags=["customers"])
async def get_customers():
    return {"msg": "Hello from get customers"}


@router.get('/customers/{id}', tags=["customers"])
async def get_customer(id: int):
    return {"msg": "Hello from get customer"}


@router.post('/customers', tags=["customers"])
async def create_customer():
    return {"msg": "Hello from post customers"}


@router.put('/customers/{id}', tags=["customers"])
async def update_customer(id: int):
    return {"msg": "Hello from put customers"}
