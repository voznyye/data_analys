import calcul

liczbaPowtórzeń=10
# ograniczenie liczby powtórzeń pętli

def main():
    calcul.writeCsv('LICZBA KLASTRÓW',calcul.liczbaKlastrów)
    calcul.losujCentroidy()
    calcul.wypiszCentroidy()
    calcul.przypiszKrotkomNumeryKlastrów()
    calcul.utwórzKlastry()
    calcul.wypiszKlastry()
    
    # poniżej założono blokadę pętli
    repeat=liczbaPowtórzeń
    while repeat < liczbaPowtórzeń:
        calcul.newCentroidy()
        calcul.wypiszCentroidy()
        calcul.przypiszKrotkomNumeryKlastrów()
        calcul.utwórzKlastry()
        calcul.wypiszKlastry()
        repeat+=1


main()