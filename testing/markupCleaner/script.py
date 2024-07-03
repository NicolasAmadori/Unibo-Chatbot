def cleanMarkdown(text):
    start_marker = "Questo sito web utilizza i cookie"
    end_marker = "Informazioni sul sito e accessibilità"

    start_index = text.find(start_marker)
    end_index = text.find(end_marker)
    print(start_index, end_index)
    if start_index == -1 or end_index == -1:
        return text

    end_index += len(end_marker)
    cleaned_text = text[:start_index] + text[end_index:]
    
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