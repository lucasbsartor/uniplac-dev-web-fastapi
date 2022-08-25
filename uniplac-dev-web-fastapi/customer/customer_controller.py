from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Customer(BaseModel):
    name: str
    cpf: str
    phone: str
    password: str
    registration: str
    group: str


@router.get('/customers', tags=["customers"])
async def get_customers():
    return {"msg": "Hello from get customers"}


@router.get('/customers/{id}', tags=["customers"])
async def get_customer(id: int):
    return {"msg": "Hello from get customer", "id": id}


@router.post('/customers', tags=["customers"])
async def create_customer(customer: Customer):
    return {"msg": "Hello from post customers", "customer": customer}


@router.put('/customers/{id}', tags=["customers"])
async def update_customer(id: int, customer: Customer):
    return {"msg": "Hello from put customers", "id": id, "customer": customer}


@router.delete('/customers/{id}', tags=["customers"])
async def get_customer(id: int):
    return {"msg": "Hello from delete customer", "id": id}
