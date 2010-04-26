#!/usr/bin/python
import sys, re, os

#pattern = r'<script language="JavaScript1\.1".*</script>\s*<div class="sr_rows\s*nobordertop ">\s*<div class="sr_lnk_box">\s*<a href="(?P<addr>/recipes/\w*)" onclick="'

#pattern = r'</script>\s*<div class="sr_rows\s*nobordertop ">\s*<div class="sr_lnk_box">\s*<a href="(?P<addr>/recipes/\w*)" onclick="'

#pattern = r'\s*nobordertop\s*">\s*<div\s*class="sr_lnk_box">\s*<a\s*href="(?P<addr>/recipes/\w*)"\s*onclick="'
#pattern = r'<div\s*class="sr_rows\s*nobordertop\s*">\s*<div\s*class="sr_lnk_box">\s*<a href="(?P<addr>/recipes/(\w|/|-)*)"\s*onclick="'
pattern = r'<div\s*class="sr_lnk_box">\s*<a href="(?P<addr>/recipes/(\w|/|-)*)"\s*onclick="'

matcher=re.compile(pattern)

def getFoodLink(search):
    """Takes in a string which is sometype of food, performs a search on Epicruious.com, returns a URL with a recipe."""
    try:
        search=search.replace(" ","\%20") #for http lookups
        os.system("wget -q http://www.epicurious.com/tools/searchresults/all?search="+search+" 2>&1 1>/dev/null")
        search = search.replace("\%20", " ") #and back
        src=open("all?search="+search)
        html = "".join([line for line in src])
        src.close()
        os.remove("all?search="+search)
        m=matcher.search(html)
        return "http://www.epicurious.com"+m.group("addr")
    except Exception:  #in case of catastrophe
        return "http://www.epicurious.com/recipesmenus/quickeasy/recipes" 

if __name__=="__main__":
    while True:
        print getFoodLink(raw_input("Food interest: \n"))
