# simple dpy HelpFormatter

A HelpFormatter for discord.ext.commands that is marginally better than the default.

## Sample output

Here's the output of various help commands for a bot of mine.

### help

Emote Manager lets you manage custom server emotes from your phone.

NOTE: Most commands will be unavailable until both you and the bot have the "Manage Emojis" permission.

**_Emotes:_**\
**list**\
A list of all emotes on this server.\
**_Jishaku:_**\
**jishaku**\
The Jishaku debug and diagnostic commands.\
**_Meta:_**\
**invite**\
Gives you a link to add me to your server.\
**support**\
Directs you to the support server.\
**_No Category:_**\
**help**\
Shows this message.

Type `@GenericBot help` command for more info on a command.\
You can also type `@GenericBot help` category for more info on a category.

### help Emotes

Commands:\
**add**\
Add a new emote to this server.\
**add-from-ec**\
Copies one or more emotes from Emote Collector to your server.
**list**\
A list of all emotes on this server.\
**remove**\
Remove an emote from this server.\
**rename**\
Rename an emote on this server.

Type `@GenericBot help` command for more info on a command.\
You can also type `@GenericBot help` category for more info on a category.

### help add-from-ec

`@GenericBot [add-from-ec|addfromec] <name> [names...]`

Copies one or more emotes from Emote Collector to your server.

The list of possible emotes you can copy is here:
https://emote-collector.python-for.life/list
