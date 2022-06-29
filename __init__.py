# Copyright (C) 2022  Olof Enström

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from mycroft import MycroftSkill, intent_handler
import requests

class JitsiMagicmirror(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler("StartMeeting.intent")
    def start_meeting_with_name(self, message):
        name = message.data.get("name", None)

        if name is None:
            return self.start_meeting_unspecified_name(message)

        self.__start_meeting(name)
    
    @intent_handler("EndMeeting.intent")
    def end_meeting(self, message):
        try:
            requests.get("http://localhost:8080/MMM-jitsi/dispose")
        except requests.exceptions.RequestException as err:
            self.speak_dialog("ErrorMirror")

    @intent_handler("UnspecifiedName.intent")
    def start_meeting_unspecified_name(self, message):
        response = self.get_response("Who")
        if response:
            self.__start_meeting(response) # Pass in only the name or the whole response?
    
    def __start_meeting(self, name):
        # TODO: Get contact based on name. Make request to http://localhost:8080/MMM-jitsi/start and pass the contact information
        try:
            requests.get("http://localhost:8080/MMM-jitsi/start", {"name": name})
            self.speak_dialog("StartMeeting", data={"name": name})
        except requests.exceptions.RequestException as err:
            self.speak_dialog("ErrorMirror")

def create_skill():
    return JitsiMagicmirror()

