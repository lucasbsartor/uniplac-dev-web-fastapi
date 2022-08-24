from fastapi import FastAPI

from customer import customer_controller
from employee import employee_controller

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

app.include_router(customer_controller.router)
app.include_router(employee_controller.router)
