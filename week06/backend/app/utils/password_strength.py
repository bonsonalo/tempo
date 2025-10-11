import re


def validate_password_strength(password: str) -> str:
    if not len(password) >= 8:
        raise ValueError("Password should be more than 8 character")
    if not re.search(r"[A-Z]", password):
        raise ValueError("password should atleast consist of 1 uppercase letter")
    if not re.search(r"[a-z]", password):
        raise ValueError("password should consist of smallcase letter")
    if not re.search(r"\d", password):
        raise ValueError("Password should contain atleast one number")
    if not re.search(r"[!@#$%^&*(){}/'.,]", password):
        raise ValueError("password should contain special character")
    return password