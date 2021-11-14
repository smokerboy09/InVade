from telethon import events
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User
from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from . import *

#-------------------------------------------------------------------------------

hell_pic = Config.ALIVE_PIC or "https://telegra.ph/file/a93f8e4354f2eef4e3dbe.png"
alive_c = f"""  🔺 ╔═══╗                   ╔═══╗ 🔺  
╔══🔥🔥  sмσкεя вσт  🔥🔥══╗
 🔻╚═══╝                   ╚═══╝ 🔻

 ┏━━━━━━━━━━━━━━━━
 ┣ ✪ 🅼**ᴀꜱᴛᴇʀ** ✪
 ┣
 ┣『 {hell_mention} 』
 ┣
 ┗━━━━━━━━━━━━━━━━  
┏━━━━━━━━━━━━━━━━
┣ ➤ **𝐓ᴇʟᴇᴛʜᴏɴ 𝐕ᴇʀꜱɪᴏɴ** 
┣      ┗ ⌜{tel_ver}⌟
┣━━━━━━━━━━━━━━━━
┣ ➤ **𝐒ᴍᴏᴋᴇᴇ 𝐕ᴇʀꜱɪᴏɴ**
┣      ┗ ⌜{hell_ver}⌟
┣━━━━━━━━━━━━━━━━
┣ ➤ **𝐒ᴜᴅᴏ** 
┣      ┗ ⌜{is_sudo}⌟
┣━━━━━━━━━━━━━━━━
┣ ➤ **𝐂ʜᴀɴɴᴇʟ** 
┣      ┗  ⌜ [ᴊᴏɪɴ](https://t.me/CHATWITHFRIENDSS0) ⌟
┣━━━━━━━━━━━━━━━━
┣ ➤ **[𝐂ʀᴇᴀᴛᴏʀ]**(Https://t.me/Maratha_op)
━━━━━━━━━━━━━━━━
"""

# MADE BY TECHNO PRO ( @MARATHA_OP ) 🥺🥺

# @MARATHA_OP is Piro 🥺😂

#hmm....

#-------------------------------------------------------------------------------

@bot.on(hell_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def up(hell):
    if hell.fwd_from:
        return
    await hell.get_chat()
    await hell.delete()
    await bot.send_file(hell.chat_id, hell_pic, caption=alive_c)
    await hell.delete()

msg = f"""
**⚡ 𝕊𝕄𝕆𝕂𝔼ℝ𝔹𝕆𝕋 𝕀𝕊 𝕆ℕ𝕃𝕀ℕ𝔼⚡**
{Config.ALIVE_MSG}

**🏅 𝙱𝚘𝚝 𝚂𝚝𝚊𝚝𝚞𝚜 🏅**
**𝕋𝔼𝕃𝔼𝕋ℍ𝕆ℕ :**  `{tel_ver}`
**😈𝕊𝕄𝕆𝕂𝔼ℝ𝔹𝕆𝕋😈  :**  **{hell_ver}**
**𝔸𝔹𝕌𝕊𝔼    :**  **{abuse_m}**
**𝕊𝕌𝔻𝕆      :**  **{is_sudo}**
"""

botname = Config.BOT_USERNAME

@bot.on(hell_cmd(pattern="smoker$"))
@bot.on(sudo_cmd(pattern="smoker$", allow_sudo=True))
async def hell_a(event):
    try:
        hell = await bot.inline_query(botname, "alive")
        await hell[0].click(event.chat_id)
        if event.sender_id == ForGo10God:
            await event.delete()
    except (noin, dedbot):
        await eor(event, msg)


CmdHelp("alive").add_command(
  "alive", None, "Shows the Default Alive Message"
).add_command(
  "smoker", None, "Shows Inline Alive Menu with more details."
).add_warning(
  "✅ Harmless Module"
).add()
