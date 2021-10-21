class MessageFor():
    
    """Clase que provee los mensajes para los emails"""

    def confirmation_email(nickname: str, auth_token:str) -> str:
        """
        Método mensaje para email de confirmación.
            |- Parámetros -> self: object => Objeto instanciado que llama al método.
                             nickname: str => Nickname con el que se identifica el jugador.
                             auth_token: str => Token que contiene la informacion del jugador.
            |- Retorno -> str => Texto de mensaje en formato HTML;
            |- Función -> Envia un correo desde el email siigobugfinder@outlook.com con el mensaje, asunto y correo entregados
                          por parámetros.
        """

        return f"""<h1>Works {nickname}.\n<a href="http://localhost:4000/users/auth/{auth_token}">Confirm</a></h1>"""