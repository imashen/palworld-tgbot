# Palworld-TgBot | Simple Functionality Bot for Palworld on Telegram
This bot implements basic Telegram bot functionalities, such as retrieving the list of online players, kicking, banning, unbanning players, and broadcasting messages to the entire server.

## Feature Introduction
/start Start the bot </br>
/auth Authenticate admin privileges </br>
/kick Kick a player | Command format: /kick <PlayerID> <Reason> </br>
/ban Ban a player | Command format: /ban <PlayerID> <Reason> </br>
/unban Unban a player | Command format: /unban <PlayerID> </br>
/announce Broadcast to the server | Command format: /announce <Message> </br>

## Using Docker Container:
```
docker run -itd --name tg-bot \
 -e "TELEGRAM_BOT_TOKEN"="7042050000:AAG-gex61EsmnHp00VwgMw00EFol2xPGlzQ" \
 -e "ADMIN_PASSWORD"="demopassword" \
 -e "API_BASE_URL"="http://gameserver.ip:8212/v1/api" \
 -e "API_USERNAME"="admin" \
 -e "API_PASSWORD"="demo_rest_api_password" \
 imashen/palworld-tgbot:latest
```

ADMIN_PASSWORD is the password used to verify the /auth command, allowing the bot to authenticate and enable admin commands via private chat. </br>
API_BASE_URL is the base URL for the server's RestAPI. </br>
API_USERNAME defaults to admin. </br>
API_PASSWORD is the RestAPI password set on your Palworld server. </br>
# Palworld-TgBot | 幻兽帕鲁Telegram简易功能机器人


