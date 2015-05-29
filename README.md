md-to-toc is a python script that parses a markdown file and outputs a table of contents as a markdown list.

## Usage ##

- Install Python 2.7 (haven't tested with other versions)

- Run 'md-to-toc <markdown_file>'

- Copy output to your markdown file


## Alternatives ##

[github-markdown-toc](https://github.com/ekalinin/github-markdown-toc) is a bash script that uses GitHub's API to convert a markdown file to HTML, then parses the HTML to produce the table of contents. This script is more robust than md-to-toc because it parses out the anchors directly from HTML, while md-to-toc converts the header titles to anchors using my best guess at GitHub's algorithm. The advantage to using md-to-toc is that it doesn't require an internet connection.
