import urllib.request
import re

url = 'https://samparkmedelhi.com/assets/index-cx2jKWsA.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    content = urllib.request.urlopen(req).read().decode('utf-8', errors='ignore')
    matches = re.finditer(r'(?:shark|tank|youtube\.com|youtu\.be|img\.youtube)', content, re.IGNORECASE)
    for m in matches:
        start = max(0, m.start() - 80)
        end = min(len(content), m.end() + 120)
        print('SNIPPET:', content[start:end])
except Exception as e:
    print('Error:', e)
