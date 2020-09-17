import pickle, time
filename = 'betalinger.pk'
Savedfilename= 'betalinger2.pk'

fodboldtur ={}

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

def save():
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
        payMoney()

    dict[name] += amount


    if dict[name] > 562.5:
        print("Du kan ikke insætte mere end 562,5.-")
        menu()
    else:
        print('Du har nu betalt ' + str(dict[name]) + ' kr.')

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
        print(str(item) + ', ' + str(dict[item]) + ' kr. Mangler ' + str(562.5 - dict[item]))
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
    menu()

def resetAll():
    for name in dict.keys():
        dict[name] = 0
    save()
    menu()

def menu():
    print("MENU")
    print("1: Print liste")
    print("2: Hvor meget har jeg betalt?")
    print("3: Betal")
    print("4: Afslut program og gem")
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
        resetAll()            #Det er bare så vi har mulighed for at genstarte beløbene når vi tester programmet
    else:
        print('Ugyldig indtastning')
        time.sleep(1)
        menu()

infile = open(filename,'rb')
dict = pickle.load(infile)
infile.close()
menu()

