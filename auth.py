from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

from models import User
from database import db


# Register User
def register_user(username, email, password):

    existing_user = User.query.filter_by(
        email=email
    ).first()

    if existing_user:
        return {
            "status": False,
            "message": "Email already exists"
        }

    hashed_password = generate_password_hash(password)

    new_user = User(
        username=username,
        email=email,
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return {
        "status": True,
        "message": "User Registered Successfully"
    }


# Login User
def login_user(email, password):

    user = User.query.filter_by(
        email=email
    ).first()

    if not user:
        return {
            "status": False,
            "message": "User Not Found"
        }

    if check_password_hash(
        user.password,
        password
    ):
        return {
            "status": True,
            "message": "Login Successful"
        }

    return {
        "status": False,
        "message": "Invalid Credentials"
    }