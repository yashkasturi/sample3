from PIL import Image
import requests

def af(c,e):

		url = c
		try:
			resp = requests.get(url, stream=True).raw
		except requests.exceptions.RequestException as e:  
			sys.exit(1)
		try:
			img = Image.open(resp)
		except IOError:
			print("Unable to open image")
			sys.exit(1)
		img.save('static/images/after.jpg', 'jpeg')
		url = e
		try:
			resp = requests.get(url, stream=True).raw
		except requests.exceptions.RequestException as e:  
			sys.exit(1)
		try:
			img = Image.open(resp)
		except IOError:
			print("Unable to open image")
			sys.exit(1)
		img.save('static/images/before.jpg', 'jpeg')