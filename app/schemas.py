from pydantic import BaseModel


class GugusData(BaseModel):
    nrp: str
    nama: str
    gugus: str
    region: str


class GugusSuccessResponse(BaseModel):
    success: bool = True
    message: str
    data: GugusData


class ErrorResponse(BaseModel):
    success: bool = False
    message: str
