import os

while True:
    os.system('taskkill /f /im ClassM_Client_Service.exe')
    os.system('taskkill /f /im ClassM_Client.exe')