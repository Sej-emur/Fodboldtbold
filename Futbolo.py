import pickle, time, random
filename = 'betalinger.pk'
Savedfilename= 'betalinger2.pk'



dict = {
    'Hans Hansen': 0,
    'Klaus Klausen': 0,
    'Ole Olsen': 0,
    'Bent Bentsen': 0,
    'Peter Petersen': 0,
    'Anders Andersen': 0,
    'Jens Jensen': 0,
    'Ib Ibsen': 0
    }

def save(): #Gemme funktion, der bliver kaldt når de andre funktioner har lavet en ændring, der skal gemmes
    outfile = open(filename, 'wb')
    pickle.dump(dict, outfile)
    outfile.close()

def afslut():
    save()
    print("Programmet er afsluttet!")
    quit()



def payMoney():
    name = input('Navn: ')
    amount_string = input('Beløb: ')
    try:
        amount = float(amount_string)
    except ValueError:
        print("Ugyldig indtastning")
        payMoney()

    def confirm():
        valg = input("Er du sikker?(ja/nej): ")
        valg = valg.lower()
        if valg == "ja":
            dict[name] += amount
            if dict[name] > 562.5:  # 562.5 er det beløb alle skal betale for at nå de 4500 kr.
                print(
                    "Du kan ikke insætte mere end 562,5.-")  # Denne del af koden sørger for at ingen betaler for meget
                menu()
            else:
                print('Du har nu betalt ' + str(dict[name]) + ' kr.')
        elif valg == "nej":
            print("Går til hovedmenuen...")
            time.sleep(2)
            menu()
        else:
            print("Ugyldig intastning")
            confirm()
    confirm()






    save()
    time.sleep(3)
    menu()





def moneyPaid():
    name = input('Navn: ')

    print(name + ' har betalt ' + str(dict[name]) + ' kr. og mangler at betale ' + str(562.5 - dict[name]))
    time.sleep(3)
    menu()

def printliste():

    for item in dict.keys():
        print(str(item) + ', ' + str(dict[item]) + ' kr. Mangler ' + str(562.5 - dict[item]) + ' kr.')
    time.sleep(3)
    menu()

def bottom3_metode_2():
    print("Bottom 3:")
    bund3 = list(sorted(dict.items(), key=lambda kv: (kv[1], kv[0])))[:3]
    for item in bund3:
        print(item)
    time.sleep(3)
    menu()

def reset():
    name = input('Navn: ')
    dict[name] = 0
    save()
    print(f"{name} har nu betalt {dict[name]} kr.")
    time.sleep(2)
    menu()

def resetAll():
    for name in dict.keys():
        dict[name] = 0
    save()
    printliste()
    time.sleep(5)
    menu()

def defaultList():
    for name in dict.keys():
        dict[name] = random.randint(0, 562)
    save()
    printliste()
    time.sleep(5)
    menu()

def menu():
    print("MENU")
    print("1: Print liste")
    print("2: Hvor meget har jeg betalt?")
    print("3: Betal")
    print("4: Gem og afslut")
    print("5: 3 laveste")
    valg = input("Indtast dit valg: ")
    if (valg == '1'):
        printliste()
    if (valg == '2'):
        moneyPaid()
    if (valg == '3'):
        payMoney()
    if (valg == '4'):
        afslut()
    if (valg == "5"):
        bottom3_metode_2()
    if (valg == 'reset'):
        reset()
    if (valg == 'reset all'): #reset og resetAll funktionerne er ikke til brugerne.
        resetAll()   #Det er bare så vi har mulighed for at genstarte beløbene når vi tester programmet
    if (valg == 'default'):
        defaultList()
    else:
        print('Ugyldig indtastning')
        time.sleep(1)
        menu()

infile = open(filename,'rb')
dict = pickle.load(infile)
infile.close()
menu()

