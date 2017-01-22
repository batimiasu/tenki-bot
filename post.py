#coding: UTF-8

import requests
import slackweb
import os
from bs4 import BeautifulSoup

html = requests.get('http://www.tenki.jp/radar/3/16/').content
src = BeautifulSoup(html, 'lxml').find(id='radar_image_entries').get('src')
slack = slackweb.Slack(os.environ["WEBHOOK_URL"])
slack.notify(text=src)
