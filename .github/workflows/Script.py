import random
import time
from datetime import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Configuración de Google Sheets
scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

spreadsheet = client.open("Nombre-de-tu-Hoja")
worksheet = spreadsheet.sheet1

while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    glucose = random.randint(50, 400)
    worksheet.append_row([timestamp, glucose])
    print(f"[{timestamp}] Glucosa: {glucose} mg/dL - Guardado en Google Sheets")
    time.sleep(300)
