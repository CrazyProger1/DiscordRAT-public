import discord
import command_handlers

from state import State
from config import Config
from text import *


class Executor:
    def __init__(self, user: discord.User, config: Config):
        self.user = user
        self.state = State()
        self.config = config

    async def reply_error(self, err: str, msg: str):
        await self.user.send(err + msg)

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
                await self.reply_error(ERR_OUTPUT, 'output is empty')
                return

            await self.reply(output)

        except AttributeError:
            await self.reply_error(
                ERR_COMMAND, COMMAND_DOES_NOT_EXISTS.format(command=command)
            )
        except TypeError as e:
            await self.reply_error(
                ERR_ARG, str(e)
            )

        except Exception as e:
            await self.reply_error(
                ERR_UNIDENTIFIED, str(e)
            )
