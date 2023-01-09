from aiogram.utils import executor
from creat_bot import dp
from handlers import mute_file
from handlers import ban_file
from handlers import warn_file
from handlers import filter_file
from handlers import other_commands
from handlers import id_file
from handlers import games_commands


mute_file.register_handlers_mute_file(dp)
ban_file.register_handlers_ban_file(dp)
warn_file.register_handlers_warn_file(dp)
other_commands.register_handlers_other_commands(dp)
id_file.register_handlers_id_file(dp)
games_commands.register_handlers_id_file(dp)
filter_file.register_handlers_filter_file(dp)


if __name__ == '__main__':
    print('It has started!')
    executor.start_polling(dp)