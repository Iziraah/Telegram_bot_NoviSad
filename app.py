
from heandlers import dp
from aiogram.utils import executor

from heandlers.users.text_answers import AlbumMiddleware
   




if __name__ == '__main__':
    dp.middleware.setup(AlbumMiddleware())
    executor.start_polling(dispatcher=dp)