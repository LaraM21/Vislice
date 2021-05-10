% rebase("pageBase.tpl" , title = "Igrajmo se")

  <h1>Vislice</h1>

  <h2>Dosedaj si uganil</h2>
  <h3>{{ igra.pravilni_del_gesla() }}</h3>

  <h2>Dosedaj si zgrešil</h2>
  <h3>{{ igra.nepravilni_ugibi() }}</h3>

  % if stanje == 'w':
  <h3>Zmagal si</h3>
  % elif stanje == 'x':
  <h3>Zgubil si</h3>
  <h4>Prava beseda je bila {{ igra.geslo }}</h4>
  % else:
  <form  method="POST">
        <label>
        Vnesite črko:
    <input type = "text" name = "ugibana_crka">
        </label>
    <input type="submit" >UGIBAJ!</input>
    % end
  </form>
