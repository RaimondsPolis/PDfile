import sqlite3
from flask import Flask, render_template, request, redirect
from dati import add_user, iegut_lietotaju, iegut_zinojumus, add_message, iegut_skaitu

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():


    if request.method == "POST":
        vards = request.form['name']
        uzvards = request.form['lastname']
        lietotajvards = request.form['username']
        dati = ""
        try:
            error = ("All text boxes must be filled!")
            if vards and uzvards and lietotajvards:
                add_user(vards, uzvards, lietotajvards)
                error = ""
                dati = (f"Pievienots lietotājs - {vards} {uzvards}, {lietotajvards}")
        except sqlite3.IntegrityError:
            error = ("Username allready exists!")
        except:
            error = ("An unnexpected error occoured!")

        

        return render_template("index.html", aizsutitais = dati, error1 = error)

    return render_template("index.html")

@app.route("/zinojumi", methods=["POST","GET"])
def zinojumi():
    users = iegut_lietotaju()
    dati = iegut_zinojumus()
    error = ""
    if request.method == "POST":
        user_id = request.form['name']
        zinojums = request.form['zinojums']
        try:
            error = "Message cannot be empty"
            if zinojums:
                error = ""
                add_message(zinojums, user_id)
        except:
            error = "An unexpected error occoured!"


        return render_template("zinojumi.html", users = users, dati = dati, error = error)

    return render_template("zinojumi.html", users = users, dati = dati)

@app.route("/statistika")
def statistika():
    lietotaji = iegut_skaitu()
    print(lietotaji)
    return render_template("statistika.html", lietotaji = lietotaji)



if __name__ == '__main__':
    app.run(port = 5000)