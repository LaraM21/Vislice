import bottle
import model
COOKIE_ID_IGRE = "ID_IGRE"


@bottle.get("/")
def index():
    return bottle.template("index.tpl")

@bottle.get("/igra/")
def nova_igra():
    vislice = model.Vislice.preberi_iz_datoteke()
    id_igre = vislice.nova_igra()
    print(vislice.igre)
    vislice.zapisi_v_datoteko()
    bottle.response.set_cookie(COOKIE_ID_IGRE,id_igre,
    path = "/", secret = "SECRET" )
    
    bottle.redirect("/igraj/")

@bottle.get("/igraj/")
def igraj_igro():
    id_igre = int(bottle.request.get_cookie(COOKIE_ID_IGRE, secret = "SECRET"))
    vislice = model.Vislice.preberi_iz_datoteke("podatki.json")
    trenutna_igra, trenutno_stanje = \
    vislice.igre[id_igre]
    vislice.zapisi_v_datoteko()
    return bottle.template("igra.tpl",
    igra = trenutna_igra,
    stanje = trenutno_stanje)

@bottle.get("/igra/<id_igre:int>/")
def pokazi_igro(id_igre):
    vislice = model.Vislice.preberi_iz_datoteke("podatki.json")
    trenutna_igra, trenutno_stanje = \
    vislice.igre[id_igre]
    vislice.zapisi_v_datoteko()
    return bottle.template("igra.tpl",
    igra = trenutna_igra,
    stanje = trenutno_stanje)

@bottle.post("/igraj/")
def ugibaj_na_igri_igraj():
    id_igre = int(bottle.request.get_cookie(COOKIE_ID_IGRE, secret = "SECRET"))
    vislice = model.Vislice.preberi_iz_datoteke()
    ugibana = bottle.request.forms["ugibana_crka"]

    vislice.ugibaj(id_igre,ugibana)
    vislice.zapisi_v_datoteko()
    bottle.redirect(f"/igraj/")

"""
@bottle.get("/igra/<id_igre:int>/")
def poglej_igro(id_igre):
    igra, stanje = vislice.igre[id_igre]
    return bottle.template("igra.tpl", igra=igra, stanje = stanje)

@bottle.post("/igra/<id_igre:int>/")
def ugibaj_crko(id_igre):
    ugibana_crka = bottle.request.forms["ugibana_crka"]

    vislice.ugibaj(id_igre, ugibana_crka)

    bottle.redirect("")


"""

#poženi miško
bottle.run(reloader=True, debug=True)

print("Tega se ne sme videt")