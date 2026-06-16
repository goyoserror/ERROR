from flask import Flask, url_for, request, redirect, session

app = Flask(__name__)

app.secret_key = "clave_secreta_error_123"

USUARIO = "error"
CONTRASENA = "ACOELLOJucv.0"


@app.route("/")
def inicio():
    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>ERROR</title>
        <style>
            body {{
                margin: 0;
                background-image: url('{url_for("static", filename="imagen.png")}');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                height: 100vh;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 120px;
            }}

            h1 {{
                color: red;
                font-size: 90px;
                text-shadow: 3px 3px 8px black;
            }}

            .boton {{
                background-color: red;
                color: white;
                text-decoration: none;
                padding: 15px 40px;
                font-size: 22px;
                border-radius: 10px;
                box-shadow: 3px 3px 8px black;
            }}

            .boton:hover {{
                background-color: darkred;
            }}
        </style>
    </head>
    <body>
        <h1>ERROR</h1>
        <a class="boton" href="/login">Ingresar</a>
    </body>
    </html>
    """


@app.route("/login", methods=["GET", "POST"])
def login():
    mensaje = ""

    if request.method == "POST":
        usuario = request.form["usuario"]
        contrasena = request.form["contrasena"]

        if usuario == USUARIO and contrasena == CONTRASENA:
            session["usuario"] = usuario
            return redirect("/panel")
        else:
            mensaje = "Usuario o contraseña incorrectos"

    return f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login ERROR</title>
        <style>
            body {{
                margin: 0;
                background-image: url('{url_for("static", filename="imagen.png")}');
                background-size: cover;
                background-position: center;
                background-repeat: no-repeat;
                height: 100vh;
                color: white;
                font-family: Arial, sans-serif;
                display: flex;
                justify-content: center;
                align-items: center;
            }}

            .login-box {{
                background-color: rgba(0, 0, 0, 0.75);
                padding: 35px;
                border-radius: 15px;
                width: 320px;
                text-align: center;
                box-shadow: 0 0 15px black;
            }}

            h2 {{
                color: red;
                font-size: 40px;
                margin-bottom: 20px;
            }}

            input {{
                width: 90%;
                padding: 12px;
                margin: 10px 0;
                border: none;
                border-radius: 8px;
                font-size: 16px;
            }}

            button {{
                background-color: red;
                color: white;
                border: none;
                padding: 12px 35px;
                font-size: 18px;
                border-radius: 8px;
                cursor: pointer;
                margin-top: 10px;
            }}

            button:hover {{
                background-color: darkred;
            }}

            .error {{
                color: #ff5555;
                font-weight: bold;
            }}

            a {{
                color: white;
                display: block;
                margin-top: 15px;
            }}
        </style>
    </head>
    <body>
        <div class="login-box">
            <h2>ERROR</h2>

            <form method="POST">
                <input type="text" name="usuario" placeholder="Usuario" required>
                <input type="password" name="contrasena" placeholder="Contraseña" required>
                <button type="submit">Ingresar</button>
            </form>

            <p class="error">{mensaje}</p>

            <a href="/">Volver</a>
        </div>
    </body>
    </html>
    """


@app.route("/panel")
def panel():
    if "usuario" not in session:
        return redirect("/login")

    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Panel ERROR</title>
        <style>
            body {
                background-color: #111;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 100px;
            }

            h1 {
                color: red;
                font-size: 60px;
            }

            a {
                color: white;
                background-color: red;
                padding: 12px 25px;
                text-decoration: none;
                border-radius: 8px;
            }
        </style>
    </head>
    <body>
        <h1>Bienvenido al ERROR</h1>
        <p>Has ingresado correctamente.</p>
        <a href="/salir">Cerrar sesión</a>
    </body>
    </html>
    """


@app.route("/salir")
def salir():
    session.clear()
    return redirect("/")
