# 语言
- ENG [English](README.md)
- CHS [简体中文](README_CHS.md)

实现简易的Telegram机器人功能，如获取在线玩家列表，踢出、封禁、解禁、全服广播内容等操作

## 功能介绍
/start 开始机器人 </br>
/auth 验证管理员权限 </br>
/kick 踢出玩家 | 命令格式：/kick <玩家ID> <原因> </br>
/ban 封禁玩家 | 命令格式：/ban <玩家ID> <原因> </br>
/unban 解禁玩家 | 命令格式：/unban <玩家ID> </br>
/announce 全服广播 | 命令格式：/announce <播报消息> </br>

## Docker容器化使用：
```
docker run -itd --name tg-bot \
 -e "TELEGRAM_BOT_TOKEN"="7042050000:AAG-gex61EsmnHp00VwgMw00EFol2xPGlzQ" \
 -e "ADMIN_PASSWORD"="demopassword" \
 -e "API_BASE_URL"="http://gameserver.ip:8212/v1/api" \
 -e "API_USERNAME"="admin" \
 -e "API_PASSWORD"="demo_rest_api_password" \
 imashen/palworld-tgbot:latest
```
`ADMIN_PASSWORD`校验指令`/auth`时所用的密码，可以与机器人私聊来鉴权验证以使用管理员指令 </br>
`API_BASE_URL`服务器RestAPI总接口地址 </br>
`API_USERNAME`默认为`admin` </br>
`API_PASSWORD`是你在palworld服务器中设定的RestAPI的密码 </br>
