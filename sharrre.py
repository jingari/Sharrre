# encoding: utf-8

import urllib2, re

def get_count(channel=None, url=None):
	data = {
		"url": url,
		"count": 0	
	}
	if channel == "googlePlus":
		# Google did not release any public API to get +1's count at the moment,
		# there is only an URL that builds a GooglePlus widget containing a =1 button
		# and the shares count.
		# We have to parse it manually to retrieve the count...
		# See http://stackoverflow.com/questions/7403553/how-do-i-get-the-counter-of-a-google-plus-1-button
		# The returned HTML contains:
		#	...
		# 	<div id="aggregateCount" class="V1">4.6k</div>
		#	...
		# where "4.6k" is the count we are looking for.
		GOOGLEPLUS_REGEXP = r'aggregateCount".*>(?P<count>[0-9\.kK]+)<'
		GOOGLEPLUS_URL = "https://plusone.google.com/u/0/_/+1/fastbutton?url=%s&count=true"
		response = urllib2.urlopen(GOOGLEPLUS_URL % (url,), None, 10)
		raw_html = response.read()
		response.close()
		match_obj = re.search(GOOGLEPLUS_REGEXP, raw_html)
		if match_obj is not None:
			data["count"] = match_obj.groupdict()["count"]
		else:
			# If the RegExp did not match anything, the HTML has probably changed...
			data["count"] = -1

	return data