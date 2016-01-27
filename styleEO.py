import urllib
import urllib2
import json
import datetime


# For the tumblr API call, we can only get 20 ID posts at a time
# Can use the offset property to run a forloop until we hit the number of posts
# associated with the account to get all post Iids

blog_content = urllib2.urlopen('http://api.tumblr.com/v2/blog/styleseatblog.tumblr.com/posts?api_key=')

data_loaded = json.load(blog_content)
data_formatted = json.dumps(data_loaded, indent=4, separators=(',', ': '))

for i in range (0, 19):
	print "\n"
	body = data_loaded["response"]["posts"][i]["body"]
	addition_info = data_loaded["response"]["posts"][i]
	print json.dumps(addition_info, indent=4, separators=(',', ': '))
	print json.dumps(body, indent=4, separators=(',', ': '))
	print "\n"
	print "\n"




