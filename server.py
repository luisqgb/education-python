from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def inicio():
    return """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Mi servidor</title>
        <style>
            body {
                background: #111827;
                color: white;
                font-family: Arial, sans-serif;
                text-align: center;
                padding: 60px 20px;
            }
            h1 {
                color: #60a5fa;
            }
            .caja {
                background: #1f2937;
                padding: 25px;
                border-radius: 15px;
                max-width: 500px;
                margin: auto;
            }
        </style>
    </head>
    <body>
        <div class="caja">
            <h1>¡Servidor funcionando!</h1>
            <p>Mi servidor está ejecutándose en una máquina remota.</p>
            <p>Proyecto creado con Python y Flask.</p>
        </div>
    </body>
    </html>
    """

@app.route("/estado")
def estado():
    return {
        "servidor": "activo",
        "mensaje": "Todo funciona correctamente"
    }

if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto)
