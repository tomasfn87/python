import sys
import re


if __name__ == '__main__':
    inputs = sys.argv

    if len(inputs) > 1:
        input_file = sys.argv[1]

        with open(input_file, 'r') as fh:
            data = fh.read()

        csv_lines = data.split(',\n')
        matches = []
        re_possible_website_url = r"(?i)((ht{1,2}ps?:(\/{1,2}|\\{1,2}))?(w{3}\.)?([a-z][a-z0-9-]+\.)+([a-z][a-z0-9-]+)((\/|\\)[^\'\"\s\[\]\(\)\{\}]*)*\/?)"
        
        for line in csv_lines:
            if re.findall(re_possible_website_url, line):
                for i in re.findall(re_possible_website_url, line):
                    matches.append(i[0])
                    
        n_match_length = len(str(len(matches)))

        print('Total matches:', len(matches))
        for i in range(0, len(matches)):
            print(f'- {str(i+1).rjust(n_match_length, "0")} - {matches[i]}')
