from flask import Flask, render_template, url_for
app = Flask(__name__)                    # this gets the name of the file so Flask knows it's name

@app.route("/")                          # this tells you the URL the method below is related to
@app.route("/home")        # this prints HTML to the webpage
def home():
    return render_template("index.html") 
    
@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/music")
def music():
    return render_template("music.html")

@app.route("/videos")
def videos():
    return render_template("player.html")

@app.route("/test_page")
def test_page():
    return render_template("test.html")

if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, host="0.0.0.0")