# -*- coding: utf-8 -*-
"""
Created on Wed May 23 21:56:21 2018

@author: 14flash
"""

from libs import command
import re

class Command(command.ErrorlessCommand):
    '''Replies with a specific image

Anyone who uses this is worse than the disease

**Usage**
```<conjugated get> cancer```
Where
**`<conjugated get>`** is a valid verb tense of "get" '''

    def matches(self, message):
        return re.search(r'\b(gave\sme|gives\sme|get|gets|got)\scancer\b', message.content, re.I)

    def action(self, message):
        yield from self.send_message(message.channel, 'https://i.imgur.com/km8vp8v.png')
