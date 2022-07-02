import telebot
import config
from bs4 import BeautifulSoup as bs
import requests
import random
import wikipedia
from telebot import types
#  import urllib
# import v

bot = telebot.TeleBot(config.token)


def rand(): # определят конечное число страниц на сайте

    url_n = 'https://nekdo.ru/'
    r_n = requests.get(url_n)

    #  print(r_n.status_code)

    soup = bs(r_n.text, 'html.parser')
    page_m = soup.find_all('a', class_='nav')
    page2_m = page_m[::-1]
    page3_m = page2_m[0]

    print(page3_m)
    all_page = []
    all_x = 0
    for i in page3_m:
        all_page.append(i)
        print(all_page)
        # inz = map(int,all_page)
        all_x = int(''.join(all_page))
    print(all_x)
    # page_x = str(random.randint(1, all_x))
    # print(page_x)
    # print(soup)
    return all_x


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет ✌️!')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    anecdot = types.KeyboardButton('ЖМИ')
    help = types.KeyboardButton('/help')
    markup.add(anecdot,help)
    bot.send_message(message.chat.id, 'Жми Кнопку и получай новый анекдот', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Я веселый Бот... Я могу найти кучу Анекдотов✌️! "ЖМИ" и смейся )))')

# @bot.message_handler(commands=['1'])
# def send_pic(m):
    # banlist = redis.sismember('banlist', '{}'.format(m.from_user.id))
    # if str(banlist) == 'False':
    # urllib.urlretrieve("https://source.unsplash.com/random", "img.jpg")
    # photo = open(img.jpg)
    # bot.send_photo(message.chat.id, photo)
    # bot.send_photo(m.chat.id, open('img.jpg'))

@bot.message_handler(commands=["ping"])
def ping(message):
     bot.reply_to(message, 'Живой я ...Живой... Ток уснул)))')


'''''''''
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="С пюрешкой")
    keyboard.add(button_1)
    button_2 = "Без пюрешки"
    keyboard.add(button_2)
    await message.answer("Как подавать котлеты?", reply_markup=keyboard)

'''''


@bot.message_handler()
def anecdot(message):
        all_x = rand()
        page_x = str(random.randint(1, all_x))
        print(all_x)
        print(page_x)
        # print(soup)
        url = 'https://nekdo.ru/' + 'page' + '/' + page_x
        r = requests.get(url)
        soup = bs(r.text, 'html.parser')
        print(url)
        anecdots = soup.find_all('div', class_='text')
        print(anecdots)

        all_anecdots = []
        print(all_anecdots)
        for i in anecdots:
            all_anecdots.append(i.text)
        print(all_anecdots)
        bot.send_message(message.chat.id, random.choice(all_anecdots))



bot.polling(none_stop=True)
# bot.infinity_polling()
