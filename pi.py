from libs import command
from libs import dataloader

PI_FILE = 'addons/funkin/data/pi.txt'

class Command(command.DirectOnlyCommand, command.Config):
    '''Your daily dose of pi

**Usage**
```@Idea pi``` '''

    def __init__(self, config=None, **kwargs):
        super().__init__(config=PI_FILE, **kwargs)

    def matches(self, message):
        return " pi " in message.content.lower() or " pi" == message.content.lower()[-3:] or "pi " == message.content.lower()[:3]

    def action(self, message):
        yield from self.send_message(message.channel, self.config.content[1][int(self.config.content[0])])
        self.config.content[0]= str(int(self.config.content[0])+1)
        self.config.save()
