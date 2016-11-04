from flask import Flask
from os import environ

app = Flask(__name__)

@app.route("/")
@app.route("/hello")
def say_hi():
    return "Hello World!"
    
@app.route("/hello/<name>")
def hello_person(name):
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a picture of a kitten.  Awww...
        </p>
        <img src="http://placekitten.com/g/200/300">
    """
    return html.format(name.title())
    
@app.route("/jedi/<first_name>/<last_name>/")
def hello_jedi(first_name, last_name):
    
    jedi_name=first_name[:3] + last_name[:2]
    html = """
        <h1>
            Hello {}!
        </h1>
        <p>
            Here's a random starwars-ey picture
        </p>
        <img src="https://source.unsplash.com/user/danielkcheung/1600x900">
    """
    return html.format(jedi_name.title())

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))
