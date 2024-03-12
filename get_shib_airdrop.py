# GET shib airdrop

import time
from telethon import TelegramClient, events, sync

import os
from os.path import join, dirname
from dotenv import load_dotenv
load_dotenv()

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
# cp .env.example .env
# fill your configuration
YOUR_TG_API_ID = os.environ.get("YOUR_TG_API_ID")
YOUR_TG_API_HASH = os.environ.get("YOUR_TG_API_HASH")

client = TelegramClient(
	'AirdropClient',
	YOUR_TG_API_ID,
	YOUR_TG_API_HASH,
	# config the proxy if you are Chinese user
	proxy=('socks5', '127.0.0.1', 7890)
)
client.start()

while True:
	client.send_message(
		'https://t.me/OfficialShibaAirdropBot',
		'🎁 Hourly Bonus'
	)

	# ♻️ Come back: 6.0 hours later(💸 it's free)
	time.sleep(6*3600)
