from dataclasses import dataclass
from environs import Env


@dataclass
class TgBot:
    token: str


@dataclass
class BotConfig:
    tg_bot: TgBot


def load_bot_config(path: str | None = None) -> BotConfig:
    env = Env()
    env.read_env(path)
    return BotConfig(tg_bot=TgBot(token=env('BOT_TOKEN')))
