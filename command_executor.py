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
            lines = text.split('\n')
            buffer = ''
            buff_length = 0

            for line in lines:
                curr_line_length = len(line)
                if curr_line_length > 2000:
                    await self.user.send(buffer)
                    buffer = ''
                    buff_length = 0

                    text = line
                    while text:
                        length = len(text)
                        shorted_text = text[0:2000 if length > 2000 else -1]
                        await self.user.send(shorted_text)
                        text = text[2000::]
                    continue

                if buff_length + curr_line_length < 2000:
                    buffer += line + '\n'
                else:
                    await self.user.send(buffer)
                    buffer = line + '\n'

                buff_length = len(buffer)
            if buffer:
                await self.user.send(buffer)
            return

        await self.user.send(text)

    async def reply_file(self, text: str, filepath: str):
        await self.user.send(text, file=discord.File(filepath))

    async def handle_callback(self, clb_tp, *params):
        match clb_tp:
            case 'file':
                await self.reply_file(
                    params[0],
                    params[0]
                )

    async def execute(self, *args, command: str, **kwargs):
        try:
            handler = getattr(command_handlers, command + '_hndl')
            output = handler(
                *args,
                state=self.state,
                config=self.config,
                user=self.user,
                **kwargs
            )
            if isinstance(output, tuple | list):
                await self.handle_callback(output[0], *output[1::])
                return

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
