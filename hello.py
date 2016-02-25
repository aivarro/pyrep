#!/usr/bin/python3

# Notepad++, gedit, pluma, kate, nano, vi, emacs

print("Hello world!")

for line in open("/etc/passwd"):
	if line.startswith("root") or "/bash" in line:
		print(line)
print("This line is already outside of the loop")
