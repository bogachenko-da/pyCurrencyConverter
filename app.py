import telebot
from config import curr_keys, TOKEN
from extensions import APIException, Converter
from config import DEFAULT_COMMANDS

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def bot_start(message: telebot.types.Message):
    """
    Функция-обработчик команды start.
    """
    text = f'Здравствуйте, <b>{message.from_user.full_name}</b>!' \
           '\nИнформация по работе бота /help.'
    bot.send_message(message.chat.id, text, parse_mode='html')


@bot.message_handler(commands=['help'])
def command_start_help(messsage: telebot.types.Message):
    """
    Функция-обработчик команды help.
    """
    text = 'Чтобы начать работу введите через пробел:' \
           '\n<имя исходной валюты>' \
           '\n<имя валюты, в которою необходимо конвертировать>' \
           '\n<количество исходной валюты>' \
           '\nПример: доллар рубль 4' \
           '\n/values - Список доступных валют' \
           '\n/commands - Список доступных команд'
    bot.reply_to(messsage, text)


@bot.message_handler(commands=['commands'])
def bot_help(message: telebot.types.Message):
    """
    Функция-обработчик команды commands.
    """
    text = [f'/{command} - {desk}' for command, desk in DEFAULT_COMMANDS]
    bot.reply_to(message, '\n'.join(text))


@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    """
    Функция-обработчик команды values.
    """
    text = 'Доступные валюты:'
    for key, value in curr_keys.items():
        text = '\n'.join((text, f'{key}: {value}'))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    """
    Функция принимает данные от пользователя и возвращает результат конвертирования.
    """
    try:
        values = (message.text.lower().split(' '))

        if len(values) != 3:
            raise APIException('Слишком много параметров.')

        quote, base, amount = values
        total_base = Converter.get_price(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} - {total_base}'
        bot.send_message(message.chat.id, text)


bot.polling()
