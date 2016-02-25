import os

def humanize(bytes):
    if bytes < 1024:
        return "%d B" % bytes
    elif bytes < 1024 ** 2:
        return "%.1f kB" % (bytes / 1024.0)
    elif bytes < 1024 ** 3:
        return "%.1f MB" % (bytes / 1024.0 ** 2)
    else:
        return "%.1f GB" % (bytes / 1024.0 ** 3)

for filename in os.listdir("."):
    mode, inode, device, nlink, uid, gid, size, atime, mtime, ctime = os.stat(filename)
    print filename, humanize(size)

