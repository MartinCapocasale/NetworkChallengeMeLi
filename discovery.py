from netaddr import *
import os, sys

#Ejemplo de ejecucion >> python discovery.py 192.168.122.0/24
#Ingreso la subnet y recorro en busca de dispositivos
def discover(subnet):
    file = open("iplist","w")
    print "Escaneo de la red : %s " %subnet

    for host in IPNetwork(subnet):
        if os.system("ping -c 1 -w2 %s >> /dev/null" % host) == 0:
           print "Host %s encontrado" % host
           x = str(host)
           file.write(x + "\n")
        else:
            print "Host %s no encontrado " % host
            pass

    file.close()



subnet = sys.argv[1]
discover(subnet)
