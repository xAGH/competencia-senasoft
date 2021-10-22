from src.controllers.public_controllers import *
from src.controllers.users_controllers import *
from src.controllers.room_controllers import *
from src.controllers.cards_controllers import *

public: dict[any] = {

}

users: dict[any] = {
    "login": "/users/login", "login_controller": UsersLoginController.as_view("signin"),
    "signup": "/users/signup", "signup_controller": UsersSignupController.as_view("signup"),
    "auth": "/users/auth/<uid>", "auth_controller": UsersAuthController.as_view("auth"),
}

cards: dict[any] = {
    "cards": "/cards", "cards_controller": CardsController.as_view("cards")
}

rooms: dict[any] = {
    "rooms_view": RoomController.as_view("room"),
    "create_room": "/create_room",
    "room": "/room"
}