from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory user data
users = []

# GET all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# POST a new user
@app.route('/users', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data.get("name") or not data.get("email"):
        return jsonify({"error": "Name and email are required"}), 400
    users.append(data)
    return jsonify({"message": "User added", "user": data}), 201

# PUT to update user by index
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id >= len(users):
        return jsonify({"error": "User not found"}), 404
    data = request.get_json()
    users[user_id].update(data)
    return jsonify({"message": "User updated", "user": users[user_id]}), 200

# DELETE a user by index
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id >= len(users):
        return jsonify({"error": "User not found"}), 404
    deleted = users.pop(user_id)
    return jsonify({"message": "User deleted", "user": deleted}), 200

if __name__ == '__main__':
    app.run(debug=True)
