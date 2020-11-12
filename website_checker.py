import requests
import re
import datetime


regex_title_match = '.*?<title.*?>(.+?)</title>'
pattern = re.compile(regex_title_match)


row = {}
row['response_time'] = None
row['error_code'] = None
row['content_found'] = False
row['time_stamp'] = datetime.datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")


def check(website, website_title):
	try:

		response = requests.get(website)
		row['response_time'] = response.elapsed.total_seconds()

		if 200 == response.status_code:
			match = pattern.match(response.text)
			row['content_found'] = website_title == match.groups(0)[0]
		else:
			row['error_code'] = response.status_code


	except requests.ConnectionError:
		print('Could not reach website', website)

	return row
