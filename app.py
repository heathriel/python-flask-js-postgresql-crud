from flask import Flask, request, jsonify, send_file
import os
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="35.209.201.133",
    port=5432,
    user="usyny1atg53ox",
    password="BKZ4bvr3mqe!yrf_npx",
    database="dbwdxqj0qx08zj"
)
cur = conn.cursor()

@app.route("/api/user/<unique_identifier>", methods=["GET"])
def get_user(unique_identifier):
    cur.execute(f"SELECT * FROM uwt WHERE unique_identifier = '{unique_identifier}'")
    user = cur.fetchone()

    if not user:
        return jsonify({"message": "User not found"}), 404

    return jsonify(user)

@app.route("/api/user/<unique_identifier>", methods=["PUT"])
def update_user(unique_identifier):
    new_user = request.get_json()
    first_name = new_user.get("first_name")
    full_name = new_user.get("full_name")
    email = new_user.get("email")
    photo_url = new_user.get("photo_url")
    bio = new_user.get("bio")
    six_word_one_liner = new_user.get("six_word_one_liner")
    location = new_user.get("location")
    key_words_change_from_skills = new_user.get("key_words_change_from_skills")
    organization = new_user.get("organization")
    title = new_user.get("title")
    organization_url = new_user.get("organization_url")
    linkedin_url = new_user.get("linkedin_url")
    last_update = new_user.get("last_update")
    
    cur.execute(f"UPDATE uwt SET first_name = '{first_name}', full_name = '{full_name}', email = '{email}', photo_url = '{photo_url}', bio = '{bio}', six_word_one_liner = '{six_word_one_liner}', location = '{location}', key_words_change_from_skills = '{key_words_change_from_skills}', organization = '{organization}', title = '{title}', organization_url = '{organization_url}', linkedin_url = '{linkedin_url}', last_update = '{last_update}' WHERE unique_identifier = '{unique_identifier}' RETURNING *")
    updated_user = cur.fetchone()
    conn.commit()

    if not updated_user:
        return jsonify({"message": "User not found"}), 404

    return jsonify(updated_user)

@app.get('/')
def home():
    return send_file('static/index.html')


if __name__ == "__main__":
    app.run(debug=True)
