from pydantic import BaseModel

class ClaseIris(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float
    species: str

class Insert(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float