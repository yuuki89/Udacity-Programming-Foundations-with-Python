import urllib

def read_text():
    quotes = open("C:\detect_profanity\movie_quotes.txt")
    contents = quotes.read()
    print(contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdyl.com/profanity?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
    if "true" in output:
        print("Profanity found")
    elif "false" in output:
        print("No profanity found")
    else:
        print("Error opening file. Is the specified path a text file?")
    
read_text()
