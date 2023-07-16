from flask import Blueprint, request, jsonify

user_blueprint = Blueprint(
    "user",
    __name__,
)


@user_blueprint.route("/users/<id>")
def get_user(id):
    req_name = request.args.get("name")
    user = {
        "id": id,
        "name": req_name if req_name else "Chandara",
        "email": "name@example.com"
    }
    return jsonify(user), 200


@user_blueprint.route("/users", methods=['POST'])
def create_user():
    req_user = request.get_json()
    return jsonify(req_user), 201
