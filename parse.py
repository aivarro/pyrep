fh = open("access.log")

# Excersises for practicing at home:
# most visited url
# most visited user agent
# most used OS

keywords = "Windows", "Linux", "OS X", "Android", "Linux", "Ubuntu", "Googlebot", "facebookexternalhit", "bingbot", "YandexBot"
d = {}

total = 0

for line in fh:
	total = total + 1
	try:
		source_timestamp, request, response, _, _, agent, _ = line.split("\"")
		method, path, protocol = request.split(" ")
		for keyword in keywords:
			if keyword in agent:
				d[keyword] = d.get(keyword, 0) + 1
				break

#		print "URL: http://enos.itcollege.ee" + path
#		print "agent:", agent
#		print "--"
	except ValueError:
		pass
#		print "Failed to parse:", line



total = sum(d.values())
print "Total lines with requested keywords:", sum(d.values())

#l.sort(key = lambda t:t[1], reverse=True)#python3
#l.sort(key = lambda (key, hits):-hits)#won't work in python

for key, value in sorted(d.items(), key = lambda (keyword,hits):hits, reverse=True):
#	print key, "==>", value, "(", value * 100 / total, "%)"
	print "%s => %d (%.02f%%)" % (key, value, value * 100.0 / total)
