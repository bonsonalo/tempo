from pydantic import BaseModel, EmailStr,  field_validator, ConfigDict, Field
from typing import Optional
class User(BaseModel):
    """ Here I am dictating what dtype the variables should be """
    model_config= ConfigDict(strict=True) # to be strict in the dtype. ie it doesnt convert 7 into "7" just because we used str in the class model. We only use it when needed
    user: str=Field(min_length=1, max_length=10) # we use field to dictate what the the str should be. ge(greater or equal to), gt(greater than). we can also write the default and description in that
    email: EmailStr # EmailStr allows us to make sure the email is not just str but also an email containing @ sign 
    account_id: int
    salary: Optional[float] = None # optional with default value. It means if not given it will be None by default. but if float given it will take that
    is_active: Optional[bool] = True # the default is True, unless specified otherwise


# now lets say we only accept positive account_id value, so to do that we use validator decorator from pydantic

    @field_validator("account_id")
    def validate_account_id(cls, value):
        if value < 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value

user = User(user="jack", email="bonson@gmail.com", account_id=10)
print(user)

# user_json_str = user.model_dump_json() # TO CHANGE IT TO JSON,  WE CAN  use .model_dump_json().
# print(f"raw_parse(default): {user}")
# print(f"json format: {user_json_str}") 






