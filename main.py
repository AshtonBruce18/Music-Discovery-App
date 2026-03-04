from flask import Flask, redirect, url_for, render_template, request, jsonify
import json
import spotify

app = Flask(__name__)


@app.route("/", methods=["POST","GET"])
def home():
    if request.method == "POST":
        answer = request.form["genre"]
        return redirect(url_for("answer", ans=answer))
    else:
        return render_template("index.html")

@app.route("/<ans>")
def answer(ans):
    return render_template("artist.html", genre=ans)
   
    
@app.route("/api/<genre>")
def display(genre):
    token = spotify.get_token()
    artists = spotify.artist_by_genre(token, genre)

    return jsonify(artists)


    '''songs = main.songs
    result = "<ol>"
    for song in songs:
        result += f"<li>{song['name']}</li>"
    result += "</ol>"
    return result
    '''


if (__name__ == "__main__"):
    app.run()

