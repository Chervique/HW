import os

SCRIPT_FOLDER = os.getcwd()
SCRIPT_PATH = SCRIPT_FOLDER + "/restore.sh" #
SCRIPT_PERIOD = "*/5 * * * * "

print ("     SELECT:")
print ("1) Create backup")
print ("2) Remove backup")
USER_CHOICE = int(input("Enter number:"))

if USER_CHOICE == 1:
  os.system("sudo chmod +x "+ SCRIPT_PATH)
  os.system("sudo cp -R /etc/nginx /etc/nginx_backup")
  #os.system("sudo echo" + " '" + SCRIPT_PERIOD + SCRIPT_PATH + " '" + " > /etc/cron.d/nginx_backup")
  #os.system("sudo chmod 600 /etc/cron.d/nginx_backup")
  os.system("sudo echo" + " '" + SCRIPT_PERIOD + SCRIPT_PATH + " '" + " >> /etc/crontab")
  print ("Backup created")
elif USER_CHOICE == 2:
  os.system("sudo rm -R /etc/nginx_backup")
  #os.system("sudo rm /etc/cron.d/nginx_backup")
  #SHOULD ADD REMOVAL FOR CRONTAB
  print ("Backup deleted")
else:
 print("ERROR")
