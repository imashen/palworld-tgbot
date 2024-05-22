import aiohttp
import logging
from os import getenv

base_url = getenv('API_BASE_URL')
myusername = getenv('API_USERNAME')
mypassword = getenv('API_PASSWORD')

async def get_players() -> str:
    url = base_url + '/players'
    auth = aiohttp.BasicAuth(myusername, mypassword)
    
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url, auth=auth) as response:
                response.raise_for_status()
                data = await response.json()
                
                if "players" in data and data["players"]:
                    players_info = "\n".join(format_player_info(player) for player in data["players"])
                    return f"当前在线玩家:\n{players_info}"
                else:
                    return "当前没有在线玩家。"
        except aiohttp.ClientError as e:
            logging.error(f"请求错误: {e}")
            return "无法获取服务器信息。"

def format_player_info(player: dict) -> str:
    level = player.get("level", "Unknown")
    name = player.get("name", "Unknown")
    user_id = player.get("userId", "Unknown")
    return f"LV{level} {name} {user_id}"

async def send_announcement(message: str) -> str:
    url = base_url + '/announce'
    auth = aiohttp.BasicAuth(myusername, mypassword)
    headers = {'Content-Type': 'application/json'}

    async with aiohttp.ClientSession() as session:
        try:
            payload = {'message': message}
            async with session.post(url, auth=auth, headers=headers, json=payload) as response:
                response.raise_for_status()
                return "广播发送成功。"
        except aiohttp.ClientError as e:
            logging.error(f"请求错误: {e}")
            return "无法发送广播。"

async def kick_player(user_id: str, reason: str) -> str:
    url = base_url + '/kick'
    auth = aiohttp.BasicAuth(myusername, mypassword)
    headers = {'Content-Type': 'application/json'}

    async with aiohttp.ClientSession() as session:
        try:
            payload = {'userid': user_id, 'message': reason}
            async with session.post(url, auth=auth, headers=headers, json=payload) as response:
                response.raise_for_status()
                return f"玩家已踢出."
        except aiohttp.ClientError as e:
            logging.error(f"请求错误: {e}")
            return "无法执行踢出操作。"

async def ban_player(user_id: str, reason: str) -> str:
    url = base_url + '/ban'
    auth = aiohttp.BasicAuth(myusername, mypassword)
    headers = {'Content-Type': 'application/json'}

    async with aiohttp.ClientSession() as session:
        try:
            payload = {'userid': user_id, 'message': reason}
            async with session.post(url, auth=auth, headers=headers, json=payload) as response:
                response.raise_for_status()
                return f"玩家已封禁."
        except aiohttp.ClientError as e:
            logging.error(f"请求错误: {e}")
            return "无法执行封禁操作。"

async def unban_player(user_id: str) -> str:
    url = base_url + '/unban'
    auth = aiohttp.BasicAuth(myusername, mypassword)
    headers = {'Content-Type': 'application/json'}

    async with aiohttp.ClientSession() as session:
        try:
            payload = {'userid': user_id}
            async with session.post(url, auth=auth, headers=headers, json=payload) as response:
                response.raise_for_status()
                return f"玩家已解除封禁."
        except aiohttp.ClientError as e:
            logging.error(f"请求错误: {e}")
            return "无法执行解封操作。"
