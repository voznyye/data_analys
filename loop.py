import calcul

def main():
    
    calcul.kmeans_plus_plus() 
    calcul.przypiszKrotkomNumeryKlastrów() 
    calcul.utwórzKlastry() 
    # wypiszCentroidy() 
    calcul.wypiszKlastry()

    c = 0
    print(f"iteration {c}: completed")

    for _ in range(10):
        calcul.newCentroidy()
        calcul.przypiszKrotkomNumeryKlastrów()
        calcul. utwórzKlastry()
        # wypiszCentroidy()
        calcul.wypiszKlastry()
            
        c += 1
        print(f"iteration {c}: completed")


    
main()