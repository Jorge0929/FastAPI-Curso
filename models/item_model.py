class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None