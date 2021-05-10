import bottle
import model

vislice = model.Vislice()


@bottle.get("/")
def osnovna_stran():
    return bottle.template("index.tpl")

@bottle.get("/igra/")
def nova_igra():
    id_igre = vislice.nova_igra()
    return bottle.redirect(f"/igra/{id_igre}/")

@bottle.get("/igra/<id_igre:int>/")
def poglej_igro(id_igre):
    igra, stanje = vislice.igre[id_igre]
    return bottle.template("igra.tpl", igra=igra, stanje = stanje)

@bottle.post("/igra/<id_igre:int>/")
def ugibaj_crko(id_igre):
    ugibana_crka = bottle.request.forms["ugibana_crka"]

    vislice.ugibaj(id_igre, ugibana_crka)


    bottle.redirect("")




#poženi miško
bottle.run(reloader=True, debug=True)

print("Tega se ne sme videt")