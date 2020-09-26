import csv

    #Main function from an interactive prompt
def main():
    menu()

##################################################################################################

def menu():
    print()
    print("************ MAIN MENU **************")
    print()

#user interface for menu options
    option = input("""
1:  Import and export routes
2:  Means of transport used
3:  Total value of imports and exports
Enter an option: """)
    print()
    
    if option == "1":
        #Clean screen
        print("\033[H\033[J")
        print("****# Import and export routes #*****")
        print()
        #Get function value
        import_export_routes()
        print()
        option = input("""
        Back menu? Y
        Exit? N: 
        """)
        if option == "Y":
          menu()
        elif option == "N":
          pass
    elif option == "2":
        #Clean screen
        print("\033[H\033[J")
        print("****# Means of transport used #*****")
        print()
        #Get function value
        means_transport()
        print()
        option = input("""
        Back menu? Y
        Exit? N: 
        """)
        if option == "Y":
          menu()
        elif option == "N":
          pass
    elif option == "3":
        #Clean screen
        print("\033[H\033[J")
        print("****# Best countries by Total value of imports and exports #*****")
        #Get function value
        total_value()
        print()
        option = input("""
        Back menu? Y
        Exit? N: 
        """)
        if option == "Y":
          menu()
        elif option == "N":
          pass
    else:
        print("You must select a valid option")
        print("Please, try again")
        menu()
        
##################################################################################################

def import_export_routes():

    with open("synergy_logistics_database.csv", "r") as archivo_csv:
        #lector = csv.reader(archivo_csv, delimiter = ",")
        lector = csv.DictReader(archivo_csv, delimiter = ",")
        for linea in lector:
            result = sorted(lector, reverse = True, key=lambda d: float(d['total_value']))
            #print(linea["origin"], " ", linea["destination"], " ", linea["total_value"])
        
        print(result[0:10])
        
##################################################################################################

def means_transport():
    with open("synergy_logistics_database.csv", "r") as archivo_csv:
        lector = csv.DictReader(archivo_csv, delimiter = ",")
        search_dictionary = {}
        for search_data in lector:
            try:
                search_dictionary[search_data["transport_mode"]] = int(search_dictionary[search_data["transport_mode"]]) + 1
            except:
                search_dictionary[search_data["transport_mode"]] = 1

        print(search_dictionary)
        
##################################################################################################

def total_value():
    
    with open("synergy_logistics_database.csv", "r") as archivo_csv:
        lector = csv.DictReader(archivo_csv, delimiter = ",")
        a = sum(int(linea["total_value"]) for linea in lector)/19056
        #print(a)
        with open("synergy_logistics_database.csv", "r") as archivo_csv:
          lector = csv.DictReader(archivo_csv, delimiter = ",")
          l = []
          lista = []
          for b in lector:
              if int(b["total_value"]) >= a:
                #print(b["origin"])
                l.append(b["origin"])
              elif int(b["total_value"]) >= a:
                #print(b["destination"])
                l.append(b["origin"])
          lista = list(set(l))
          print(lista)
main()