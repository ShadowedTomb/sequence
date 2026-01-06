import os
from os import environ

TG_BOT_TOKEN = os.environ.get("BOT_TOKEN", "8599916340:AAFMrjig6vxfHHKt8m6VJBjr3y5bz046C2s")
APP_ID = int(os.environ.get("APP_ID", "22460191"))
API_HASH = os.environ.get("API_HASH", "c4be3756a8351d7f89f2195e921aea52")
OWNER_ID = int(os.environ.get("OWNER_ID", "7984224708"))
MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://JeffyBackUp:JeffyBackUp@cluster0.hgbjdhr.mongodb.net/?retryWrites=true&w=majority")
PORT = os.environ.get("PORT", "8080")
DB_URL = os.environ.get("DB_URI", "-1003510304245")
DB_NAME = os.environ.get("DB_NAME", "ShadowedTomb")
BOT_USERNAME = os.environ.get("BOT_USERNAME", "advsequencebot")
FSUB_PIC = os.environ.get("FSUB_PIC", "https://i.ibb.co/BH8xmrn0/x.jpg")
START_PIC =os.environ.get("START_PIC", "https://i.ibb.co/YTFw6xxC/x.jpg")
START_MSG = os.environ.get("START_MSG", "<b>Sᴇɴᴘᴀɪ...!!!{mention}</b> \n<blockquote><b><i>Exᴘᴇʀɪᴇɴᴄᴇ ᴛʜᴇ ꜰᴀꜱᴛᴇꜱᴛ ᴡᴀʏ ᴛᴏ ᴏʀɢᴀɴɪᴢᴇ ʏᴏᴜʀ ᴄᴏɴᴛᴇɴᴛ. ɪ ꜱᴘᴇᴄɪᴀʟɪᴢᴇ ɪɴ ꜱᴇᴀᴍʟᴇꜱꜱ ꜰɪʟᴇ ꜱᴇQᴜᴇɴᴄɪɴɢ. ᴇꜰꜰɪᴄɪᴇɴᴄʏ, ʀᴇᴅᴇꜰɪɴᴇᴅ.</i></b></blockquote>")
ABOUT_TXT = os.environ.get("ABOUT_MESSAGE", "<i><b><blockquote>✧ ᴄʜᴀɴɴᴇʟ: <a href=https://t.me/ShadowedTomb>ꜱʜᴀᴅᴏᴡᴇᴅ ᴛᴏᴍʙ</a>\n✧ ᴏᴡɴᴇʀ: <a href=https://t.me/ShadowedTomb>ꜱʜᴀᴅᴏᴡᴇᴅ ᴛᴏᴍʙ</a>\n✧ ᴅᴇᴠᴇʟᴏᴘᴇʀ: <a href='https://t.me/name_huh'>ᴺᴬᴹᴱ ᴴᵁᴴ</a>\n✧ ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>ᴍᴏɴɢᴏ </a></blockquote></b></i>")
HELP_TXT =  os.environ.get("HELP_MESSAGE", "ᴀʀᴀ.. ᴀʀᴀ... {mention} Sᴇɴᴘᴀɪ \n<blockquote expandable><b><i>ɪ'ᴍ ᴀ ꜰɪʟᴇ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ᴅᴇꜱɪɢɴᴇᴅ ꜰᴏʀ ᴘᴜʙʟɪᴄ ᴜꜱᴇ. ɪ ᴄᴀɴ ᴏʀɢᴀɴɪᴢᴇ ᴀɴᴅ ꜱᴇQᴜᴇɴᴄᴇ ʏᴏᴜʀ ꜰɪʟᴇꜱ, ᴀɴᴅ ᴇᴠᴇɴ ᴛʀᴀɴꜱꜰᴇʀ ᴛʜᴇᴍ ᴛᴏ ᴀ ᴅᴇꜱɪɢɴᴀᴛᴇᴅ ᴅᴜᴍᴘ ᴄʜᴀɴɴᴇʟ.. </i></b></blockquote>")
TG_BOT_WORKERS = 10000
FSUB_LINK_EXPIRY = 300
DATABASE_CHANNEL = int(os.environ.get("DATABASE_CHANNEL", "-1003534870861"))
LOG_FILE_NAME = "sequence-bot.log"
SEASON_PATTERN = r'[Ss](\d{1,2})'
EPISODE_PATTERN = r'[Ee][Pp]?(\d{1,3})'
QUALITY_PATTERN = r'(480p|720p|1080p|HDRip|2k|4k)'

TEMP_DIR = "temp_files"
if not os.path.exists(TEMP_DIR):
    os.makedirs(TEMP_DIR)

SORTING_MODES = {
  'Quality': lambda x: (x['quality_order']),
  'All': lambda x: (x['season'], x['episode'], x['quality_order']),
  'Episode': lambda x: (x['episode']),
  'Season': lambda x: (x['season'])
}
QUALITY_ORDER = {
  '480p': 1,
  '720p': 2,
  '1080p': 3,
  'HDRip': 4,
  '2k': 5,
  '4k': 6,
  'unknown': 7
}
