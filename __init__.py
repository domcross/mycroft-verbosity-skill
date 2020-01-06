from mycroft import MycroftSkill, intent_file_handler


class MycroftVerbosity(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('verbosity.mycroft.intent')
    def handle_verbosity_mycroft(self, message):
        value = ''

        self.speak_dialog('verbosity.mycroft', data={
            'value': value
        })


def create_skill():
    return MycroftVerbosity()

