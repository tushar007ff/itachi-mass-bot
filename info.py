import os
import time

class Config(object):
    # Pyrogram Client
    API_ID    = int(os.environ.get("API_ID", "17763538"))  # ⚠️ Required
    API_HASH  = os.environ.get("API_HASH", "babad31b4b434fc53d8bd13370c556c3") # ⚠️ Required
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8190350217:AAFPBQoEK96Dkg7ILHM9louqXLt6c8SOJUs") # ⚠️ Required
    
    # Other Configs
    BOT_START_TIME = time.time()
    OWNER    = int(os.environ.get("OWNER", "7507408570"))  # ⚠️ Required
    SUDO = list(map(int, os.environ.get("SUDO", "7538572906 6636904611").split()))  # ⚠️ Required
    # Web Response Config
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))

class Txt(object):

    SEND_NUMBERS_MSG = """
❪ SEND THE TOTAL NUMBER YOU HAVE ❫

☛ How many Number do You have
"""

    SEND_TARGET_CHANNEL = """
( SEND THE TARGET CHANNEL LINK or USERNAME)

☛ For e.g :- <code> @ </code> or <code> https:/t.me/its_innocent_boy_2926 </code>
"""

    SEND_SESSION_MSG = """
❪ SEND SESSOIN STRING ❫

☛ Generate Session String form @


"""

    SEND_API_ID = """
❪ SEND API ID ❫

☛ Api_id Get from my.telegram.org
"""
    SEND_API_HASH = """
❪ SEND API HASH ❫

☛ Api_hash Get from my.telegram.org
"""

    MAKE_CONFIG_DONE_MSG = """
Your {} accounts has been added 👥

And Logined to the Target Channel/Group to Report it. ✅

➜ Click the button bellow to see the Number of Telegram account you added.
"""

    ADDED_ACCOUNT = """
Your have added {} accounts 👥

➜ Click the button bellow to see the More Info of the Telegram accounts which you haved added.
"""

    ACCOUNT_INFO = """
<b> Name :- </b> <code> {0} </code>
<b> User Id :- </b> <code> {1} </code>
"""

    REPORT_CHOICE = """
❪ SELECT REASON FOR REPORT 👤 ❫

1. Report for child abuse
2. Report for copyrighted content
3. Report for impersonation
4. Report an irrelevant geogroup
5. Report an illegal durg
6. Report for Violence
7. Report for offensive person detail
8. Reason for Pornography
9. Report for spam

Whats your  reason: select 1-9 👇 
"""

    SEND_NO_OF_REPORT_MSG = """
❪ SELECT NUMBER OF REPORTS 👤 ❫

**Send Number of reports which you want to report to this @{}**

The bot will keep reporting to target channel or group until it's reach the number of report. 🎯
"""

    START_MSG = """
𝐚𝐥𝐥𝐞 {},🙈\n\n👉 𝐓𝐇𝐈𝐒 𝐈𝐒 𝐀 𝐏𝐎𝐖𝐄𝐑𝐅𝐔𝐋𝐋 𝐌𝐀𝐒𝐒 𝐑𝐄𝐏𝐎𝐑𝐓𝐈𝐍𝐆 𝐁𝐎𝐓😁😁 𝐓𝐇𝐈𝐒 𝐈𝐒 𝐁𝐀𝐒𝐄𝐃 𝐎𝐑 𝐋𝐀𝐓𝐄𝐒𝐓 𝐋𝐈𝐁𝐑𝐀𝐑𝐈𝐄𝐒 𝐀𝐍𝐃 𝐓𝐇𝐄 𝐈𝐃𝐄𝐀 𝐎𝐅 𝐑𝐄𝐏𝐎𝐑𝐓𝐈𝐍𝐆 𝐖𝐈𝐓𝐇 𝐌𝐔𝐋𝐓𝐈𝐏𝐋𝐄 𝐀𝐂𝐂𝐎𝐔𝐍𝐓𝐒😎😎.\n\n👉 𝐓𝐇𝐈𝐒 𝐁𝐎𝐓 𝐍𝐄𝐄𝐃𝐄𝐃 𝐒𝐄𝐒𝐒𝐈𝐎𝐍 𝐎𝐅 𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 𝐈𝐃𝐒 𝐓𝐎 𝐌𝐀𝐊𝐄 𝐑𝐄𝐏𝐎𝐑𝐓 𝐎𝐍 𝐓𝐇𝐄 𝐓𝐀𝐑𝐆𝐄𝐓😚😚\n\n👉 𝐓𝐇𝐈𝐒 𝐌𝐀𝐒𝐒 𝐁𝐎𝐓 𝐈𝐒 𝐑𝐄𝐏𝐑𝐄𝐒𝐍𝐓𝐄𝐃 𝐁𝐘 𝐓𝐅𝐖🦁\n\n👉 𝐓𝐎 𝐆𝐄𝐓 𝐓𝐇𝐄 𝐀𝐂𝐒𝐒𝐄𝐒 𝐎𝐅 𝐁𝐎𝐓 𝐂𝐎𝐍𝐓𝐀𝐂𝐓 𝐖𝐈𝐓𝐇 [👑𝐓𝐅𝐖 𝐀𝐃𝐌𝐈𝐍👑](https://t.me/tfw_admin)
"""

    HELP_MSG = """
🔆 HELP

📚 Available commands:
⏣ /start - check I'm alive 
⏣ /make_config - To Make Config 
⏣ /del_config - Delete the Config
⏣ /target - To see the target channel
⏣ /see_accounts - See all the accounts you added
⏣ /add_account - Add new accounts
⏣ /report - Report the target
⏣ /restart - Restart the bot

💢 Features:
► Report a single channel or group with multiple Id's
► Type of report option available
► Facilitie to change the Target Channel or Group
► Facilitie to add the multiples accounts after once you make config
► All the accounts you added will automatically joined the target channel or group
► No need to enter phone number, password or otp just send session string and that's it
► Check the server status and resources
"""

    ABOUT_MSG = """
- 𝖬𝗒 𝖭𝖺𝗆𝖾 : <a href=https://t.me/{}>{}</a>
- 𝖢𝗋𝖾𝖺𝗍𝗈𝗋 : <a href=@itzdaxx</a>
- 𝖫𝗂𝖻𝗋𝖺𝗋𝗒 : Pyrogram
- 𝖫𝖺𝗇𝗀𝗎𝖺𝗀𝖾 : 𝖯𝗒𝗍𝗁𝗈𝗇 𝟥
- 𝖣𝖺𝗍𝖺𝖡𝖺𝗌𝖾 : 𝖬𝗈𝗇𝗀𝗈𝖣𝖡
- 𝖡𝖮𝖳 𝖲𝖾𝗋𝗏𝖾𝗋 : 𝖠𝗇𝗒𝖶𝗁𝖾𝗋𝖾
"""
