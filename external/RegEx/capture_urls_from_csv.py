import re
import sys

if __name__ == '__main__':
    inputs = sys.argv

    if len(inputs) > 1:
        inputFile = sys.argv[1]

        with open(inputFile, 'r') as fh:
            data = fh.read()

        csvLines = data.split('\n')
        rePossibleWebsiteUrl = r"(?i)(([fh]t{1,2}ps?:(\/{1,2}|\\{1,2}))?(w{3}\.)?([a-z][a-z0-9-]*)(\.[a-z][a-z0-9-]*)+((\/|\\)[^\\\/\s]+)*\S?\b[\\\/]?)"
        urls = []

        for i in range(0, len(csvLines)-1):
            if re.findall(rePossibleWebsiteUrl, csvLines[i]):
                for j in re.findall(rePossibleWebsiteUrl, csvLines[i]):
                    urls.append({
                        'url': j[0],
                        'line': i+1
                    })
                    
        numDigitsMatchNumber = len(str(len(urls)))

        print(f'Matches ({len(urls)}):')
        for i in range(0, len(urls)):
            print(f'* {str(i+1).rjust(numDigitsMatchNumber, " ")} - {urls[i]["url"]} ({urls[i]["line"]})')
