# Read excel and send certificate to respective person
import create
import pandas as pd
import send
import sys


EMAIL = "email@example.com"
PASSWORD = "password"


data = pd.read_excel(sys.argv[1])
names = data['Name'].tolist()
course = data['Course'].tolist()
year = data['Year'].tolist()
mail = data['Mail'].tolist()




for i in range(len(data)):
    create.make(names[i], course[i], year[i], 'template.jpg')
    print("Certificate for %s is being printed" % names[i])
    try:
        send.mail_send(names[i], mail[i], EMAIL, PASSWORD)
        print("Mail Successfully send for %s" % names[i])
    except Exception as e:
        print("An error occurred: "+str(e))
    
