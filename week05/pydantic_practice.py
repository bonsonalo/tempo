from pydantic import BaseModel, EmailStr,  field_validator, ConfigDict

class User(BaseModel):
    """ Here I am dictating what dtype the variables should be """
    model_config= ConfigDict(strict=True) # to be strict in the dtype. ie it doesnt convert 7 into "7" just because we used str in the class model.
    user: str
    email: EmailStr # EmailStr allows us to make sure the email is not just str but also an email containing @ sign 
    account_id: int


# now lets say we only accept positive account_id value, so to do that we use validator decorator from pydantic

    @field_validator("account_id")
    def validate_account_id(cls, value):
        if value < 0:
            raise ValueError(f"account_id must be positive: {value}")
        return value

user = User(user="jack", email="bonson@gmail.com", account_id=10)

user_json_str = user.model_dump_json() # TO CHANGE IT TO JSON,  WE CAN  use .model_dump_json().
print(f"raw_parse(default): {user}")
print(f"json format: {user_json_str}") 


