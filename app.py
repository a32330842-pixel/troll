from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    ip_visitante = request.headers.get("X-Forwarded-For", request.remote_addr)
    
    with open("visitantes.log", "a") as f:
        f.write(f"{ip_visitante}\n")
    
    return f"<h1>Olá! Seu IP é: {ip_visitante}</h1>"

if __name__ == "__main__":
    app.run(debug=True)