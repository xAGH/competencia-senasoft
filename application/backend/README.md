# 1. Backend - BugFinder

En el siguiente documento se definirá la estructura del backend del proyecto. Se establecen los paquetes utilizados, entre otras cosas.

## 1.1. Paquetes & Herramientas

- [flask](https://flask.palletsprojects.com/en/2.0.x/)
- [flask_socketio](https://flask-socketio.readthedocs.io/)
- [flask_cors](https://flask-cors.readthedocs.io/en/latest/)
- [pyjwt](https://pyjwt.readthedocs.io/en/stable/)
- [pymysql](https://pypi.org/project/PyMySQL/)
  
## 1.2. Eventos de los sockets (Server)

RoomNamespace.on_connect() — se encarga de connectar nuevos usuarios.

RoomNamespace.on_message(data) — emite nuevos mensajes al cliente.
*Parameters:*
    - data: dict — donde se envía el código de la sala y un mensaje personalizado.

RoomNamespace.on_join(data) — une a un nuevo usuario a una sala dependiendo del código de la misma.
*Parameters:*
    - data: dict — donde se envía el código de la sala.

RoomNamespace.on_game_start(data) — toma el estado inicial del juego y comienza el mismo, validando la cantidad de usuarios que se encuentran en sala.
*Parameters:*
    - data: dict — donde se envía el código de la sala.

RoomNamespace.on_timeout(data) — emite un evento de finalización del tiempo en caso de que un usuario no responda a la pregunta, etc.
*Parameters:*
    - data: dict — donde se envía el código de la sala.

RoomNamespace.on_game_in_course() — en desarrollo...

RoomNamespace.on_make_question() — en desarrollo...

RoomNamespace.on_throw_accusation(data) — se emite el evento cuando el usuario elige la opción de acusar y valida la acusación del mismo.
*Parameters:*
    - data: dict — donde se envía el código de la sala y los datos de la acusación, es decir: dev_card, mod_card, error_card y player.

RoomNamespace.on_game_end(data) — se emite cuando el juego ha finalizado y cierra la sala que se creó.
*Parameters:*
    - data: dict — donde se envía el código de la sala.

RoomNamespace.on_leave(data) — se emite el evento cuando un usuario se sale de la sala.
*Parameters:*
    - data: dict — donde se envía el código de la sala y el nombre de usuario que se salió

RoomNamespace.on_disconnect() — se emite el evento en el momento que un usuario recarga la página o se sale del navegador.

## 1.3. Eventos de los sockets (Client)

- RoomNamespace.on_join():

    Socket.chat_message(message) — se emite cuando el servidor envía los mensajes del chat.

    Socket.room_not_found() — se emite cuando una sala no ha sido creada.

    Socket.room_full() — se emite el evento cuando la sala está llena.

    Socket.user_is_on_room() — se emite cuando un usuario que se encuentra en la sala intenta entrar desde otro lugar.

    Socket.user_joined() — se emite cuando un nuevo usuario entra a una sala creada.

- RoomNamespace.on_game_start():

    Socket.game_start() — se emite una vez el juego ha comenzado con los estados iniciales de las cartas.

    Socket.game_waiting() — se emite cuando la sala no tiene los usuarios necesarios.

- RoomNamespace.on_timeout():

    Socket.game_next_turn() — se emite cuando es necesario cambiar el turno del usuario.

- RoomNamespace.on_throw_accusation():

    Socket.user_win() — se emite cuando un usuario acierta la acusación.

    Socket.game_next_turn() — se emite cuando es necesario cambiar el turno del usuario.

- RoomNamespace.on_game_end():

    Socket.game_end() — se emite cuando el juego ha finalizado.

- RoomNamespace.on_leave():

    Socket.user_leave() — se emite cuando el usuario cierra una pestaña o se sale de la aplicación

### 1.3.1. Iniciando

1. Instalar paquetes necesarios para el proyecto, ubicándose en el directorio application/backend ejecuta el siguiente comando.

```bash
    pip install -r requirements.txt
```

2. Ejecutar el archivo en application/database/siigo_bugfinder.sql en un gestor de bases de datos MySql.
   2.1. Entrar al archivo en appilcation/backend/src/database.py y modificar la linea 10 cambiando el valor password y el user si es necesario es necesario.

3. Arrancar el servidor.

```bash
    python main.py 
```
