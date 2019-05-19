import scriptBackup
import schedule
import time

def mensual():
 schedule.every(31).days.do(scriptBackup.backup)

 while True:
     print ("Se generara un backup el primer dia del mes...")
     schedule.run_pending()
     time.sleep(10)


 print ("Script Backup-Mensual Terminado")
