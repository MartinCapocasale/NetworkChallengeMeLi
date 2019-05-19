import scriptBackup
import schedule
import time

def diario():
 schedule.every(1).seconds.do(scriptBackup.backup)

 n = 0
 while n <= 5:
     print ("Generando backups diario...")
     schedule.run_pending()
     time.sleep(1)
     n = n+1

 print ("Script Backup-Diario Terminado")
