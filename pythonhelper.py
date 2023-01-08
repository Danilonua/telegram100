from aiogram.utils import executor
from creat_bot import dp
from handlers import mute_file
from handlers import ban_file
from handlers import warn_file
from handlers import filter_file
from handlers import other_comands


mute_file.register_handlers_mute_file(dp)
ban_file.register_handlers_ban_file(dp)
warn_file.register_handlers_warn_file(dp)
other_comands.register_handlers_other_commands(dp)


filter_file.register_handlers_filter_file(dp)


if __name__ == '__main__':
    print('It has started!')
    executor.start_polling(dp)