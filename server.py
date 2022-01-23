from flask import Flask, render_template, redirect,request
from friend import Friend # import the class from friend.py

app = Flask(__name__)

@app.route("/")
def index():
    friends = Friend.get_all() # call the get all classmethod to get all friends
    print(friends)
    return render_template("index.html", friends = friends)

@app.route('/create_friend', methods=["POST"])
def create_friend():
    data = {
        "fname": request.form["fname"], # First we make a data dictionary from our request.form coming from our template.
        "lname" : request.form["lname"], # The keys in data need to line up exactly with the variables in our query string.
        "occ" : request.form["occ"]}
    Friend.save(data)# We pass the data dictionary into the save method from the Friend class.
    return redirect('/')# Don't forget to redirect after saving to the database.

if __name__ == "__main__":
    app.run(debug=True)