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
from mycroft.skills.api import SkillApi
from mycroft.messagebus import Message

class JitsiMagicmirror(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)
    
    def initialize(self):
        self.contacts_skill = SkillApi.get("contacts-skill")
        self.add_event("jitsi-magicmirror-skill:call", self.handle_call_event)
        self.add_event("jitsi-magicmirror-skill:hangup", self.handle_hangup_event)
    
    def handle_call_event(self, message):
        """Request to make a call received over messagebus."""
        data = message.data
        if data.get("name") is None or data.get("email") is None or data.get("phone") is None:
            return
        self.__emit_call(data)
    
    def handle_hangup_event(self, message):
        """Request to hang up the call received over messagebus."""
        self.__emit_hangup()

    @intent_handler("StartMeeting.intent")
    def start_meeting_with_name(self, message):
        name = message.data.get("name", None)

        if name is None:
            return self.start_meeting_unspecified_name(message)

        self.__start_meeting(name)
    
    @intent_handler("EndMeeting.intent")
    def end_meeting(self, message):
        self.__emit_hangup()

    @intent_handler("UnspecifiedName.intent")
    def start_meeting_unspecified_name(self, message):
        response = self.get_response("Who")
        if response:
            self.__start_meeting(response)
    
    def __start_meeting(self, name):
        best_match = self.contacts_skill.get_best_match(name)
        if not best_match or len(best_match) <= 0:
            self.speak_dialog("NotFound", {"name": name})
            return
        elif len(best_match) == 1:
            contact = {"name": best_match[0][0], "email": best_match[0][1], "phone": best_match[0][2]}
        else:
            selection = self.ask_selection([x[2] for x in best_match], "WhoFromSelection")
            selected = [(name, email, phone) for (name, email, phone, score) in best_match if phone == selection]
            if len(selected) == 1:
                contact = {"name": selected[0][0], "email": selected[0][1], "phone": selected[0][2]}
            else:
                return
        if self.ask_yesno("ConfirmCall", contact) == "yes":
            self.__emit_call(contact)
    
    def __emit_call(self, contact):
        self.speak_dialog("StartMeeting", {"name": contact["name"]})
        self.bus.emit(Message(f"RELAY:MMM-jitsi2:JITSI_CALL", contact))
    
    def __emit_hangup(self):
        self.speak_dialog("EndMeeting")
        self.bus.emit(Message(f"RELAY:MMM-jitsi2:JITSI_DISPOSE"))

def create_skill():
    return JitsiMagicmirror()

