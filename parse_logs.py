import os
import gzip
import urllib
 
# Following is the directory with log files,
# On Windows substitute it where you downloaded the files
root = "/home/aromandi/logs"
keywords = "Windows", "Linux", "OS X", "Ubuntu", "Googlebot", "bingbot", "Android", "YandexBot", "facebookexternalhit"
d = {}
total = 0
users = {}
 
for filename in os.listdir(root):
    if not filename.startswith("access.log"):
        print "Skipping unknown file:", filename
        continue
    if filename.endswith(".gz"):
        continue
        fh = gzip.open(os.path.join(root, filename))
    else:
        fh = open(os.path.join(root, filename))
    print "Going to process:", filename

    for line in fh:
        total = total + 1
        try:
            source_timestamp, request, response, referrer, _, agent, _ = line.split("\"")
            method, path, protocol = request.split(" ")
            _, status_code, content_length, _ = response.split(" ")
            content_length = int(content_length) #convert response size in bytes to int
            path = urllib.unquote(path)
            #print "Response bits:", response
            #url = "http://enos.itcollege.ee" + urllib.unquote(path)
            if path.startswith("/~"):
                username, remainder = path[2:].split("/", 1)
                print "Got user:", username
                try:
                    users[username] = users[username] + content_length
                except:
                    users[username] = content_length

            for keyword in keywords:
                if keyword in agent:
                    try:
                        d[keyword] = d[keyword] + 1
                    except KeyError:
                        d[keyword] = 1
                    break # Stop searching for other keywords
        except ValueError:
            pass # This will do nothing, needed due to syntax

def humanize(bytes):
    return "%sMB" % bytes / (1024*1024)

print("Top 5 visited users:")
results = users.items()
results.sort(key = lambda item:item[1], reverse=True)
for user, transferred_bytes in results[:30]:
    print user, "==>", transferred_bytes / (1024 * 1024), "MB"
     
print "Total lines:", total
     
results = users.items()
results.sort(key = lambda item:item[1], reverse=True)
for keyword, hits in results[0:5]:
    print keyword, "==>", hits, "(", hits * 100 / total, "%)"
