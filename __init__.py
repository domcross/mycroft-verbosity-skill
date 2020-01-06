# Copyright 2020, domcross
# Github https://github.com/domcross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from mycroft import MycroftSkill, intent_file_handler
from mycroft.messagebus.message import Message

class MycroftVerbosity(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('set.verbosity.intent')
    def handle_verbosity_mycroft(self, message):
        if message.data.get("verbosity"):
            verbosity = message.data.get("verbosity").lower()
        else:
            self.speak_dialog('error.verbosity', data=None)
            return
        verbosity_values = self.translate_namedvalues('verbosity.value')
        if verbosity in verbosity_values:
            self.bus.emit(Message("mycroft.debug.log", data={
                'level': verbosity_values[verbosity]
            }))
            self.speak_dialog('verbosity', data={
                'verbosity': verbosity
            })
        else:
            self.speak_dialog('error.verbosity', data=None)


    @intent_file_handler('set.loglevel.intent')
    def handle_loglevel_mycroft(self, message):
        if message.data.get("loglevel"):
            loglevel = message.data.get("loglevel").lower()
        else:
            self.speak_dialog('error.loglevel', data=None)
            return
        loglevel_values = self.translate_namedvalues('loglevel.value')
        self.log.debug("loglevel_values {}".format(loglevel_values.keys()))
        if loglevel in loglevel_values:
            self.bus.emit(Message("mycroft.debug.log", data={
                'level': loglevel_values[loglevel]
            }))
            self.speak_dialog('loglevel', data={
                'loglevel': loglevel
            })
        else:
            self.speak_dialog('error.loglevel', data=None)


def create_skill():
    return MycroftVerbosity()

