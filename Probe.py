import Pferde
import Funktionen as fkt
import Initialization as int

jockey_eins = Pferde.Jockey("Benni", 2)
pferd_eins = Pferde.Pferd(1, "Benno Breitpferd", 10, jockey_eins)

pferde_teilnehmer, pferde_reserve, jockey_liste, spieler_stats, teilnehmer \
    = int.initialization(Pferde.Pferd, Pferde.Jockey)

for n in pferde_teilnehmer:
    n.zeige_daten()


for n in teilnehmer.items():
    schlüssel, wert = n

    if teilnehmer[schlüssel] == spieler_stats:
        print("\nKontostand:", teilnehmer["Spieler"]["Balance"])

fkt.pferdemarkt(pferde_reserve)