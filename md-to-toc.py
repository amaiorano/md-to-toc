# Author: Antonio Maiorano (amaiorano@gmail.com)

import os
import sys
import re

TOC_LIST_PREFIX = "-"
# TOC_LIST_PREFIX = "*"

HEADER_LINE_RE = re.compile("^(#+)\s*(.*?)\s*(#+$|$)", re.IGNORECASE)

# Dictionary of anchor name to number of instances found so far
anchors = {}

def print_usage():
	print("\nUsage: md-to-toc <markdown_file>")

def to_github_anchor(title):
	'''Converts markdown header title (without #s) to GitHub-formatted anchor'''
	
	# Convert to lower case and replace spaces with dashes
	anchor_name = title.strip().lower().replace(' ', '-')
	
	# Strip all invalid characters
	anchor_name = re.sub("[^A-Za-z0-9\-_]", "", anchor_name)
	
	# If we've encountered this anchor name before, append next instance count
	count = anchors.get(anchor_name)
	if (count == None):
		anchors[anchor_name] = 0
	else:
		count = count + 1
		anchors[anchor_name] = count
		anchor_name = anchor_name + '-' + str(count)
	
	return '#' + anchor_name
	
#TODO: Find a library that does this
def to_web_string(s):
	return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def toggles_block_quote(line):
	'''Returns true if line toggles block quotes on or off (i.e. finds odd number of ```)'''
	n = line.count("```")
	return n > 0 and line.count("```") % 2 != 0

def main(argv = None):
	if argv is None:
		argv = sys.argv

	if len(argv) < 2:
		print_usage()
		return 0

	filespec = argv[1]

	in_block_quote = False

	file = open(filespec)
	for line in file.readlines():

		if (toggles_block_quote(line)):
			in_block_quote = not in_block_quote;

		if (in_block_quote):
			continue

		m = HEADER_LINE_RE.match(line)
		if m != None:
			header_level = len(m.group(1))
			title = m.group(2)
			spaces = "  " * (header_level - 1)
			print("{}{} [{}]({})".format(spaces, TOC_LIST_PREFIX, to_web_string(title), to_github_anchor(title)))

if __name__ == "__main__":
	sys.exit(main())
