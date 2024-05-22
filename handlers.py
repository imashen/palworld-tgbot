from telegram import Update
from telegram.ext import ContextTypes, ConversationHandler
from palworld import get_players, send_announcement, kick_player, ban_player, unban_player

# 定义一个全局变量来存储管理员密码
ADMIN_PASSWORD = getenv("ADMIN_PASSWORD")
PASSWORD, = range(1)

# 定义启动命令的处理函数
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Welcome to GijinkaBot!")

# 定义身份验证命令的处理函数
async def auth_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("请在私聊框中输入管理员密码")
    return PASSWORD

# 处理用户输入的密码
async def handle_auth(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.message.text == ADMIN_PASSWORD:
        context.user_data["is_authenticated"] = True
        await update.message.reply_text("身份验证成功！")
        # 删除用户输入的密码消息
        await update.message.delete()
        return ConversationHandler.END
    else:
        await update.message.reply_text("密码错误，请重新输入:")
        # 删除用户输入的错误密码消息
        await update.message.delete()
        return PASSWORD

# 定义一个装饰器函数来检查身份验证状态
def require_auth(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not context.user_data.get("is_authenticated"):
            await update.message.reply_text("请先使用/auth命令进行身份验证。")
            return
        return await func(update, context)
    return wrapper

# 定义获取服务器信息的处理函数
async def players_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = await get_players()
    await update.message.reply_text(message)

# 定义全服播报命令的处理函数
@require_auth
async def announce_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = " ".join(context.args)
    if not message_text:
        await update.message.reply_text("请输入要播报的消息。")
        return

    response = await send_announcement(message_text)
    await update.message.reply_text(response)

# 定义踢出玩家的处理函数
@require_auth
async def kick_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("请输入正确的命令格式：/kick <玩家ID> <踢出原因>")
        return

    user_id = args[0]
    reason = " ".join(args[1:])
    response = await kick_player(user_id, reason)
    await update.message.reply_text(response)

# 定义封禁玩家的处理函数
@require_auth
async def ban_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) < 2:
        await update.message.reply_text("请输入正确的命令格式：/ban <玩家ID> <封禁原因>")
        return

    user_id = args[0]
    reason = " ".join(args[1:])
    response = await ban_player(user_id, reason)
    await update.message.reply_text(response)

# 定义解禁玩家的处理函数
@require_auth
async def unban_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) < 1:
        await update.message.reply_text("请输入正确的命令格式：/unban <玩家ID>")
        return

    user_id = args[0]
    response = await unban_player(user_id)
    await update.message.reply_text(response)
