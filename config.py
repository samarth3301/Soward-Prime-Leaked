MAIN_COLOR = 0x2f3136  #Main colour for bot's embed
RED_COLOR = 0xFF0000  #Red colour for error embeds

#EMOJI'S FOR BOT

EMOJIS = {
    'loading': '<a:swrdldmijg:1017405092321824799>',
    'tick_yes': '<:ri8:1038487759750438912>',
    'tick_no': '<:Wrong:1017402708703064144>',
    'reaction': '<:ModulesEmoji:1021050609010479154>',
}

SUPPORT_SERVER_LINK = "https://discord.gg/caQgKh2DVA"

import time
import os
from dotenv import load_dotenv
load_dotenv()


BOT_TOKEN = os.environ.get("TOKEN") 
BOT_TOKEN_BETA = os.environ.get("TOKEN_BETA") 

MONGO_DB_URL = os.environ.get("MONGO") 
MONGO_DB_URL_BETA = os.environ.get("MONGO_BETA")  # database for the beta bot (optional)
DB_UPDATE_INTERVAL = 300  # the interval at which the database is updated

PREFIX = "?"  # the default prefix for the bot
OWNERS = []  # the bot owners
COOLDOWN_BYPASS = []  # the users that bypass the cooldown
 # the id of the epicbot guild
PREMIUM_GUILDS = [746202728031584358, 749996055369875456, 876751925859725332]  # the ids of the premium guilds (it bypasses some cmd requirements)

# AFK KEYS

UD_API_KEY = os.environ.get("UD_API_KEY")
WEATHER_API_KEY = os.environ.get("WEATHER")
TOP_GG_TOKEN = os.environ.get("SHIT_GG_TOKEN")
TWITCH_CLIENT_ID = os.environ.get("TWITCH_CLIENT_ID")
TWITCH_CLIENT_SECRET = os.environ.get("TWITCH_CLIENT_SECRET")
CHAT_BID = os.environ.get("CHAT_BID")
CHAT_API_KEY = os.environ.get("CHAT_API_KEY")
DAGPI_KEY = os.environ.get("DAGPI_KEY")
STATCORD_KEY = os.environ.get("STATCORD_KEY")
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")

# SECRET LOGS HEHE :3

ONLINE_LOG_CHANNEL = 1009737849073053757
SHARD_LOG_CHANNEL = 1009737849073053757
ADD_REMOVE_LOG_CHANNEL = 793832499645644800
DATABASE_LOG_CHANNEL = 1009737849073053757
COMMANDS_LOG_CHANNEL = 1009737849073053757
ERROR_LOG_CHANNEL = 1009737849073053757
DM_LOG_CHANNEL = 1009737849073053757
BUG_REPORT_CHANNEL = 1007214201741250590
RANK_CARD_SUBMIT_CHANNEL = 1009737849073053757
SUGGESTION_CHANNEL = 1007214215632801832
USER_REPORT_CHANNEL = 1040359129383964772

# WEBHOOK LOGS

WEBHOOKS = {
    "startup": (1048500838479450192, os.environ.get("startup_webhook")),
    "add_remove": (1048500838479450192, os.environ.get("add_remove_webhook")),
    "cmd_uses": (1048500838479450192, os.environ.get("cmd_uses_webhook")),
    "cmd_error": (1048500838479450192, os.environ.get("cmd_error_webhook")),
    "event_error": (1048500838479450192, os.environ.get("event_error_webhook")),
}

# COLORS


# MAIN_COLOR = 0xDC143C # crimson
MAIN_COLOR = 0x2f3136  # light blue kinda
RED_COLOR = 0xFF0000
ORANGE_COLOR = 0xFFA500
PINK_COLOR = 0xe0b3c7
PINK_COLOR_2 = 0xFFC0CB
STARBOARD_COLOR = 15655584
INVISIBLE_COLOR = 0x36393F

# LINK

WEBSITE_LINK = ""
SUPPORT_SERVER_LINK = "https://discord.gg/soward"
INVITE_BOT_LINK = "https://discord.com/oauth2/authorize?client_id=1013771497157972008&permissions=1101052116095&scope=applications.commands%20bot"
VOTE_LINK = "https://top.gg/bot/1013771497157972008/vote"

# ROLES

