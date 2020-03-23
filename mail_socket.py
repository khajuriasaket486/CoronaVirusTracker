import smtplib, ssl
import getpass
import webscrapingTrackCoronaVirus
class EmailSocket:
    def __init__(self,uname, upass):
        self.port = 465  # Default Port for SSL...
        self.username = uname
        self.password = upass
        self.context = ssl.create_default_context()
        self.smtp_server = 'smtp.gmail.com'

    def send_to_mail(self):
        with smtplib.SMTP_SSL(host=self.smtp_server, port=self.port, context=self.context) as server:

            subject = f'Coronavirus stats in {webscrapingTrackCoronaVirus.cv.epidermic_details[0]} today!'
            body = 'Today in ' + webscrapingTrackCoronaVirus.cv.epidermic_details[0] + '\
                        \nThere is new data on coronavirus:\
                        \nTotal cases: ' + webscrapingTrackCoronaVirus.cv.epidermic_details[1] + '\
                        \nNew cases: ' + webscrapingTrackCoronaVirus.cv.epidermic_details[2] + '\
                        \nTotal deaths: ' + webscrapingTrackCoronaVirus.cv.epidermic_details[3] + '\
                        \nNew deaths: ' + webscrapingTrackCoronaVirus.cv.epidermic_details[4] + '\
                        \nTotal Recovered: ' + webscrapingTrackCoronaVirus.cv.epidermic_details[5] + '\
                        \nActive Cases: ' + webscrapingTrackCoronaVirus.cv.epidermic_details[6] + '\
                        \nSerious, critical cases: ' + webscrapingTrackCoronaVirus.cv.epidermic_details[7] + \
                        '\n\nCheck the link: https://www.worldometers.info/coronavirus/'

            try:
                server.login(uname, upass)
                message = f'subject: {subject}\n\n{body}'
                server.sendmail('Coronavirus', input('Enter Receiver\'s email: ' ), message)
                print('Email Sent!')
            except smtplib.SMTPAuthenticationError as SAE:
                print(SAE)



        # upass = getpass.getpass() # Doesnt work in pycharm console so use terminal(cmd, linux terminal or pycharm terminal).
uname = input("Enter Your Email: ")
upass = input("Enter Your Password: ")
ems = EmailSocket(uname, upass)
ems.send_to_mail()

