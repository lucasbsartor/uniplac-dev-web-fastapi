from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class Employee(BaseModel):
    name: str
    cpf: str
    phone: str
    password: str
    registration: str
    group: str


@router.get('/employees', tags=["employees"])
async def get_employees():
    return {"msg": "Hello from get employees"}


@router.get('/employees/{id}', tags=["employees"])
async def get_employee(id: int):
    return {"msg": "Hello from get employee", "id": id}


@router.post('/employees', tags=["employees"])
async def create_employee(employee: Employee):
    return {"msg": "Hello from post employees", "employee": employee}


@router.put('/employees/{id}', tags=["employees"])
async def update_employee(id: int, employee: Employee):
    return {"msg": "Hello from put employees", "id": id, "employee": employee}


@router.delete('/employees/{id}', tags=["employees"])
async def get_employee(id: int):
    return {"msg": "Hello from delete employee", "id": id}
