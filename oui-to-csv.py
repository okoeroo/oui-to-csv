#!/usr/bin/env python3

import sys
import requests


url_oui = "http://standards-oui.ieee.org/oui.txt"
try:
    oui_data = requests.get(url_oui).text
except:
    print("Error: can't download the OUI file")
    sys.exit(1)


with open('oui.csv', 'w') as f:
    for line in oui_data.splitlines():
        if "(base 16)" in line:
            split_line = line.split()
            oui = split_line[0]
            company_name = " ".join(split_line[3:])
            print(f"\"{oui}\",\"{company_name}\"")
            f.write(f"\"{oui}\",\"{company_name}\"")
