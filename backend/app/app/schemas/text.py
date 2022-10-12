from pydantic import BaseModel
from typing import List

class Text(BaseModel):
    sentences: List[str]