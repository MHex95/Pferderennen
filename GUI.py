import Pferde
import Funktionen as fkt

jockey_eins = Pferde.Jockey("Benni", 2)
pferd_eins = Pferde.Pferd(1, "Benno Breitpferd", 10, jockey_eins)

wettkonto, pferde, spieler, erfahrung = fkt.initialization(Pferde.Pferd, Pferde.Jockey, Pferde.Konto)

for n in pferde:
    n.zeige_daten()