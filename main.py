from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/api/v1/healthz")
def health():
    return jsonify({"message":"Ok v1"}), 200

@app.route("/api/v1/users/<id>")
def get_user(id):
    req_name = request.args.get("name")
    user = {
        "id": id,
        "name": req_name if req_name else "Chandara",
        "email": "name@example.com"
    }
    return jsonify(user), 200

@app.route("/api/v1/users",methods=['POST'])
def create_user():
    req_user = request.get_json()
    return jsonify(req_user), 201

if __name__ == "__main__":
    app.run(debug=True)