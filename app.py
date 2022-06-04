# services
from api.services import friends_services
# flask
from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({
        "message": "Welcome to my friends API!"
    })


@app.route("/friends", methods=["GET"])
def get_all_friends():
    friends = friends_services.get_all_friends()
    return jsonify({
        "message": "friends found",
        "data": friends,
        "error": False
    })


@app.route("/friends/<int:friend_id>", methods=["GET"])
def get_one_friend(friend_id: int):
    friend = friends_services.get_one_friend(friend_id)

    return jsonify({
        "message": "friend found",
        "data": friend,
        "error": False
    })


@app.route("/friends", methods=["POST"])
def create_friend():
    payload = request.get_json()

    new_fullname = payload.get("fullname")

    if not new_fullname or new_fullname.strip() == "":
        return jsonify({
            "message": "fullname is empty",
            "error": True
        }), 400

    new_telephone = payload.get("telephone")

    if not new_telephone or new_telephone.strip() == "":
        return jsonify({
            "message": "telephone is empty",
            "error": True
        }), 400

    response = friends_services.create_friend(new_fullname, new_telephone)

    if not response:
        return jsonify({
            "message": "error to insert in database",
            "error": True
        }), 500

    new_friend = {
        "fullname": new_fullname,
        "telephone": new_telephone
    }

    return jsonify({
        "message": "friend found",
        "data": new_friend,
        "error": False
    }), 201


@app.route("/friends/<int:friend_id>", methods=["DELETE"])
def delete_friend(friend_id: int):
    response = friends_services.delete_friend(friend_id)

    if not response:
        return jsonify({
            "message": "error to delete in database",
            "error": True
        }), 500

    return jsonify({
        "message": "friend removed",
        "error": False
    })


@app.route("/friends/<int:friend_id>", methods=["PUT", "PATCH"])
def update_friend(friend_id: int):
    payload = request.get_json()

    new_fullname = payload.get("fullname")
    new_telephone = payload.get("telephone")

    response = friends_services.update_friend(friend_id, new_fullname, new_telephone)

    if not response:
        return jsonify({
            "message": "error to update in database",
            "error": True
        }), 500

    return jsonify({
        "message": "friend updated",
        "error": False
    })


if __name__ == '__main__':
    app.run()
