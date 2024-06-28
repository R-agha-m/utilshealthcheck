from pydantic import BaseModel


class Regex(BaseModel):
    PHONE_NUMBER: str
    EMAIL: str
    LANDLINE: str
    NATIONAL_ID: str
    BASE64: str


class Dataset(BaseModel):
    WEBPAGE_ADDRESS: str


class User(BaseModel):
    SECRET_KEY: str
