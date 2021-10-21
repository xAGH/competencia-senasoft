class MessageFor():
    
    """Clase que provee los mensajes para los emails"""

    def confirmation_email(nickname: str, auth_token:str) -> str:
        """
        Método mensaje para email de confirmación.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
                             nickname: str => Nickname con el que se identifica el jugador.
                             auth_token: str => Token que contiene la informacion del jugador.
            |- Retorno -> str => Texto de mensaje en formato HTML;
            |- Función -> Genera un texto en estructura html.
        """

        return f"""
           <div 
            style="padding: 0%;
                margin: 0%;
                width: 100%;
                height: 100%;
                font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;">
                <center>
                    <h1>¡Hola {nickname}, gracias por registrarte en SiigoBugFinder!</h1>
                    <br><br><br>
                    <h2>Para que tengas acceso a la tabla de puntuaciones y conservar tu nickanme único, <br><br><br><a
                        style="color: white;
                            padding: 10px;
                            border-radius: 50px;
                            background-color: rgb(10, 137, 255);
                            font-style: none;
                            text-decoration: none;
                            font-size: 20px;"
                        href="http://localhost:4000/users/auth/{auth_token}">Confirma tu cuenta</a></h2>
                </center>
            </div>
            """