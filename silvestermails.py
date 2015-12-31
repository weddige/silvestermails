#!/usr/bin/env python3
__author__  = 'Konstantin Weddige'

from email.mime.text import MIMEText
from argparse import ArgumentParser
from datetime import date
from smtplib import SMTP
import json

if __name__ == '__main__':
    print('   .')
    print('   o   .')
    print(' ____.o___')
    print(' \  .    / Silvestermails')
    print('  \~~~~~/')
    print("   '-.-'   Version 2.1")
    print('     |')
    print('     |     Konstantin Weddige')
    print("   _.'._")
    print()
    parser = ArgumentParser(description='Verschickt vordefinierte Silvestermails.')
    parser.add_argument('-s', '--subject', nargs='?', default='Ein frohes neues Jahr {0}'.format(date.today().year))
    parser.add_argument('-f', '--sender', nargs='?', default='ich@domain.tld')
    parser.add_argument('-b', '--body', nargs='?', default='body.txt')
    parser.add_argument('-r', '--recipients', nargs='?', default='recipients.json')
    args = parser.parse_args()

    file = open(args.body, 'r', encoding='utf-8')
    body = file.read()
    file.close()

    recipients = open(args.recipients, 'r')
    try:
        for recipient in json.load(recipients):
            try:
                mail = MIMEText(body.format(**recipient), 'plain', 'utf-8')
            except KeyError as e:
                print('Dein Template verwendet eine nicht definierte Variable.')
                break
            mail['To'] = recipient['email']
            mail['From'] = args.sender
            mail['Subject'] = args.subject

            print(mail.as_string())

            s = SMTP('localhost')
            s.sendmail(args.sender, [recipient['email']], mail.as_string())
            s.quit()
    except OSError: #Python 3.2 kennst ConnectionRefusedError nicht
        print('Du scheinst keinen lokalen Mailserver zu haben.')
    recipients.close()
