#!/usr/bin/env python

import smtplib
import xmlrpc.client
import ssl
import logging.config

ssl._create_default_https_context = ssl._create_unverified_context
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def list_test(s, logger):
    try:
        output = s.listtest(str(repr({'k': 'v1'})))
        logger.info(output)
    except Exception as e:
        logger.error("Error: " + format(str(e)))
    return output


def arg_parser(server, logger):
    port = 8443
    dest = "https://" + server + ":" + port
    s = xmlrpc.client.ServerProxy(dest)
    output = list_test(server, logger)
    return output


def health_check(logger):
    server = "svash00045ee"
    output = arg_parser(server, logger)
    if 'OK' in output:
        status = "Green"
    else:
        status = "Red"

    sender = "sender@gmail.com"
    recipient = "receiver@gmail.com"
    recipient_cc = "cc_receiver@gmail.com"
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Health Check"
    msg['From'] = sender
    msg['To'] = recipient
    msg['Cc'] = recipient_cc

    text = " "
    html = """
    <html>
        <head>
            <style>
                table {
                    font-family: arial, sans-serif;
                    border-collapse: collapse;
                    width: 100%
                }
                td, th {
                    border: 1px solid #000000;
                    text-align: left;
                    padding: 8px;
                }
            </style>
        </head>
        <body>
            <p>Dear Team,</p>
            <p>Find below health check report:</p>
            <table style='width:100%'>
                <tr style="background-color:#205385; color:#ffffff; font-weight:bold">
                    <th>Env</th>
                    <th>Status</th>
                    <th>Version</th>
                </tr>
                <tr>
                    <td>EE</td>
                    <td>""" + status + """</td>
                    <td>x.y.z</td>
                </tr>
            </table>
            <p>Regards, <br>
            NPA Team
            </p>
        </body>
    </html>"""
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)

    s1 = smtplib.SMTP('localhost')
    s1.sendmail(sender, recipient.split(',') + recipient_cc.split(','), msg.as_string())
    s1.quit()
    logger.info("Mail sent successfully")


if __name__ == "__main__":
    logging.config.fileConfig(LOGCONFFILE)
    logger = logging.getLogger('alert.npa.healthcheck')
    health_check(logger)
