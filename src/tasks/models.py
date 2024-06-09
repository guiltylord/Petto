from pydantic import BaseModel


# Request the main body order class model
class Order(BaseModel):
    customer_name: str
    order_quantity: int
