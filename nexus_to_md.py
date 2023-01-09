import os
import requests
from contextlib import redirect_stdout
from bs4 import BeautifulSoup

def get_soup_from_url(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')

def get_soup_from_file(filename):
    dirpath = os.path.join(os.path.dirname(__file__)) 
    subfolder = "input"
    file_to_open = os.path.join(dirpath, subfolder, filename)

    with open(file_to_open, encoding = "UTF8") as savedpage:
        soup = BeautifulSoup(savedpage, 'html.parser')
        savedpage.close()
    return soup

def get_only_mod_tags(mode, location):
    if mode == "file":
        soup = get_soup_from_file(location)
    elif mode == "url":
        soup = get_soup_from_url(location)
    else:
        raise ValueError("Use either file or url")

    raw = soup.find_all(True, {"class": ["tile-name", "desc", "realauthor"]})

    output = ""
    for element in raw:
        output += element.prettify()

# produces an intermediate file with the results of the find all + prettification
# Might be useful for debugging if the script is choking on some unexpected tags
    with open('steptwo.html', 'w', encoding = "UTF-8") as o:
        with redirect_stdout(o):
            print(output)
            o.close()

def class_is_tile_name(tag):
    return str(tag['class']).__eq__(('[\'tile-name\']'))

def class_is_desc(tag):
    return str(tag['class']).__eq__(('[\'desc\']'))

def class_is_realauthor(tag):
    return str(tag['class']).__eq__(('[\'realauthor\']'))
        
def filter_tags(raw):
    modnames = set()
    descs = set()

    for tag in raw:
        if "b" in tag.name:
            continue
        elif tag.name == "a":
            modname = tag.contents[0].strip()
            if modname not in modnames:
                modnames.add(modname)
                print(f"[**{modname}**]({tag['href']})", end="")

        elif class_is_realauthor(tag):
            print(f" by {tag.contents[2].strip()}  ")

        elif tag.name == "p" and class_is_desc(tag):
            desc = tag.contents[0].strip()
            if desc not in descs:
                descs.add(desc)
                print(f"{desc}  \n")

def convert_tags_to_markdown(output_file_name):
    # Target format: markdown
    # * [**NAME**](URL) by AUTHOR  \n
    # DESC  \n\n

    file_to_open2 = os.path.join(os.path.dirname(__file__), 'steptwo.html')

    with open(file_to_open2, encoding = "UTF8") as steptwo:
        modsoup = BeautifulSoup(steptwo, 'html.parser')
        raw = modsoup.find_all(True)

        filter_tags(raw)

        output_file_name = output_file_name + ".md"

        output_path = os.path.join(os.path.dirname(__file__), "output", output_file_name)

        with open(output_path, 'w', encoding = "UTF-8") as o2:
            with redirect_stdout(o2):
                filter_tags(raw)
                o2.close()

## USER INPUT SECTION ##

# mode you want to use (file or url), name of the file to convert (needs to be in input folder)
get_only_mod_tags("file", "newthisweek.html")
# type the name you want the output file to have. Script will add .md automatically
convert_tags_to_markdown("week9jan")