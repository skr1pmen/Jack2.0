import asyncio
import aioschedule
from assets import config
from aiogram import Bot, Dispatcher
from handlers import user_commands, admin_commands
from callback.functions import Functions


async def schedule():
    aioschedule.every(15).minutes.do(Functions.new_schedule)
    # aioschedule.every().day.at("00:00").do(del_day_stats)
    # aioschedule.every().monday.at("00:00").do(week_reset)
    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(1)


async def main():
    bot = Bot(config.TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(
        user_commands.router,
        admin_commands.router,
    )

    asyncio.create_task(schedule())
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
