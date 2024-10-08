#usr/bin/python3

import requests

def number_of_subscribers(subreddit):
	"""
		Returns number of subscribers for a given subreddit
	"""
	url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
	headers = {"User-Agent": "Mozzila/5.0"}
	response = requests.get(url, headers=headers)
	if response.status_code == 200:
		data = response.json()
		return data['data']['subscribers']
	else:
		return 0


	if __name__ == '__main__':

	import sys

	if len(sys.argv) < 2:
		print("Please pass an argument for the subreddit to search.")
	else:
		print(number_of_subscribers(sys.argv[1]))
