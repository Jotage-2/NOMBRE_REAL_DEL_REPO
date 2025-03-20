from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# Saldo aleatorio
saldo = random.randrange(10, 5000)

@app.route("/")
def index():
    return render_template("index.html", saldo=saldo)

@app.route("/consultar", methods=["GET"])
def consultar():
    global saldo
    return jsonify({"saldo": saldo})

@app.route("/retirar", methods=["POST"])
def retirar():
    global saldo
    retiro = float(request.json.get("retiro", 0))
    
    if saldo >= retiro:
        saldo -= retiro
        return jsonify({"message": f"Retiraste {retiro}", "saldo": saldo, "success": True})
    else:
        return jsonify({"message": "Saldo insuficiente", "saldo": saldo, "success": False})

if __name__ == "__main__":
    app.run(debug=True)
