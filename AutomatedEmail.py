import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint
import smtplib, ssl



def log_in_to_google_sheets():
    scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)
    client = gspread.authorize(creds)
    sheet = client.open("tutorial").sheet1
    data = sheet.get_all_records()
    return sheet

def log_in_to_google_gmail():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls() 
    s.login("email@gmail.com", "password")
    return s
    

def send_email():
    sheet = log_in_to_google_sheets()
    s = log_in_to_google_gmail()
    row = sheet.row_values(1)  
    col = sheet.col_values(1)  
    cell = sheet.cell(1,2).value
    numRows = sheet.row_count

    for i in range(1,16):
        name = sheet.cell(i,1).value
        if (name == ""):
            name = "Default Header"
        email = sheet.cell(i,2).value
        password = sheet.cell(i,3).value
        subject = 'subject'
        body = "body"
        message = f'Subject: {subject}\n\n{body}'
        s.sendmail("tayfunymz@gmail.com", "tayfunymz@gmail.com", message) 
        pprint("Sending email for... " + name)

    s.quit()

def main():
    send_email()

main()
