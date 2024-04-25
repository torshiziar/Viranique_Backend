import requests
from celery import shared_task
from celery.utils.log import get_task_logger
import logging
from .utils import Util
from automation.melipayamak import Api

logger = get_task_logger(__name__)
logger1 = logging.getLogger('django')


@shared_task(name="send_verify_email")
def send_verify_email(data):
    logger.info("sent feedback email")
    return Util.send_email(data)


@shared_task(name="send_register_email")
def send_register_email(data):
    logger.info("sent register email")
    return Util.send_email_2(data)


@shared_task(name="send_verify_sms")
def send_verify_sms(phone, link):
    # data = {'from': '50004001927031', 'to': [phone], 'text': link, 'udh': ''}
    # response = requests.post('https://console.melipayamak.com/api/send/advanced/fe0dc37dac1c4ebebde2f5a49a54b5e2',
    #                          json=data)
    
    # print(response.json())


    #===== !!!! NEW CODE FOR sending SMS !!!!====================
    logger1.info("Before send SMS create User")
    username = '09391927031'
    password = 'f637h2'
    api = Api(username,password)

    sms = api.sms()
    _from = '50004001927031'
    text = link
    response = sms.send(phone,_from,text)
    logger1.info("After sent SMS create User")

    #================================================================



    
