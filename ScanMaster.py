import socket
from datetime import datetime
from colorama import init, Fore

init()

def port_scan(target):
    open_ports = []
    print(Fore.GREEN + f"Commence le scan sur {target}")
    start_time = datetime.now()
    
    try:
        for port in range(1, 65536):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                open_ports.append(port)
                service_name = socket.getservbyport(port, 'tcp')
                print(Fore.GREEN + f"Port {port} ouvert - Service : {service_name}")
            s.close()
    except KeyboardInterrupt:
        print(Fore.GREEN + "\nScan interrompu par l'utilisateur.")
    except socket.gaierror:
        print(Fore.GREEN + "\nAdresse IP incorrecte.")
    except socket.error:
        print(Fore.GREEN + "\nImpossible de se connecter au serveur.")
    
    end_time = datetime.now()
    total_time = end_time - start_time
    print(Fore.GREEN + f"Scan terminé en : {total_time}")
    
    if open_ports:
        print(Fore.GREEN + f"Ports ouverts détectés : {open_ports}")
        for port in open_ports:
            service_name = socket.getservbyport(port, 'tcp')
            print(Fore.GREEN + f"Port {port} (Service : {service_name}) est ouvert.")
            print(Fore.GREEN + f"- Assurez-vous que le service sur le port {port} est sécurisé.")
            print(Fore.GREEN + f"- Mettez à jour les logiciels et applications sur ce port.")
            print(Fore.GREEN + f"- Utilisez des pare-feu pour restreindre l'accès au port {port}.")
    else:
        print(Fore.GREEN + "Aucun port ouvert détecté.")


ascii_art = '''
    .--.       
   |o_o |      
   |:_/ |                   
  //   \ \    
 (|     | )   
/'\_   _/`\   
\___)=(___/      
   
'''
print(Fore.GREEN + ascii_art)

target = input(Fore.GREEN + "Entrez l'adresse IP ou le nom de domaine à scanner : ")
port_scan(target)

input(Fore.GREEN + "Appuyez sur Entrée pour fermer le programme...")