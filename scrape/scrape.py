import requests
import getopt, sys
import search
from bs4 import BeautifulSoup
from search import Novelfull

full_cmd_arguments = sys.argv;
argument_list = full_cmd_arguments[1:];
short_options = "s:e:l:hi"
long_options = ["start=", "end=", "link=", "help", "individual"]

start = ""
end = ""
link = ""
group = True;

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    print(str(err))
    sys.exit(2)

for current_argument, current_value in arguments:
    if current_argument in ("-s", "--start"):
        start = current_value;
    elif current_argument in ("-e", "--end"):
        end = current_value;
    elif current_argument in ("-l", "--link"):
        link = current_value;
    elif current_argument in ("-h", "--help"):
        print("help? HELP??")
    elif current_argument in ("-i", "--individual"):
        group = False

nf = Novelfull(link, start, end);
contentPages = nf.get_content_pages()

chapterLinks = nf.get_chapter_links(contentPages)

nf.write_chapters(chapterLinks, group)
