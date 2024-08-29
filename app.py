from flask import Flask, request, jsonify, send_from_directory
import instaloader
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='../frontend', static_url_path='')
CORS(app)

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/profile-info', methods=['POST'])
def get_profile_info():
    data = request.json
    profile_name = data.get('profile_name')
    
    if not profile_name:
        return jsonify({"status": "error", "message": "Profile name is required."}), 400

    L = instaloader.Instaloader()
    try:
        profile = instaloader.Profile.from_username(L.context, profile_name)
        profile_info = {
            "username": profile.username,
            "fullname": profile.full_name,
            "bio": profile.biography,
            "followers": profile.followers,
            "following": profile.followees,
            "posts": profile.mediacount,
        }
        return jsonify({"status": "success", "profile_info": profile_info}), 200
    except instaloader.exceptions.ProfileNotExistsException:
        return jsonify({"status": "error", "message": "The profile does not exist or the URL is incorrect."}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": f"An error occurred: {e}"}), 500

if __name__ == '__main':
    app.run(debug=True)
