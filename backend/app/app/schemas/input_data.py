from pydantic import BaseModel

class InputData(BaseModel):
    bed: int
    bath: int
    acre_lot: float
    city: str
    state: str
    zip_code: int
    house_size: float