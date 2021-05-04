import requests
import time
import smtplib

def print_hi(hospital_name, week_date, age_roup, district,emailid):
    gmail_user = 'goaforhumanity@gmail.com'
    gmail_password = 'Humanity@2021'

    sent_from = gmail_user
    to = [emailid]
    subject = 'Vaccin available in {} for age group {} '.format(hospital_name,age_roup)
    body = 'Vaccin available hurry up'

    message = """\
    Subject: Hi there, Vaccin is available please register your self

    This message is sent from Python."""

    myurl = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}"
    newurl = myurl.format(district, week_date)


    # baseurl = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=151&date=11-05-2021"
    response = requests.get(newurl)
    data = response.json()
    for i in data['centers']:
        print(i)
        if i['name'] == hospital_name:
            for j in i['sessions']:
                print(j)
                if j['min_age_limit'] == age_roup:
                    print(j['min_age_limit'])
                    if j['available_capacity'] > 0:
                        print(j['available_capacity'])
                        # send mail
                        try:
                            server = smtplib.SMTP('smtp.gmail.com', 587)
                            server.starttls()
                            # server.ehlo()
                            server.login(gmail_user, gmail_password)
                            server.sendmail(sent_from, to, message)
                            server.close()
                        except :
                            print
                            'Something went wrong...'
    time.sleep(60000)






    print(response.status_code)
    print(response.json())

if __name__ == '__main__':
    # North Goa 151
    # South Goa 152
    while True:
        print_hi('Manipal Hospital', '11-05-2021', 18, '151', 'vaibhav.naik7217@gmail.com')

