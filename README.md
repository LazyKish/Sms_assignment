Django SMS Application with Twilio
Overview:
This project is a Django-based application that enables users to send SMS messages via Twilio. It demonstrates the integration of Twilio's messaging API with Django to provide SMS functionality seamlessly.


Basic Features
Send SMS Messages

Allow users to send SMS messages by providing the recipient's number and a message body.

How it works
pip install django twilio
django-admin startproject sms_assignment
cd sms_assigment

Setup: Install the necessary dependencies, including Django and Twilio SDK.Twilio Account Setup
Sign up at Twilio and get your:

Account SID
Auth Token
Twilio phone number
Acts as a gateway to deliver SMS messages to the recipient.

User Interface:The user provides the recipient's phone number and message through a web form or API request.

How to Run:
git clone repository https://github.com/LazyKish/Sms_assignment.git
Install Dependencies: pip install -r requirements.txt
if you already added or Set Up Twilio Credentials:  Twilio ACCOUNT_SID, AUTH_TOKEN, and TWILIO_PHONE_NUMBER and add .env file or directly into the settings.py file.

Run the Server: python manage.py runserver

Access the Application: Open your browser and go to http://127.0.0.1:8000.


