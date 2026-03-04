from dotenv import load_dotenv
import os
import base64
import requests
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = requests.post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}

def artist_by_genre(token, genre):
    url = f"https://api.spotify.com/v1/search?q=genre%3D{genre}&type=artist&limit=50"
    headers = get_auth_header(token)
    result = requests.get(url, headers=headers)
    json_result = json.loads(result.content)["artists"]

    artists = json_result["items"]
    rareArtists = []
    for artist in artists:
        if(artist['popularity'] <= 50):
            rareArtists.append(artist)
    return json.dumps(rareArtists)

