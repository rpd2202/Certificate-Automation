#########Certificate-Automation ###############################

Hi Guy this is a Simple automation for generating and sending the certificates through mail.
Here I have a template.jpg that is the template for the certificate.
and name.xlsx where every participants name,course,year,mail id is filled in a particular format.

How to Run?

Install the Required packages:
Linux : python3 -m pip install -r requirements.txt
Windows : python -m pip install -r requirements.txt

NOTE: For testing purpose i have used local main smtpd server if you want to run in a production environment change the sender email, and password in main.py 
and remove comment server.login() and change host and port number accordingly.

Local host a smptd server:
Linux: sudo python3 -m smtpd -c DebuggingServer -n localhost:1025
Windows: python -m smtpd -c DebuggingServer -n localhost:1025

To run:
python3 main.py name.xlsx

here name.xlsx is excel file 