BOT_MOD_ROLE = 1052860581650116618
OWNER_ROLE = 992488457383465061
SUPPORTER_ROLE = 992488456146137108
PARTNER_ROLE = 785404547883204608
STAFF_ROLE = 992488456867565669
BOOSTER_ROLE = 787336331474370563
DESIGN_HELPER_ROLE = 856100670780342272
VIP_ROLE = 746202728031584366
SOWARD_PREMIUM_ROLE = 992486993755910205
BIG_PP_GANG = []
NO_PP_GANG = []

# EMOJIS


BADGE_EMOJIS = {
    "USER": "<:Users:1048842224852541521>",
    "cutevi": "",
    "bot_mod": "<:Moderator:1051552457517432943>",
    "owner": "👑",
    "staff_member": "<a:TEAM_SOWARD:1039939734388084836>",
    "supporter": "<:EARLY_SUPPORTER:1017728098436919356>",
    "booster": "",
    "partner": "",
    "bug_hunter": "",
    "elite_bug_hunter": "",
    "early_supporter": "",
    "Big_PP": "",
    "No_PP": "",
    "aw||oo||sh": "",
    "wendo": "",
    "cat": "",
    "best_streamer": "",
    "voter": "",
    "cutie": "",
    "helper": "",
    "savior": "🙏",
    "very_good_taste": "",
    "samsung_girl": "",
    "love_magnet": "",
    "designer": "🎨",
}
EMOJIS = {
    'heawt': ' ',
    'loading': '<a:Loading:1041988103931428894> ',
    'hacker_pepe': ' ',
    # 'tick_yes': '<:tickYes:828260365908836423> ',
    'tick_yes': '<:ri8:1038487759750438912> ',  # '<a:EpicTik:766172079179169813> ',
    # 'tick_no': '<:tickNo:828262032495214643> ',
    'tick_no': '<:Wrong:1017402708703064144> ',
    'wave_1': ' ',
    'shy_uwu': ' ',
    'add': ' ',
    'remove': ' ',
    'pepe_jam': ' ',
    'pog_stop': ' ',
    'catjam': ' ',
    'epic_coin': ' ',
    'bruh': ' ',
    'mmm': ' ',
    'sleepy': ' ',
    'muted': ' ',
    'unmuted': ' ',
    'reminder': '⏰ ',
    'cool': ' ',
    'settings': ' ',
    'settings_color': ' ',
    'lb': ' ',
    'poglep': ' ',
    'weirdchamp': ' ',
    'twitch': ' ',
    'members': ' ',
    'ramaziHeart': ' ',
    'leveling': ' ',
    'vay': ' ',
    'chat': ' ',
    'hu_peng': ' ',
    'disboard': ' ',
    'online': ' ',
    'idle': ' ',
    'dnd': ' ',
    'arrow': ' ',
    'reaction': ' ',
    'cmd_arrow': ' ',
    'youtube': ' ',
    'cry_': ' '
}
EMOJIS_FOR_COGS = {
    'actions': '<a:hugs:839739273083224104>',
    'emojis': '<a:cool:844813588476854273>',
    'fun': '<a:laugh:849534486869442570>',
    'games': '🎮',
    'image': '📸',
    'info': '<:info:849534946170241034>',
    'leveling': '<a:leveling:849535096838815775>',
    'misc': '<a:PetEpicBot:797142108611280926>',
    'mod': '🛠️',
    'music': '<a:music:849539543103569941>',
    'nsfw': '🔞',
    'config': '<:settings:825008012867534928>',
    'starboard': '⭐',
    'utility': '🔧',
    'user': '<:EpicMembers:794075799422238720>',
    'notifications': '🔔',
    'custom': EMOJIS['settings_color'][:-1],
}
CUTE_EMOJIS = [
    "<:shy:844039614032904222>",
    "<:shy_peek:844039614309466134>",
    "<:Shy:851665918236557312>",
    "<:shy2:851666263922966588>",
    "<a:HeartOwO:849179336041168916>",
    "<:Heawt:802801495153967154>",
    "<:UwUlove:836174204108931072>",
    "<:Pikaluv:842981646424473601>",
    "<:mmm:834782050006466590>",
    "<a:kissl:808235261708337182>",
    "<:ur_cute:845151161039716362>",
    "<:thanks:800741855805046815>",
    "<a:hugs:839739273083224104>"
]
THINKING_EMOJI_URLS = [
    'https://cdn.discordapp.com/emojis/862387505852055602.png',
    'https://cdn.discordapp.com/emojis/768302864685727755.png',
    'https://cdn.discordapp.com/emojis/854206416830988318.png',
    'https://cdn.discordapp.com/emojis/853192295277002752.png',
    'https://cdn.discordapp.com/emojis/585956493392871424.png',
    'https://cdn.discordapp.com/emojis/819207595876417546.png'
]



