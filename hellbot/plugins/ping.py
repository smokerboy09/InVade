import asyncio
import datetime

from . import *

@bot.on(hell_cmd(pattern="ping$"))
@bot.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def pong(hell):
    if hell.fwd_from:
        return
    start = datetime.datetime.now()
    event = await eor(hell, "`·.·★ 𝐏𝐈𝐍𝐆 ★·.·´")
    end = datetime.datetime.now()
    ms = (end - start).microseconds / 1000
    await event.edit(
        f"╰•★★ 𝐏𝐎𝐍𝐆 ★★•╯\n\n    ✨  `{ms}`\n    ✨  __**𝐎𝐖𝐍𝐄𝐑**__ **:**  {hell_mention}"
    )


CmdHelp("ping").add_command(
  "ping", None, "Checks the ping speed of your Hêllẞø†"
).add_warning(
  "✅ Harmless Module"
).add()

# hellbot
