from telethon.sync import TelegramClient, events
import configparser
from telethon import utils
import time

# Setting configuration values
api_id = 'API ID'
api_hash = 'YOUR HASH'

api_hash = str(api_hash)

phone = 'PHOEN NUMBER'
username = 'USERNAME'

news_papers = ['Editorial-Business Standard',
 'The-Hindu',
 'Editorial-Indian-Express',
 'Editorial-The-Hindu',
 'Indian Express']

while True:
	with TelegramClient('anuj',api_id,api_hash) as client:
		messages = client.get_messages('https://t.me/UpscMaterials',limit=10000)
		print('messages no: ',len(messages))
		count = 0
		required_files = 0
		exception_count = 0

		for msg in messages:
			count +=1
			try:
				pdf_name = msg.media.document.attributes[0].file_name
			except:
				exception_count +=1
				continue
			for x in news_papers:
				if x in pdf_name:
					print('message no: ',count,msg.media.document.attributes[0].file_name)
					required_files +=1
					if count%2000 == 1 or count%2000 == 2:  #this condition allowed to download atmax 2 files.
						client.download_media(msg)
						break
			count +=1
	print('Total messaged :', count)
	print('required files: ', required_files)
	print('Other messages :', exception_count)
	time.sleep(120)



client.run_until_disconnected()
    
 