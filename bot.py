import requests
import telebot
from telebot import types
from user_agent import *
tok = input("ENTER TOKEN BOT :")
bot = telebot.TeleBot(tok)
@bot.message_handler(commands=["start"])
def f(message):
    name = message.chat.first_name
    dev =types.InlineKeyboardButton(text=f"{name}",callback_data="sf")
    key=types.InlineKeyboardMarkup()
    key.raw_width=1
    key.add(dev)
    bot.send_message(message.chat.id,f"""
𝚂𝙴𝙽𝙳 𝚈𝙾𝚄𝚁 𝙳𝙰𝚃𝙰 :""",reply_markup=key)
@bot.message_handler(func=lambda m:True)
def f(message):
    chat_id = str(message.chat.id)
    start = bot.send_message(message.chat.id, f"Please Wait "+str(message.chat.first_name))
    odata0 = message.text
    pro=0
    while True:
        import requests
        from user_agent import generate_user_agent
        headers = {
        'authority': 's.learnhacker.repl.co',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98", "Google Chrome";v="98"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'upgrade-insecure-requests': '1',
        'user-agent': str(generate_user_agent()),
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-dest': 'document',
        'referer': f'https://followplus2.techdz1.repl.co/?timer=0&cd=like&odata={odata0}&submit=submit',
        'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    }
        params = (
        ('timer', '0'),
        ('cd', 'like'),
        ('odata', odata0),
        ('submit', 'submit'),
)
        response = requests.get('https://followplus2.techdz1.repl.co',headers=headers, params=params).text
        if 'coin":' in response:
            hamo = response.split('"coin":')[1].split("}")[0]
            pro+=1
            coin = types.InlineKeyboardButton(text=f"➬ 𝗖𝗼𝗶𝗻𝘀 : {hamo} ",callback_data="hx")
            ch = types.InlineKeyboardButton(text=f"➬ 𝗗𝘂𝘀𝘁𝗲𝗱  : {pro} ",callback_data="zjd")
            result = f"""
✅ 𝗦𝗲𝗿𝘃𝗲𝗿 𝗢𝗻𝗹𝗶𝗻𝗲
✅ 𝗧𝗿𝗮𝗰𝗶𝗻𝗴 𝗦𝘁𝗮𝗿𝘁𝗲𝗱
✅ 𝗣𝗟𝗘𝗔𝗦𝗘 𝗪𝗔𝗜𝗧..."""
            key=types.InlineKeyboardMarkup()
            key.raw_width=1
            key.add(coin)
            key.add(ch)
            bot.edit_message_text(text=result,chat_id=int(chat_id), message_id=start.message_id,reply_markup=key)
            if 'coin":' in response:
            	h = types.InlineKeyboardButton(text=f"➬ 𝗖𝗼𝗶𝗻𝘀 : {hamo} ",callback_data="hx")
            result = f"""
✅ 𝗦𝗲𝗿𝘃𝗲𝗿 𝗢𝗻𝗹𝗶𝗻𝗲
❌ 𝗧𝗿𝗮𝗰𝗶𝗻𝗴 𝗦𝘁𝗮𝗿𝘁𝗲𝗱
✅ 𝗣𝗟𝗘𝗔𝗦𝗘 𝗪𝗔𝗜𝗧..."""
            key = types.InlineKeyboardMarkup()
            key.raw_width = 1
            key.add(h)
            bot.edit_message_text(text=result, chat_id=int(chat_id), message_id=start.message_id, reply_markup=key)
bot.polling(True)