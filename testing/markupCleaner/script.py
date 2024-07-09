import re

def cleanMarkdown(text):
    marker = "==============="
    cleaned_text = text
    start_index = text.find(marker)
    end_index = text.find(marker, start_index + len(marker))
    if start_index != -1 and end_index != -1:
        cleaned_text = text[:start_index] + text[end_index:]

    #Regexs
    linkRegex = r'\*\s+\[([^\]]*)\]\(([^)"]*)(?:\s*"([^"]*)")?\)'
    cleaned_text = re.sub(linkRegex, '', cleaned_text, flags=re.DOTALL)#Remove links

    htmlTagRegex = r'<([^<>]*)>'
    cleaned_text = re.sub(htmlTagRegex, '', cleaned_text)#Removing html tags

    extraLinesRegex = r'\n\s*\n'
    cleaned_text = re.sub(extraLinesRegex, '\n\n', cleaned_text)#Removing extra newlines
    return cleaned_text

def readFile():
    filePath = "testing/markupCleaner/test.txt"
    text = ""
    with open(filePath, "r", encoding="utf-8") as file:
        text = file.read()
    return text

def createFile(text):
    filePath = "testing/markupCleaner/cleaned.txt"
    with open(filePath, "w", encoding="utf-8") as file:
        file.write(text)

if __name__ == "__main__":
    createFile(cleanMarkdown(readFile()))