# SOME RANDOM STUFF

start_time = time.time()
EMPTY_CHARACTER = "‎"

custom_cmds_tags_lemao = """
**User:**
`{user_name}` - The name of the user.
`{user_nickname}` - The nickname of the user.
`{user_discrim}` - The discriminator of the user.
`{user_tag}` - The complete tag of the user. (Eg. Username#0000)
`{user_id}` - The ID of the user.
`{user_mention}` - The mention of the user.
`{user_avatar}` - The avatar of the user.

**Guild:**
`{guild_name}` - The name of the server.
`{guild_id}` - The ID of the server.
`{guild_membercount}` - The membercount of the server.
`{guild_icon}` - The icon URL of the server.
`{guild_owner_name}` - The name of the owner of the guild.
`{guild_owner_id}` - The ID of the owner of the guild.
`{guild_owner_mention}` - The mention of the owner of the guild.

**Invites:**
`{user_invites}` - The invites of the user.
`{inviter_name}` - The name of the inviter who invited the user.
`{inviter_discrim}` - The discriminator of the inviter.
`{inviter_tag}` - The complete tag of the inviter. (Eg. Username#0000)
`{inviter_id}` - The ID of the inviter.
`{inviter_mention}` - The mention of the inviter.
`{inviter_avatar}` - The avatar of the inviter.
`{inviter_invites}` - The invites of the inviter.
"""

ENABLE = ['enable', 'enabled', 'yes', 'true']
DISABLE = ['disable', 'disabled', 'no', 'false']

DEFAULT_WELCOME_MSG = """


     " `{user_name}`** has joined our server! Invited by **{inviter_mention}
    ** inviter has total {inviter_invites} invites **

"""
DEFAULT_LEAVE_MSG = """

    
  **`{user_tag}`** has left {guild_name}
 Invited by `{inviter_tag}` who has now `{user_invites}` invites
 `
"""

DEFAULT_TWITCH_MSG = """
**{streamer}** is now live! Go check them out! {url}
"""

DEFAULT_LEVEL_UP_MSG = """
hey! {user_mention} just leveled up to level {level}!
"""

DEFAULT_AUTOMOD_CONFIG = {
    "banned_words": {
        "enabled": False,
        "words": [],
        "removed_words": []
    },
    "all_caps": {
        "enabled": False
    },
    "duplicate_text": {
        "enabled": False
    },
    "message_spam": {
        "enabled": False
    },
    "invites": {
        "enabled": False
    },
    "links": {
        "enabled": False,
        "whitelist": []
    },
    "mass_mentions": {
        "enabled": False
    },
    "emoji_spam": {
        "enabled": False
    },
    "zalgo_text": {
        "enabled": False
    },

    "ignored_channels": [],
    "allowed_roles": []
}

DEFAULT_BANNED_WORDS = [
    'nigg', 'n1gg', 'n*gg',
    'cunt', 'bitch', 'dick',
    'pussy', 'asshole', 'b1tch',
    'b!tch', 'b*tch', 'blowjob',
    'cock', 'c0ck', 'faggot',
    'whore', 'negro', 'retard',
    'slut', 'rape', 'n i g g '
]

GLOBAL_CHAT_RULES = """
**Global chat rules:**

- No Racism, Sexism, Homophobia or anything stupid.
- No NSFW messages or pictures or emotes.
- Do not be rude to anyone.
- No spamming.
- No self promo.
- No malicious links.

**If your message has a "❌" reaction added, that means your message was not sent because you broke one of these rules.**

**If you break any of these rules, you WILL get blacklisted and won't be able to use the bot.**
If you see anyone breaking these rules please report them using the `report` command.
"""

ANTIHOIST_CHARS = "!@#$%^&*()_+-=.,/?;:[]{}`~\"'\\|<>"
