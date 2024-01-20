from celery import shared_task
from time import sleep
import requests
from bs4 import BeautifulSoup
import pandas as pd
from .models import Products


@shared_task()
def fetchProductData():

    # Products.objects.create(name='ramesh', price='10000',
    #                         description="hello hello hello testing")
    print("success success")
