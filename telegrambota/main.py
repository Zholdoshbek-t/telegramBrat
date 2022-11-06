from aiogram import Bot, executor, Dispatcher, types
from aiogram.types import base, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from decouple import config

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def hello(message: types.Message):
    await bot.send_message(message.chat.id, f'Hello : {message.from_user.full_name}')


#1
@dp.message_handler(commands=['games'])
async def games_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Следующий соперник",
                                         callback_data='next_task1')
    markup.add(button_call_1)
    question = 'Что у всех людей одного цвета?'
    answers = ['зубы', 'глаза', 'трицепсы', 'волосы']
    photo = open('media/1.jpg', 'rb')
    await bot.send_photo(message.chat.id, photo=photo)
    await bot.send_poll(
        message.chat.id,
                        question=question,
                        options=answers,
                        correct_option_id=1,
                        is_anonymous = False,
                        type='quiz',
                        reply_markup=markup,
                        open_period=30,
                        explanation='Настигнул тебя же есть',
                        explanation_parse_mode = ParseMode.MARKDOWN_V2
    )
#2
@dp.callback_query_handler(lambda func: func.data == 'next_task1')
async def games_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton('Следующая соперник', callback_data='next_task2')
    markup.add(button_call_2)
    question2 = 'Что или кто такой Эритроцит?'
    answers = ['Это наиболее многочисленный клеточный компонент крови', 'Мышцы, которые можно накачать во время пробежки', 'Леденцы от горла', 'Брат Цвестита']
    photo = open('media/2.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
                            question=question2,
                            options=answers,
                            correct_option_id=0,
                            open_period=30,
                            explanation='Братишка учиться надо было',
                            explanation_parse_mode=ParseMode.MARKDOWN_V2,
                            is_anonymous=False,
                            type='quiz',
                            reply_markup=markup
    )
#3
@dp.callback_query_handler(lambda func: func.data == 'next_task2')
async def task_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Следующий соперник", callback_data='next_task3')
    markup.add(button_call_3)
    question3 = 'Основная, феноменальная, неповторимая функция бровей?'
    answers3 = ['Много не допускать', 'Не допускать попадания пота в глаза', 'Делать лицо красивее', 'Давать возможность заработать визажистам или как их там звать']
    photo = open('media/3.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
                            question=question3,
                            options=answers3,
                            correct_option_id=1,
                            open_period=30,
                            explanation='Снова настиг тебя?',
                            explanation_parse_mode=ParseMode.MARKDOWN_V2,
                            is_anonymous=False,
                            type='quiz',
                            reply_markup=markup
    )

#4
@dp.callback_query_handler(lambda func: func.data == 'next_task3')
async def task_4(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_4 = InlineKeyboardButton("Близко близко", callback_data='next_task4')
    markup.add(button_call_4)
    question4 = 'Ежедневно с головы может выпадать до ... волосков?'
    answers4 = ['При щелчке выпадает 50% процентов волос', '1 миллион', '2 миллиона', '80 долларов', '80']
    photo = open('media/4.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
                            question=question4,
                            options=answers4,
                            correct_option_id=4,
                            open_period=30,
                            explanation='Подсказака в картинке, лол',
                            explanation_parse_mode=ParseMode.MARKDOWN_V2,
                            is_anonymous=False,
                            type='quiz',
                            reply_markup=markup
    )

@dp.callback_query_handler(lambda func: func.data == 'next_task4')
async def task_5(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_5 = InlineKeyboardButton("Чуть чуть осталось", callback_data='next_task5')
    markup.add(button_call_5)
    question5 = 'Самая длинная операция продолжалась 96 часов. Что за оперейшн был, а?'
    answers5 = ['В больнице Чикаго пациенту была успешно удалена раковая опухоль', 'Блицкриг', 'Найти свежую лепешку в выходные, с утра еще если что']
    photo = open('media/5.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
                            question=question5,
                            options=answers5,
                            correct_option_id=0,
                            open_period=30,
                            explanation='Хватит гуглить',
                            explanation_parse_mode=ParseMode.MARKDOWN_V2,
                            is_anonymous=False,
                            type='quiz',
                            reply_markup=markup
    )
@dp.callback_query_handler(lambda func: func.data == 'next_task5')
async def task_6(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_5 = InlineKeyboardButton("Нормально будь да вообще в общем", callback_data='next_task6')
    markup.add(button_call_5)
    question5 = 'Кто из врачей отвечает за человеческий «мотор»?'
    answers5 = ['Понятно же, МОТОРИСТ', 'Тракторист', 'Человек, логично же', 'Кардиомагнил', 'Кардиолог']
    photo = open('media/6.jpg', 'rb')
    await bot.send_photo(call.message.chat.id, photo=photo)
    await bot.send_poll(
        call.message.chat.id,
                            question=question5,
                            options=answers5,
                            correct_option_id=4,
                            open_period=30,
                            explanation='Вопрос с проходом в ноги, по любому пропустишь',
                            explanation_parse_mode=ParseMode.MARKDOWN_V2,
                            is_anonymous=False,
                            type='quiz',
                            reply_markup=markup
    )
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False)

