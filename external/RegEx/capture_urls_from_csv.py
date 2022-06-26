import re
import sys


def getURLsFromCsvFile(csvFile, showUnmatched='no'):
    with open(csvFile, 'r') as fh:
        data = fh.read()
    csvLines = data.split('\n')

    rePossibleWebsiteUrl = r"(?i)(([fh]t{1,2}ps?:(\/{1,2}|\\{1,2}))?(w{3}\.)?([a-z][a-z0-9-]*)(\.[a-z][a-z0-9-]*)+((\/|\\)[^\\\/\s]+)*\S?\b[\\\/]?)"
    urls = []
    unmatched_lines = []
    for i in range(0, len(csvLines)):
        if re.findall(rePossibleWebsiteUrl, csvLines[i]):
            for j in re.findall(rePossibleWebsiteUrl, csvLines[i]):
                urls.append({
                    'url': j[0],
                    'line': i+1
                })
        else:
            if csvLines[i] != '' and showUnmatched.lower() == 'showunmatched':
                unmatched_lines.append({
                    'content': csvLines[i],
                    'line': i+1
                })

    numDigitsMatchNumber = len(str(len(urls)))
    print(f'Matches ({len(urls)}/{len(csvLines)}):')
    for i in range(0, len(urls)):
        print(f'* {str(i+1).rjust(numDigitsMatchNumber, " ")} - {urls[i]["url"]} ({urls[i]["line"]})')
    
    numDigitsUnmatchedLinesNumber = len(str(len(unmatched_lines)))
    if showUnmatched == 'showUnmatched':
        print(f"\nUnmatched lines ({len(unmatched_lines)}/{len(csvLines)}):")
        for i in range(0, len(unmatched_lines)):
            print(f'* {str(i+1).rjust(numDigitsUnmatchedLinesNumber, " ")} - {unmatched_lines[i]["content"]} ({unmatched_lines[i]["line"]})')

if __name__ == '__main__':
    inputs = sys.argv
    if len(inputs) >= 2:
        inputFile = inputs[1]
        if len(inputs) == 2:
            getURLsFromCsvFile(inputFile)
        elif len(inputs) >= 3:
            showUnmatched = inputs[2]
            if showUnmatched.lower() == 'showunmatched':
                getURLsFromCsvFile(inputFile, 'showUnmatched')
            else:
                print("As second argument you can pass 'showUnmatched' to see lines that didn't have any URL or URL-like content.")
