import Pferde
import Funktionen as fkt

jockey_eins = Pferde.Jockey("Benni", 2)
pferd_eins = Pferde.Pferd(1, "Benno Breitpferd", 10, jockey_eins)

pferde_liste, jockey_liste, spieler_stats = fkt.initialization(Pferde.Pferd, Pferde.Jockey)

for n in pferde_liste:
    n.zeige_daten()