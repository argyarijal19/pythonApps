import re
from fastapi import APIRouter
from schemas.user_schemas import *
from repository.user_repo import *
from helper.response import *

auth = APIRouter(prefix="/user", tags=["AUTHENTICATION Detail"])


@auth.get("/")
async def get_data_all_user():
    data_user = get_user()
    if data_user:
        return success_get_data(data_user)

    return get_data_null("Tidak ada users yang terdaftar")


@auth.post("/register/")
async def register_user(user: Register):
    role_password = r"^(?=.*[A-Za-z])(?=.*\d)[A-Z][A-Za-z\d]{3,}$"
    if re.match(role_password, user.password) is not None:
        try:
            postData = create_user(user)
            if postData:
                return success_post_data(1, "Register Success")
            return post_data_fail("Create Accunt Gagal")
        except:
            post_data_fail("Create Account Gagal")
    else:
        return post_data_fail(
            "Password harus mengandung kombinasi angka dan huruf, harus diawali huruf besar, memiliki lebih dari 3 karakter")


@auth.post("/login/")
async def login_user(log: Login):
    data = login(log)
    if data["message"]:
        return get_data_null(data["message"])
    userInfo = {
        "username": data["username"],
        "id_user": data["id_user"],
        "nama_lengkap": data["nama_lengkap"]
    }
    return success_get_data(userInfo)
