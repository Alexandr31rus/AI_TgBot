import os
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from app.admin import admin
from app.user import user

load_dotenv()

async def main():
    bot = Bot(token=os.getenv("TG_TOKEN"))
    dp = Dispatcher()
    dp.include_routers(user, admin)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        print('Bot started ...')
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
