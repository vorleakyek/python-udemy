from flask import Flask

app = Flask(__name__)
print(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/bye")
def bye():
    return "<p>Bye!</p>"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, you are {number} years old!"


@app.route('/post/<name>/<int:post_id>')
def show_post(post_id,name):
    # show the post with the given id, the id is an integer
    return f'{name} Post {post_id}'


if __name__ == "__main__":
    app.run(debug=True)
