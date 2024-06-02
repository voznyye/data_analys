import calcul

def main():
    
    # Основной алгоритм
    calcul.kmeans_plus_plus()  # Инициализация центроидов с использованием K-Means++
    calcul.przypiszKrotkomNumeryKlastrów()  # Присвоение точкам ближайших кластеров
    calcul.utwórzKlastry()  # Создание кластеров
    # wypiszCentroidy()  # Запись центроидов
    calcul.wypiszKlastry()  # Запись кластеров

    c = 0
    print(f"iteration {c}: completed")

    # Перераспределение кластеров
    for _ in range(7):  # Количество итераций перераспределения
        calcul.newCentroidy()
        calcul.przypiszKrotkomNumeryKlastrów()
        calcul. utwórzKlastry()
        # wypiszCentroidy()
        calcul.wypiszKlastry()
            
        c += 1
        print(f"iteration {c}: completed")


    
main()