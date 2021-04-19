
STEVILO_DOVOLJENIH_NAPAK = 10
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o' 
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ =  'X'

class Igra:

    def __init__(self, geslo, crke):
        self.geslo = geslo
        self.crke = crke[:]

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka  in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        vse_crke = True
        for crka in self.geslo():
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

    

    
