import logging
import mechanicalsoup

from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State

# keyboardlar tugmalar bo`limi

qism = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton('Premyeralar')
        ],
    ]
)
qism.resize_keyboard = True

#keyborad tugmalar bo`limi yakuni#





#holatlar bo`limi


class Search(StatesGroup):
    search = State()



#holatlar bo`limi yakuni






#qo`shimcha funksiyalar bo`limi

browser = mechanicalsoup.StatefulBrowser()

url = "http://uzmovi.com/"

browser.open(url)


def Premyera(url):
    page = browser.get_current_page()

    premyera = page.find_all('a', class_='cs-item')

    prem_link = []
    for i in premyera:
        url = i.get('href')
        prem_link.append(url)
    return prem_link




#qo`shimcha funksiyalar bo`limi yakuni


API_TOKEN = '5131509521:AAGVgPGQAJ2Es6VoXOPs37Sts9E1UbFBXaw'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu aleykum Hemis botga xush kelibsiz!\n Bu botga istalgan film nomini yozsangiz shu zahoti fimni topib beradi...", reply_markup=qism)



@dp.message_handler(text=['Premyeralar'])
async def filmlar(message: types.Message):
    for i in Premyera("http://uzmovi.com/"):
        await message.answer(i)





@dp.message_handler()
async def qidiruv(message: types.Message):
    browser = mechanicalsoup.StatefulBrowser()

    url = "http://uzmovi.com/"

    browser.open(url)
    name = message.text
    browser.select_form('form[action="http://uzmovi.com/search"]')
    browser['q'] = name
    browser.submit_selected()

    pege1 = browser.get_current_page()
    search = pege1.find_all('a', class_='short-images-link')

    search_list = []
    for n in search:
        url = n.get('href')
        name = n.get('title')
        await message.answer(url)









@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)