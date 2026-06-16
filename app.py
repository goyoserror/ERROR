from flask import Flask, url_for

app = Flask(__name__)

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
                padding-top: 100px;
            }}

            h1 {{
                color: red;
                font-size: 70px;
                text-shadow: 3px 3px 8px black;
            }}

            p {{
                font-size: 24px;
                text-shadow: 2px 2px 5px black;
            }}

            button {{
                background-color: red;
                color: white;
                border: none;
                padding: 15px 30px;
                font-size: 18px;
                cursor: pointer;
                border-radius: 8px;
            }}

            button:hover {{
                background-color: darkred;
            }}
        </style>
    </head>
    <body>
        <h1>ERROR</h1>
        <p>Bienvenido a mi página web creada con Python.</p>
        <button onclick="alert('Página ERROR funcionando correctamente')">
            Presiona aquí
        </button>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)