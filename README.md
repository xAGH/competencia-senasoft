# 1. Competenecia Siigo - BugFinder (Regional del Quindío)

El siguiente archivo busca documentar la estructura del proyecto, estableciendo los directorios del mismo y la arquitectura
que se empleará para el desarrollo de este.

## 1.1. Integrantes

- [Brian Castro](https://github.com/briancastro-bc)
- [John James Valencia](https://github.com/dunloop26)
- [Alejandro Giraldo](https://github.com/xAGH)

## 1.2. Estructura del proyecto (Project Tree)

~~~bash
|-competencia-senasoft
    |-application
        |-database
            -siigo_bugfinder.sql
        |-backend
            |-src
                |-blueprints
                    |-api
                        -api_blueprint.py
                        -api_controllers.py
                        -api_routes.py
                    -__init__.py
                |-controllers
                    -cards_controller.py
                    -public_controllers.py
                    -room_controllers.py
                    -users_controllers.py
                |-hooks
                    -verify_token.py
                |-namespaces
                    -__init__.py
                    -room_namespace.py
                |-services
                    -cards_service.py
                    -email_service.py
                    -game_service.py
                    -rooms_service.py
                    -users_service.py
                -app.py
                -database.py
                -models.py
                -room_structure.txt
                -routes.py
            -.env
            -.gitignore
            -main.py
        |-frontend
            |-src
                |-app
                    |-components
                        |-public
                        |-shared
                            |-card
                            |-spinner
                    |-interceptors
                    |-services
                    |-src
                |-assets
                    |-avatars
                    |-errors
                    |-modules
                    |-svg
                |-environments
    |-docs
    |-media
~~~

## 1.3. Lenguajes & Frameworks

- Backend: en el servidor se decide utilizar Python como lenguaje de programación y Flask como framework web.
- Frontend: en el lado del cliente se decide utilizar Typescript como lenguaje de programación y Angular como framework de Javascript/Typescript.

## 1.4. Modelamiento de datos

- En memoria (durante la ejecución):

~~~py
    rooms: dict[any] = {
        "room_code": {
            "players": [
                {
                    "sid": "abcdeasd-asdfase",
                    "cards":[4, 8, 5, 9],
                    "discovered_cards": [1, 6, 10, 11, 12, 15],
                    "score": 1/12 * 100,
                    "nickname": "Nickname",
                    "conected": True
                },
                {
                    "sid": "asdbahe-asdfase",
                    "cards":[4, 8, 5, 9],
                    "discovered_cards": [1, 6, 10, 11, 12, 15],
                    "score": 1/12 * 100,
                    "nickname": "Nickname",
                    "conected": True
                },
                {
                    "sid": "uyasejkhe-asdfase",
                    "cards":[4, 8, 5, 9],
                    "discovered_cards": [1, 6, 10, 11, 12, 15],
                    "score": 1/12 * 100,
                    "nickname": "Nickname",
                    "conected": True
                },
                {
                    "sid": "ueaheiasd-asdfase",
                    "cards":[4, 8, 5, 9],
                    "discovered_cards": [1, 6, 10, 11, 12, 15],
                    "score": 1/12 * 100,
                    "nickname": "Nickname",
                    "conected": True
                },
            ],
            "system": {
                "hidden_cards": [1,2,3],
                "isGameStarted": True,
                "current_turn": 1
            }
        }
    }
~~~

- Almacenamiento permanente (MySQL): ...
