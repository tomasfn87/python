import sys
import re


if __name__ == '__main__':
    inputs = sys.argv

    if len(inputs) > 1:
        input_file = sys.argv[1]

        with open(input_file, 'r') as fh:
            data = fh.read()

        re_possible_website_url = r"(?i)((ht{1,2}ps?:(\/{1,2}|\\{1,2}))?(w{3}\.)?([a-z][a-z0-9-]+\.)+([a-z][a-z0-9-]+)((\/|\\)[^,\'\"\s\[\]\(\)\{\}]*)*\/?)"
        urls = re.findall(re_possible_website_url, data)
        n_urls = len(str(len(urls)))

        print('Total matches:', len(urls))
        for i in range(0, len(urls)):
            print(f'- {str(i+1).rjust(n_urls, "0")} - {urls[i][0]}')
