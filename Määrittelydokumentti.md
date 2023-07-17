### Määrittelydokumentti

- Ohjelma tehdään Python-kielellä. Pystyn tarvittaessa vertaisarvioimaan myös Javalla tehtyjä projekteja, mutta aika paljon heikommin kuin Pythonia.
- Ohjelmassa käytetään Shunting yard -algoritmia.
- Ohjelmalla voidaan tulostaa predikaattilogiikan lauseille totuustaulu, CNF-muoto tai DNF-muoto. Shunting yard -algoritmi soveltuu hyvin projektiin, koska se soveltuu hyvin aritmeettisten operaatioiden käsäittelyyn ja pystytään soveltamaan tätä myös propositiologiikkaan.
- Syötteitä:
  > - "totuustaulu A AND B => A OR C" Tämän tulostus olisi tautologia, eli totuustaulu, jossa kaikki arvot TRUE.
  > - "CNF (A and B) or C" Tämän tulostus olisi "(A or B) and (B or C)"
  > - "DNF (A or B) and C" Tämän tulostus olisi (A and C) or (B and C)
- Aikavaativuuden pitäisi olla O(n) (Shunting yard)
