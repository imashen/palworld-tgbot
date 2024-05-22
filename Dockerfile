FROM python:3.12
COPY . /bot
WORKDIR /bot
RUN pip install aiohttp python-telegram-bot
ENTRYPOINT [ "python" ]
CMD ["bot.py"]
