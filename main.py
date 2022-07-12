from flask import Flask, render_template
app = Flask(__name__)                    # this gets the name of the file so Flask knows it's name

@app.route("/")                          # this tells you the URL the method below is related to
@app.route("/home")        # this prints HTML to the webpage
def home():
    return render_template("index.html") 
    
if __name__ == '__main__':               # this should always be at the end
    app.run(debug=True, host="0.0.0.0")