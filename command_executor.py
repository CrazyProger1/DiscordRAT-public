import discord
import command_handlers

from state import State, WorkingModes
from config import Config
from text import *
from exceptions import *


class Executor:
    """
    Each user have own executor
    Responsible for command executing and replying to user
    """

    def __init__(self, user: discord.User, config: Config):
        self.user = user
        self.state = State()
        self.config = config

    async def reply_error(self, err: str, msg: str):
        await self.user.send(err + msg)

    async def reply(self, text: str):
        if len(text) > 2000:
            while text:
                length = len(text)
                shorted_text = text[0:2000 if length > 2000 else -1]
                await self.user.send(shorted_text)
                text = text[2000::]
            return
        await self.user.send(text)

    async def execute(self, *args, command: str, **kwargs):
        try:
            handler = getattr(command_handlers, command + '_hndl')
            output = handler(
                *args,
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
        except CommandExecutionError as e:
            await self.reply_error(
                ERR_COMMAND_EXECUTION, str(e)
            )

        except Exception as e:
            await self.reply_error(
                ERR_UNIDENTIFIED, str(e)
            )
