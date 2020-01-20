from flask import Flask
from flask import render_template
from flask import request
from flask import redirect

guestbook = [
    {
    "name": "Mędrek", "email":" medrek@bajkiokranoludach.pl",
     "comment": "Ninja bez opaski jest jak kot bez ogona"
    },
    {
     "name": "Gburek", "email":"gburek@bajkiokranoludach.pl",
     "comment": "Jestem na nie"
    },
    {
    "name": "Apsik", "email":"apsik@bajkiokranoludach.pl",
     "comment": "Chory jestem ciągle"
    },
    {
    "name": "Wesołek", "email":"wesolek@bajkiokranoludach.pl",
     "comment": "Ninja bez opaski jest jak kot bez ogona"
    },
    {
    "name": "Śpioszek", "email":"spioszek@bajkiokranoludach.pl",
     "comment": "Hrrrrmmmmm hrrrrmmmmm"
    },
    {
    "name": "Gapcio", "email":"gapcio@bajkiokranoludach.pl",
     "comment": "O kurcze, ouuuuuu!"
    },
    {
    "name": "Nieśmiałek", "email":"niesmialek@bajkiokranoludach.pl",
     "comment": "Ten tego..."
    }
]


app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def hello():
    name = request.form.get('guest_name', request.args.get('guest_name'))
    email = request.form.get('guest_email', request.args.get('guest_email'))
    comment = request.form.get('guest_comment', request.args.get('guest_comment'))
    new_guest = {"name": name, "email": email, "comment":comment}

    if name and email and comment:
        guestbook.append(new_guest)

    if (request.method == 'POST'):
        return redirect('/', code=302, Response=None)


    return render_template('hello.html', comments=guestbook)

if __name__ == '__main__':
    app.run(debug=True)