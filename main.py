import sqlite3
from flask import Flask, render_template, request, redirect
from dati import add_user

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():


    if request.method == "POST":
        vards = request.form['name']
        uzvards = request.form['lastname']
        lietotajvards = request.form['username']

        if vards and uzvards and lietotajvards:
            add_user(vards, uzvards, lietotajvards)

        dati = f"Pievienots lietotājs - {vards} {uzvards}, {lietotajvards}"

        return render_template("index.html", aizsutitais = dati)

    return render_template("index.html")

@app.route("/zinojumi", methods=["POST","GET"])
def zinojumi():

        #    VAJAG UZTAISĪT sistēmu kas aizsūta vārdus n shit no datubāzes uz ziņojumiem

    return render_template("zinojumi.html")

@app.route("/statistika")
def statistika():
    return render_template("statistika.html")



if __name__ == '__main__':
    app.run(port = 5000)