# from flask import Flask, render_template, request, redirect, session
# import mysql.connector
# from datetime import datetime

# app = Flask(__name__)
# app.secret_key = "veldghemmelig123"


# def get_db():
#     return mysql.connector.connect(
#         host="10.200.14.17",
#         user="heleneliasi",
#         password="dorispillow123",
#         database="sushibutikk"
#     )


# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/info", methods=["GET", "POST"])
# def info():
#     if request.method == "POST":
#         navn = request.form.get("navn")
#         nummer = request.form.get("nummer")
#         epost = request.form.get("epost")

#         db = get_db()
#         cursor = db.cursor()

#         cursor.execute(
#             "INSERT INTO kunde (navn, nummer, epost) VALUES (%s, %s, %s)",
#             (navn, nummer, epost)
#         )
#         db.commit()

#         session["kunde_id"] = cursor.lastrowid

#         cursor.close()
#         db.close()

#         return redirect("/meny")

#     return render_template("info.html")


# @app.route("/meny", methods=["GET", "POST"])
# def meny():
#     db = get_db()
#     cursor = db.cursor()

#     if request.method == "POST":
#         kunde_id = session.get("kunde_id")

#         # Riktig måte for radio button → får EN verdi
#         produkt_id = request.form.get("produkt")
#         ordre_id = request.form.get("ordre")

#         # Feilhåndtering hvis ingen valgt
#         if not produkt_id:
#             cursor.execute("SELECT * FROM meny")
#             produkter = cursor.fetchall()
#             cursor.close()
#             db.close()
#             return render_template("meny.html",
#                                    produkter=produkter,
#                                    error="Du må velge en rett før du kan betale.")

#         # Lagre én bestilling (produkt_id er ett tall)
#         cursor.execute(
#             "INSERT INTO bestilling (produkt_id, tidspunkt, kunde_id) VALUES (%s, NOW(), %s)",
#             (produkt_id, kunde_id)
#         )
#         db.commit()

#         # Hent navnet på produktet (må være i liste)
#         cursor.execute(
#             "SELECT produkt FROM meny WHERE id = %s",
#             (produkt_id,)
#         )
#         result = cursor.fetchone()
#         navn = result[0]
#         pris = result[1]

#         navn = cursor.fetchone()[0]

#         cursor.close()
#         db.close()

#         return render_template(
#             "bestilt.html",
#             produkt=navn,
#             total=pris,
#             ordre_id=ordre_id,
#             tidspunkt=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#         )

#     # GET → hent menyen
#     cursor.execute("SELECT * FROM meny")
#     produkter = cursor.fetchall()

#     cursor.close()
#     db.close()

#     return render_template("meny.html", produkter=produkter)


# if __name__ == "__main__":
#     app.run(debug=True)



















from flask import Flask, render_template, request, redirect, session
import mysql.connector
from datetime import datetime

# Flask= lager selve webapp
# render_template= viser html sider
# request = henter data fra skjema
# redirect= sender brukeren til en annen side
# session = lagrer info om kunden

app = Flask(__name__)
app.secret_key = "veldghemmelig123"


def get_db():
    return mysql.connector.connect(
        host="10.200.14.17",
        user="heleneliasi",
        password="dorispillow123",
        database="sushibutikk"
    )


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/info", methods=["GET", "POST"])
def info():
    if request.method == "POST":
        navn = request.form.get("navn")
        nummer = request.form.get("nummer")
        epost = request.form.get("epost")

        db = get_db()
        cursor = db.cursor()

        cursor.execute(
            "INSERT INTO kunde (navn, nummer, epost) VALUES (%s, %s, %s)",
            (navn, nummer, epost)
        )
        db.commit()


        #for å senere knytte bestillingen til kunden
        session["kunde_id"] = cursor.lastrowid

        #lukker databasen
        cursor.close()
        db.close()

        return redirect("/meny")

    return render_template("info.html")


@app.route("/meny", methods=["GET", "POST"])
def meny():
    db = get_db()
    cursor = db.cursor()

    # Hvis brukeren sender inn valgt sushi
    if request.method == "POST":
        produkt_id = request.form.get("produkt")

        # Legg inn bestilling i databasen
        cursor.execute(
            "INSERT INTO bestilling (produkt_id, tidspunkt, kunde_id) VALUES (%s, NOW(), 1)",
            (produkt_id,)
        )
        db.commit()

        # Hent produktnavn
        cursor.execute("SELECT produkt FROM meny WHERE id = %s", (produkt_id,))
        produktnavn = cursor.fetchone()[0]

        cursor.close()
        db.close()

        tidspunkt = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return render_template("bestilt.html", produkt=produktnavn, tidspunkt=tidspunkt)

    # GET → vis meny
    cursor.execute("SELECT * FROM meny")
    produkter = cursor.fetchall()

    cursor.close()
    db.close()

    return render_template("meny.html", produkter=produkter)


# -----------------------------------------------------
# BESTILT-SIDE
# -----------------------------------------------------
@app.route("/bestilt")
def bestilt():
    return render_template("bestilt.html")


# -----------------------------------------------------
# START SERVER
# -----------------------------------------------------
if __name__ == "__main__":
    app.run(debug=True)













# @app.route("/meny", methods=["GET", "POST"])
# def meny():
#     db = get_db()
#     cursor = db.cursor()

#     cursor.execute("SELECT * FROM meny")
#     produkter = cursor.fetchall()

#     if request.method == "POST":
#         kunde_id = session.get("kunde_id")
#         produkt_id = request.form.get("produkt")

#         if not produkt_id:
#             cursor.close()
#             db.close()
#             return render_template(
#                 "meny.html",
#                 produkter=produkter,
#                 error="Du må velge en rett før du kan betale."
#             )

#         cursor.execute(
#             "INSERT INTO bestilling (produkt_id, tidspunkt, kunde_id) VALUES (%s, NOW(), %s)",
#             (produkt_id, kunde_id)
#         )
#         db.commit()

#         ordre_id = cursor.lastrowid

#         cursor.execute(
#             "SELECT produkt, pris FROM meny WHERE id = %s",
#             (produkt_id,)
#         )
#         produkt, pris = cursor.fetchone()

#         cursor.close()
#         db.close()

#         return render_template(
#             "bestilt.html",
#             produkt=produkt,
#             total=pris,
#             ordre_id=ordre_id,
#             tidspunkt=datetime.now().strftime("%m-%d %H:%M")
#         )

#     cursor.close()
#     db.close()
#     return render_template("meny.html", produkter=produkter)




#dette kjører appen
if __name__ == "__main__":
    app.run(debug=True)
