from aiogram.utils import executor
from handlers import client,callback,extra,callback_vetka_good,\
    callback_vetka_bad,fsmadmin,fsadmin_register, notification,notification_me
from config import dp,bot
from database import bot_db
import asyncio
from decouple import config
from config import URI
async def on_startup(_):
    await bot.set_webhook(URI)
    bot_db.sql_create()
    asyncio.create_task(notification.scheduler())
    asyncio.create_task(notification_me.scheduler())
    asyncio.create_task(notification_me.scheduler_lesson())
    print("Bot is online")

async def on_shutdown(dp):
    await bot.delete_webhook()



fsmadmin.register_handler_admin(dp)
fsadmin_register.register_handler_user(dp)
client.register_handlers_client(dp)
callback.register_handler_callback(dp)
notification.register_handler_notification(dp)
notification_me.register_handler_notification_me(dp)
callback_vetka_good.register_handler_callback(dp)
callback_vetka_bad.register_handler_callback(dp)
extra.register_handler_other(dp)




if __name__ == "__main__":
    # executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
    executor.start_webhook(
        dispatcher=dp,
        webhook_path='',
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host='0.0.0.0',
        port=int(config("PORT",default=5000))
    )
