from pydantic import BaseModel


class Links(BaseModel):
    id: int
    link: str
    link_name: str
    # link_identity: str

    class Config:
        orm_mode = True
