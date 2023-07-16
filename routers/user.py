from flask import Blueprint, request, jsonify

account_blueprint = Blueprint(
    "account",
    __name__,
)


@account_blueprint.route("/users/<id>")
def get_user(id):
    req_name = request.args.get("name")
    user = {
        "id": id,
        "name": req_name if req_name else "Chandara",
        "email": "name@example.com"
    }
    return jsonify(user), 200


@account_blueprint.route("/users", methods=['POST'])
def create_user():
    req_user = request.get_json()
    return jsonify(req_user), 201
