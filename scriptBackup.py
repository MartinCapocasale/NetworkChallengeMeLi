
from getpass import getpass
import netmiko
from netmiko.ssh_exception import NetMikoTimeoutException
from netmiko.ssh_exception import AuthenticationException
import re
import datetime
import os
import shutil
import time


#Creacion del  directorio raiz
if not os.path.exists("ConfiguracionesDeSwitches"):
     os.mkdir("ConfiguracionesDeSwitches")
else:
    print ("El directorio ConfiguracionDeSwitches ya fue creado")

#validacion de ip
def get_ip (input):
        return(re.findall(r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)", input))

#Leo el archivo de las ips y  creo el directorio
def get_ips (file_name):
        for line in open(file_name, "r").readlines():
                line = get_ip(line)
                for ip in line:
                        ips.append(ip)
                        if not os.path.exists("ConfiguracionesDeSwitches/"+ip):
                                os.mkdir("ConfiguracionesDeSwitches/"+ip)



#Creacion de archivos para guardar las configuraciones
def to_create(file_name, varable):
        f=open(file_name, "w")
        f.write(varable)
        f.write("\n")
        f.close()

#Lista con las ips de los equipos
ips = []

#Agrego archivo generado con el script descovery
get_ips("iplist")

#ingreso de usuario
username = raw_input("Username: ")
password = getpass()

#Conexion a un equipo
def make_connection (ip, username, password):
                return netmiko.ConnectHandler(device_type='cisco_ios', ip=ip, username=username, password=password)


def backup():
 now = datetime.datetime.now()
 filename_prefix = "cisco9300SW-backup"
 file_name = "%s_%.2i-%.2i-%i_%.2i:%.2i:%.2i" % (filename_prefix,now.day,now.month,now.year,now.hour-3,now.minute,now.second)


 #Recorro todos los equipo, intento conectarme a ellos, extraigo la configuracion y las muevo a sus respectivas carpetas
 for ip in ips:
        try:
            net_connect = make_connection(ip, username, password)
            print ("Inicio de Backup de equipo: %s " % ip)
            output = net_connect.send_command_expect("sh run")
            file = ip+"-"+file_name
            to_create(file, output)
            shutil.move(file,"ConfiguracionesDeSwitches/"+ip)
            net_connect.disconnect()

        except NetMikoTimeoutException:
             print ("TimeOut en ip: %s" % ip )
             continue
        except AuthenticationException:
             print ("Falla de autenticacion en ip: %s" % ip)
             continue
        except SSHException:
             print ("Asegurarse de tener el SSH activo en equipo")
             continue
