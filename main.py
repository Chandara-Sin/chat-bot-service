from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/v1")
def home():
    return "Home"

@app.route("/api/v1/users/<id>")
def get_user(id):
    req_name = request.args.get("name")
    user = {
        "id": id,
        "name": req_name if req_name else "Chandara",
        "email": "name@example.com"
    }
    return jsonify(user), 200


if __name__ == "__main__":
    app.run(debug=True)