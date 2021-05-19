def initialization(Pferd, Jockey):
    kontostand = 100
    level = 1
    erfahrung = 0
    spieler = Jockey("Spieler", level)

    spieler_stats = {"Spieler": spieler, "Level": level, "Erfahrung": erfahrung, "Balance": kontostand}

    pferde_teilnahme = []
    pferde_reserve = []
    jockey_liste = []

    # Pferde an den Start bringen
    jockey_eins = Jockey("Stefan Superschnell", 9)
    pferd_eins = Pferd(1, "Red Thunder", 9, jockey_eins)
    pferde_teilnahme.append(pferd_eins)
    jockey_liste.append(jockey_eins)

    jockey_zwei = Jockey("Sebastian Sporenhart", 8)
    pferd_zwei = Pferd(2, "Brutus", 7, jockey_zwei)
    pferde_teilnahme.append(pferd_zwei)
    jockey_liste.append(jockey_zwei)

    jockey_drei = Jockey("Peter Pusteblume", 4)
    pferd_drei = Pferd(3, "Mister Hüh", 6, jockey_drei)
    pferde_teilnahme.append(pferd_drei)
    jockey_liste.append(jockey_drei)

    jockey_vier = Jockey("Holger Hinkelstein", 2)
    pferd_vier = Pferd(4, "Entchen", 4, jockey_vier)
    pferde_teilnahme.append(pferd_vier)
    jockey_liste.append(jockey_vier)

    jockey_fünf = Jockey("Bernd Blindfisch", 1)
    pferd_fünf = Pferd(5, "Ist das etwa ein Stein?!", 1, jockey_fünf)
    pferde_teilnahme.append(pferd_fünf)
    jockey_liste.append(jockey_fünf)

    pferd_sechs = Pferd(6, "Quirrly Whirly", 2, spieler)
    pferde_reserve.append(pferd_sechs)

    pferd_sieben = Pferd(6, "Ross Anthony", 4, spieler)
    pferde_reserve.append(pferd_sieben)

    pferd_acht = Pferd(6, "Grand Grey", 7, spieler)
    pferde_reserve.append(pferd_acht)

    pferd_neun = Pferd(6, "Streitross", 9, spieler)
    pferde_reserve.append(pferd_neun)

    pferd_zehn = Pferd(6, "Chinesisches Pferd", 11, spieler)
    pferde_reserve.append(pferd_zehn)

    teilnehmer = {"Spieler": spieler_stats, "Pferde Rennen": pferde_teilnahme,
                  "Pferde Stall": pferde_reserve, "Jockeys": jockey_liste}

    return pferde_teilnahme, pferde_reserve, jockey_liste, spieler_stats, teilnehmer