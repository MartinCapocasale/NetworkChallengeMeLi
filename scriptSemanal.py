import scriptBackup
import schedule
import time

def semanal():
 schedule.every().sunday.do(scriptBackup.backup)


 while True:
     print ("Se generara un backup el dia domingo...")
     schedule.run_pending()
     time.sleep(1)


 print ("Script Backup-Semanal del dia domingo Terminado")