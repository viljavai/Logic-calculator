### Viikkoraportti 4

Ma 7.8 - 2h
- Aloittelin CNF-funtion tekemistä, tämä osoittautui vaikeammaksi kuin olin alunperin ajatellut. Jonkinlaista refaktorointia pitää luultavasti tehdä tällä viikolla.

8.8 - 3h
- Muokattu totuustaulun palauttavaa funktiota
- Tehty cnf-funktiota
- Tehty toimivat cnf- ja dnf-funktiot.

9.8 - 3h
- Kirjoitin testejä cnf- ja dnf-funktioille. Nämä toimivat nyt.
- Kokonais-testikattavuus 99%.
- Aloitin jonkunlaisen suorituskykytestauksen tekemisen.
- Kaikki suunnitellut osat ohjelmasta on nyt toteutettu, vielä pitää lisätä konkatenoitujen muuttujien tunnistaminen shunting yard -algoritmiin.

Suorituskykytestaus on vielä vähän kysymysmerkki, ajattelin testata totuustaulun tekemiseen kuluvaa aikaa riippuen muuttujien määrästä. Tästä voisi tehdä jonkin hienon käppyrän.
- Onko tämä ^ ihan ok?
- Pitäisikö postfix-muunnokseen kuluvaa aikaa mitata myös? Tämän aikavaativuushan on yleisesti tiedossa. 