# NetworkChallengeMeLi

Dada una infraestructura LAN con equipos Switches Cisco, se genera Script en lenguaje python para que realice backups
sobre los equipos guardando los mismos de forma centralizada en directorios. Se debera generar 5 scripts diarios,
1 script semanal y un script mensual. 

Herramientas Utilizadas:
- Lenguaje Python 2.7
- GNS3
- Docker Network_Automation 

Se procede a pensar la siguente solucion al problema teniendo en cuenta la periodicidad y un script para realizar un descubrimiento
de la red en busca de nuevos equipos conectados.


Se crea modelo en GNS3 utilizando el docker Network_Automation Appliance https://docs.gns3.com/appliances/network_automation.html
