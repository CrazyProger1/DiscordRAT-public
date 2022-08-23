import discord
import command_handlers

from state import State
from config import Config


class Executor:
    def __init__(self, user: discord.User, config: Config):
        self.user = user
        self.state = State()
        self.config = config

    async def reply(self, text: str):
        await self.user.send(text)

    async def execute(self, command: str, **kwargs):
        try:
            handler = getattr(command_handlers, command + '_hndl')
            output = handler(
                state=self.state,
                config=self.config,
                **kwargs
            )
            if not output:
                raise
            await self.reply(output)
        except AttributeError:
            await self.reply(f'That command does not exists "{command}"')
