from flask import Flask, jsonify
from flask_cors import CORS
from routers import user, dialogflow
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
CORS(app)


app.register_blueprint(user.user_blueprint, url_prefix="/api/v1")
app.register_blueprint(dialogflow.dialogflow_blueprint, url_prefix="/api/v1")


@app.route("/api/v1/healthz")
def health():
    return jsonify({"message": "Ok v1"}), 200


if __name__ == "__main__":
    app.run(debug=True)
