# <img src="https://raw.githack.com/FortAwesome/Font-Awesome/master/svgs/solid/video.svg" card_color="#1D76BA" width="50" height="50" style="vertical-align:bottom"/> Jitsi Magicmirror
Start a jitsi meeting on the magicmirror

## About
Starts a jitsi meeting on the magicmirror. Passes the contact to the mirror so they can be invited.


### Dependencies
- [MagicMirror](https://github.com/MichMich/MagicMirror)
- [MMM-jitsi2](https://github.com/oenstrom/MMM-jitsi2)
- [contacts-skill](https://github.com/oenstrom/contacts-skill)

### Events passed to the messagebus
| Event                            | When                                 | Description                                                   |
|----------------------------------|--------------------------------------|---------------------------------------------------------------|
| `RELAY:MMM-jitsi2:JITSI_CALL`    | `start.meeting` & `unspecified.name` | Pass the contact to MagicMirror to make it start the meeting. |
| `RELAY:MMM-jitsi2:JITSI_DISPOSE` | `end.meeting`                        | Tell MagicMirror to terminate the meeting.                    |


## Commands
| Intent             | sv-se            | en-us              | Description                                                                                 |
|--------------------|------------------|--------------------|---------------------------------------------------------------------------------------------|
| `start.meeting`    | *"Ring Läkaren"* | *"Call physician"* | Find the best matching contact and emit to MagicMirror to set up the call with the contact. |
| `end.meeting`      | *"Lägg på"*      | *"Hang up"*        | Emit to MagicMirror to terminate the meeting/call.                                          |
| `unspecified.name` | *"Starta möte"*  | *"Start meeting"*  | Ask for the contact to be called. Then proceed the same way as for `start.meeting.intent`.  |

## Examples
**sv-se**
* "ring Läkaren"
* "kontakta olof"
* "starta ett möte med christoffer"
* "skapa ett möte"
* "avsluta samtalet"
* "lägg på"

**en-us**
* "call physician"
* "contact olof"
* "start a meeting with christoffer"
* "create a meeting"
* "end call"
* "hang up"

## Credits
oenstrom

## Category
**Productivity**
Media
Daily

## Tags
#Jitsi
#Jitsi meet
#Video conference
#Video meeting
#Video call
#Video

