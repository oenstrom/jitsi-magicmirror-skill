from mycroft import MycroftSkill, intent_handler


class JitsiMagicmirror(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_handler('magicmirror.jitsi.intent')
    def handle_magicmirror_jitsi(self, message):
        self.speak_dialog('magicmirror.jitsi')


def create_skill():
    return JitsiMagicmirror()

