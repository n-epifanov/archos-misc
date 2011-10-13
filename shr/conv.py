#!/usr/bin/env python

import re

index = 1
with open('asound.state') as f:
    name = "'NONAME'"
    vol = []
    for line in f:
        r = re.search('name (.*)$', line)
        if r:
            name = r.group(1)

        r = re.search('value\.?\d* (.*)$', line)
        if r:
            v = r.group(1)
            if v == 'true' or v == 'On':
                v = 1
            if v == 'false' or v == 'Off':
                v = 0

            try:
                i = int(v)
            except:
                i = 0
            vol.append(str(i))

        if line.find('}') != -1:
            sep = ','
            v = sep.join(vol)
            print '%i:%s:%i:%s' % (index, name, len(vol), v)
            name = "'NONAME'"
            vol = []
            index += 1

