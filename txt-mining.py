# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:38:18 2018

@author: DAMI
"""

import csv
import re

with open ("dates.txt") as out:
    reader = csv.reader(out)
    text = out.readlines()

formatted_dates = []
for j in text:
    regex2 =  re.findall(r'\d{2}[/-]\d{2}[/-]\d{2,4}',str(j)) or re.findall(r'(?:\d{2} )(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* (?:\d{2}, )?\d{4}',str(j))
    if regex2 == []:
        pass
    else:
        formatted_dates.append(regex2)    
print(formatted_dates)

        
        