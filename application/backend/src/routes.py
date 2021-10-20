from src.controllers.public_controllers import *
from src.controllers.users_controllers import *

public: dict[any] = {

}

users: dict[any] = {
    "login": "/users/login", "login_controller": UsersLoginController.as_view("signin"),
    "signup": "/users/signup", "signup_controller": UsersSignupController.as_view("signup"),
    "auth": "/users/auth/<id>", "auth_controller": UsersAuthController.as_view("auth"),
}