from dataclasses import dataclass
import os

from dotenv import load_dotenv

load_dotenv()


@dataclass
class TgBot:
    token: str


@dataclass
class Config:
    tg_bot: TgBot


def load_config() -> Config:
    return Config(tg_bot=TgBot(
        token=os.environ.get('TOKEN', 'Введите Ваш токен бота')
    ))
