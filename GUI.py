import Pferde
import Funktionen as fkt

jockey_eins = Pferde.Jockey("Benni", 2)
pferd_eins = Pferde.Pferd(1, "Benno Breitpferd", 10, jockey_eins)

wettkonto, erfahrung, pferde, spieler = fkt.initialization(Pferde.Konto, Pferde.Jockey)

spieler.zeige_jockey()