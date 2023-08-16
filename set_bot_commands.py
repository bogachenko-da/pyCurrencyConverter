from telebot.types import BotCommand
from config import DEFAULT_COMMANDS


def set_default_commands(bot):
    """
    Функция для вывода доступных команд.
    """
    bot.set_my_commands(
        [BotCommand(*i) for i in DEFAULT_COMMANDS]
    )
