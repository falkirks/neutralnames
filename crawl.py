import requests
import string
urls = ['https://nonbinary.wiki/wiki/Neutral_names_starting_with_' + char for char in list(string.ascii_uppercase)]

with open("names.txt", "a") as names_file:
    for url in urls:
        r = requests.get(url)
        text = r.text.split("<span class=\"mw-headline\" id=\"The_list\">The list</span>", 1)[1].split("<span class=\"mw-headline\" id=\"See_also\">See also</span>", 1)[0]
        lines = text.split('\n')
        lines = [line.replace('</p>', '').replace('<p>', '').split('.', 1)[0] for line in lines if line.startswith('</p>') or line.startswith('<p>')]
        lines = [line for line in lines if line != '' and line != '<br />' and line != '<br/>']
        for name in lines:
            names_file.write(name + '\n')
        print(url)
