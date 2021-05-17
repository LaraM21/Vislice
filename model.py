
import json

STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o' 
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ =  'X'
ZACETEK = 'A'
DATOTEKA_S_STANJEM= "podatki.json"


class Vislice:
    """
    Krovni objekt, ki upravlja z vsemi igrami (baza vseh iger in kaj dogaja noter)
    """
    def __init__(self,zacetne_igre, datoteka_s_stanjem = DATOTEKA_S_STANJEM):
        self.igre = zacetne_igre
        self.datoteka_s_stanjem = datoteka_s_stanjem

    def prost_id_igre(self):
        if not self.igre:
            return 1
        return max(self.igre.keys()) + 1

    def nova_igra(self, ):
        nov_id = self.prost_id_igre()

        sveza = nova_igra(bazen_besed)

        self.igre[nov_id] = (sveza,ZACETEK)

        return nov_id
    
    def ugibaj(self, id_igre,crka):
        igra, stanje = self.igre[id_igre]
        novo_stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, novo_stanje)


    def dobi_json_slovar(self):

        slovar_iger = {}
        for id_igre,(igra,stanje) in self.igre.items():
            slovar_iger[id_igre] = [
                igra.dobi_json_slovar(),
                stanje,
            ]

        return {
            "igre": slovar_iger,
            "datoteka_s_stanjem" : self.datoteka_s_stanjem,
            }

    @staticmethod
    def preberi_iz_datoteke(ime_datoteke=DATOTEKA_S_STANJEM):
        with open(ime_datoteke, "r") as in_file:
            slovar = json.load(in_file) #slovar
        return Vislice.dobi_vislice_iz_slovarja(slovar)


    @staticmethod
    def dobi_vislice_iz_slovarja(slovar):
        slovar_iger = {} #slovar objektov - Igra
        for id_igre, (igra_slovar,stanje) in slovar["igre"].items():
            slovar_iger[int(id_igre)] = (
                Igra.dobi_igro_iz_slovarja(igra_slovar),
                stanje
            )
        print(slovar_iger)
        return Vislice(
            slovar_iger,
            slovar["datoteka_s_stanjem"]
        )
   
    def zapisi_v_datoteko(self):
        slovar = self.dobi_json_slovar()
        with open(self.datoteka_s_stanjem,"w") as out_file:
            json.dump(slovar,out_file)



class Igra:

    def __init__(self, geslo, crke):
        self.geslo = geslo.upper()
        self.crke = crke[:]

    def dobi_json_slovar(self):
        return{
        "geslo" : self.geslo,
        "crke" : self.crke,
        }

    @staticmethod
    def dobi_igro_iz_slovarja(slovar):
        return Igra(
            slovar["geslo"],slovar.get("crke","")
        )


    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka  in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        vse_crke = True
        for crka in self.geslo:
            if crka in self.pravilne_crke():
                pass
            else:
                vse_crke = False
                break
        return vse_crke and STEVILO_DOVOLJENIH_NAPAK >= self.stevilo_napak()

    def poraz(self):
        return STEVILO_DOVOLJENIH_NAPAK < self.stevilo_napak()

    def pravilni_del_gesla(self):
        delni = ''
        ugibanje = [crka.upper() for crka in self.crke]
        for crka in self.geslo:
            if crka.upper() in ugibanje:
                delni += crka + ''
            else:
                delni += '_ '
        return delni

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self,crka):
        crka = crka.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        elif crka in self.geslo:
            self.crke.append(crka)
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            self.crke.append(crka)
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA

import random

with open("besede.txt") as inp:
    bazen_besed =inp.readlines()

def nova_igra(bazen):
    return Igra(random.choice(bazen),[])