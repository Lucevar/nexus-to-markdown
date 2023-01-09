## Nexus To Markdown

Quick and not very elegant utility script that converts a page of Nexus search results into markdown-formatted links with blurbs ready for use in mod lists.

eg:
[**BDC-Seyda Neen**](https://www.nexusmods.com/morrowind/mods/51133) by Enclavekiller  
Better Dialogue-Choices is a quest overhaul project focused on implementing rpg elements in dialogue while extending quests by giving the player multiple ways to complete them. This mod overhauls all Seyda Neen side quests.  

**Installation**:

* Download code from github
* Install python3 if you don't already have it
* Install beautifulsoup4 using pip3:
```pip3 install beautifulsoup4```
* Install the requests library with pip3:
```pip3 install requests```

**Usage**:
1. Make a search on Nexus (any game)
2. Save the html file (In windows/Chrome: CTRL + S, change dropdown type to "Webpage, HTML only")
3. Save/move the html file to nexus-to-markdown/input folder. Call it whatever you want.
4. Open the nexus_to_markdown.py file in Visual Studio Code. 
    * Optionally install some python addons to highlight code etc
    * Make sure you have the modules in the Installation section installed
5. Scroll to the bottom of nexus_to_markdown.py - the section you're looking for is marked ## USER INPUT SECTION ## 
6. Change the code to point to the page you just saved
eg if you saved it in nexus-to-markdown/input/mysearchpage.html, you would change it to `get_only_mod_tags("file", "mysearchpage.html")`
Then change the next line to have the output name you want. Eg if you want the file to be mynewoutputfile.md, use this code: `convert_tags_to_markdown("mynewoutputfile")`
7. Run nexus_to_markdown.py either through the built-in interpreter in visual studio code (the python addon will include this), or in your terminal: `python3 nexus_to_md.py`
8. You should now have a new markdown-formatted list of mods in your output folder to do whatever you want with. Go forth and make lists :) 

You can also try running it with url mode, but Nexus does a lot of the search filtering stuff with javascript, and also requires you to be a logged in premium member to get 80 results per page (and I haven't figured out how to log the script in yet), so tbh the save-html method is cumbersome but easier for now. I don't want to invest too much time in this.


## Lucevar's List Helper
A little autohotkey [https://www.autohotkey.com/](https://www.autohotkey.com/) script I wrote that allows you to copy url, mod name, author, and description to a key combo and then print them out as markdown formatted mod blurbs with one key combo. 

CTRL + NUMPAD1 = url
CTRL + NUMPAD2 = name
CTRL + NUMPAD3 = author
CTRL + NUMPAD4 = description

ALT + \ = print as markdown with name, link, and author
ALT + z = print as markdown with name, link, author, and description

Workflow: Go to mod page. Highlight url. CTRL + NUM1. Highlight name. CTRL + NUM2. Highlight author. CTRL + NUM3. Highlight desc. CTRL + NUM4. Open text document. ALT + z. Ta-da, markdown!
