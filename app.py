import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# Ruta simple de prueba
@app.route("/", methods=["GET"])
def index():
    return "Servidor MCP en funcionamiento", 200

# Ruta que usará ChatGPT como MCP: /sse
@app.route("/sse", methods=["POST"])
def mcp_sse():
    # El cuerpo de la petición que envíe ChatGPT llegará como JSON
    data = request.get_json(silent=True) or {}

    # Aquí, en el futuro, tú interpretarías 'data' y llamarías a IIJ, SCJN, Scribd, etc.
    # Por ahora devolvemos una respuesta de ejemplo para probar que todo funciona.
    respuesta = {
        "ok": True,
        "mensaje": "Respuesta de ejemplo desde el servidor MCP",
        "eco": data
    }

    return jsonify(respuesta), 200

if __name__ == "__main__":
    # Railway asigna el puerto en la variable de entorno PORT
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
