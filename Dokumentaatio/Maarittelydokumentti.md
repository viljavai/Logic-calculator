## Määrittelydokumentti

- Ohjelma tehdään Python-kielellä. Pystyn tarvittaessa vertaisarvioimaan myös Javalla tehtyjä projekteja, mutta aika paljon heikommin kuin Pythonia.
- Ohjelmassa käytetään Shunting yard -algoritmia.
- Ohjelmalla voidaan tulostaa predikaattilogiikan lauseille totuustaulu, CNF-muoto tai DNF-muoto. Shunting yard -algoritmi soveltuu hyvin projektiin, koska se käy hyvin aritmeettisten operaatioiden käsittelyyn ja pystytään soveltamaan tätä myös propositiologiikkaan.
- Syötteitä:
  > - "totuustaulu A AND B => A OR C" Tämän tulostus olisi tautologia, eli totuustaulu, jossa kaikki arvot TRUE.
  > - "CNF (A and B) or C" Tämän tulostus olisi "(A or B) and (B or C)"
  > - "DNF (A or B) and C" Tämän tulostus olisi (A and C) or (B and C)
- Koodi ja kommentit on nyt englanniksi ja dokumentaatio suomeksi. Jos tämä on ongelma, voin kääntää kommentit suomeksi ennen vertaisarviointeja.
- Koulutusohjelma on TKT-kandi.

### O-analyysi

#### Aikavaativuus

- Syötteen käsittely shunting yard -algoritmilla: O(n)
- Jos syötteessä on m muuttujaa, totuustauluun tulee 2^m riviä. Näin ollen totuustaulun luomisen aikavaativuus on O(2^m), missä m on muuttujien määrä syötteessä. 

Kokonais-aikavaativuus on siis **O(2^m)**

#### Tilavaativuus 
- Shunting yard -algoritmin tilvaativuus: O(n)
- Totuustaulun generoimisen tilavaativuus: O(2^m), missä m on muuttujien määrä syötteessä.

Kokonais-tilavaativuus on siis **O(2^m)**

### Lähteitä:
- https://en.wikipedia.org/wiki/Shunting_yard_algorithm pseudokoodi
- (Näitä tulee lisää)

