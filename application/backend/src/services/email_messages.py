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
<center>
    <div 
style="padding: 0%;
       margin: 0%;
       width: 75%;
       height: 100%;
       border:1px solid rgba(0,0,0,0.25);
       padding: 24px;
       border-radius: 25px;
       font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;"
>
    <img style="width: 75%;
                float: left;
                margin-left: 16%;"
    src="https://alejo-imagenes-desde-flask.s3.amazonaws.com/game_logo.png" alt="Imagen">
    <br style="clear: both;">
    <center><h1 style="font-weight: 400;">Hola <strong>{nickname}</strong></h1> <h2 style="font-weight: 400; font-size:24px;"><br>¡Gracias por registrarte en SiigoBugFinder!</h2>
    <h2 style="font-weight: 400;">Para que tengas acceso a la <strong>tabla de puntuaciones</strong> y <strong>conservar tu nickname único</strong> <br><br><a
        style="color: white;
               padding: 10px;
               border-radius: 50px;
               background-color: rgb(10, 137, 255);
               font-style: none;
               text-decoration: none;
               font-size: 1.3rem;"
        href="http://localhost:4000/users/auth/{auth_token}">Confirma tu cuenta</a></h2>
    </center>
</div>

</center>
            """