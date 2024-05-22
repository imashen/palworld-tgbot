import logging
import os
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import start_command, players_command, announce_command, kick_command, ban_command, unban_command, auth_command, handle_auth
from os import getenv
mytoken = getenv('TELEGRAM_BOT_TOKEN')

# 启用日志记录
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def main() -> None:
    # 创建Application对象，并传入你的机器人Token
    application = ApplicationBuilder().token(mytoken).build()

    # 注册启动命令处理器
    application.add_handler(CommandHandler("start", start_command))

    # 注册身份验证命令处理器
    application.add_handler(CommandHandler("auth", auth_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_auth))

    # 注册获取服务器信息的命令处理器
    application.add_handler(CommandHandler("players", players_command))

    # 注册全服播报命令处理器
    application.add_handler(CommandHandler("announce", announce_command))

    # 注册踢出玩家命令处理器
    application.add_handler(CommandHandler("kick", kick_command))

    # 注册封禁玩家命令处理器
    application.add_handler(CommandHandler("ban", ban_command))

    # 注册解禁玩家命令处理器
    application.add_handler(CommandHandler("unban", unban_command))

    # 启动机器人
    application.run_polling()

if __name__ == '__main__':
    main()
