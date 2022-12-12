import bottle
import model
#NIKOLI NE IMPORTAJ sqlite3 v spletni vmesnik

glavni_model = model.Model()

@bottle.get("/")
def glavna_stran():
    return bottle.template("glavna.html", uporabniki = podatki)

bottle.run(debug = True, reloader = True)


