import os
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    # Ruta básica para probar que el servidor está vivo
    return "Servidor MCP en funcionamiento", 200

@app.route("/sse", methods=["POST"])
def mcp_sse():
    # Leer el JSON enviado por el cliente (ChatGPT u otro)
    data = request.get_json(silent=True) or {}

    # Respuesta mínima de prueba
    respuesta = {
        "ok": True,
        "mensaje": "Respuesta de ejemplo desde el servidor MCP (Render)",
        "eco": data
    }

    return jsonify(respuesta), 200

if __name__ == "__main__":
    # Render establece PORT en una variable de entorno
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
