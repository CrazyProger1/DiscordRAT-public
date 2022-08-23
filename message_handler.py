import discord
import re

from config import Config
from command_executor import Executor
from state import WorkingModes
from commands import *
from text import *


class MessageHandler:
    def __init__(self, config: Config):
        self.config = config
        self.command_executors: dict[discord.User, Executor] = {}

    @staticmethod
    def is_command(message: discord.Message):
        return message.content.startswith('$')

    @staticmethod
    def parse_command_with_args(command_with_args: str) -> tuple[str, tuple]:

        split_command = re.split(r'\s+', command_with_args)
        args = []
        if len(split_command) > 1:
            args = split_command[1::]

        return split_command[0].strip()[1::], tuple(map(str.strip, args))

    @staticmethod
    def parse_command_with_kwargs(command_with_kwargs: str) -> tuple[str, dict]:
        command = ''
        kwargs = {}

        result = re.match(r'\$[\w]+', command_with_kwargs)
        if result:
            command = result.group()[1::]

        arguments = re.findall(r'\s*[\w]+\s*=\s*[\w]+\s*', command_with_kwargs[len(command) + 1::])
        arguments.extend(
            map(lambda e: e.replace("'", ''),
                re.findall(r'\s*[\w]+\s*=\s*\'[\S\s]+\'\s*', command_with_kwargs[len(command) + 1::]))
        )

        for arg_string in arguments:
            key_value: str = arg_string.split('=')
            kwargs.update({key_value[0].strip(): key_value[1].strip()})

        return command, kwargs

    @staticmethod
    async def change_mode(command: str, executor: Executor) -> bool:
        for mode_key, commands in COMMANDS.items():
            if command in commands:
                executor.state.working_mode = WorkingModes(mode_key)
                working_mode = executor.state.working_mode
                await executor.reply(
                    MODE_AUTO_CHANGE.format(value=working_mode.value, name=working_mode.name)
                )
                return True
        return False

    async def handle_command(self, raw_command: str, executor: Executor):
        working_mode = executor.state.working_mode

        match working_mode:
            case WorkingModes.filesystem:
                command, args = self.parse_command_with_args(
                    command_with_args=raw_command,
                )
                if command not in COMMANDS.get(working_mode.value):
                    if await self.change_mode(command=command, executor=executor):
                        return await self.handle_command(
                            raw_command=raw_command,
                            executor=executor
                        )

                await executor.execute(
                    *args,
                    command=command
                )
            case WorkingModes.basic:
                command, kwargs = self.parse_command_with_kwargs(
                    command_with_kwargs=raw_command,
                )

                if command not in COMMANDS.get(working_mode.value):
                    if await self.change_mode(command=command, executor=executor):
                        return await self.handle_command(
                            raw_command=raw_command,
                            executor=executor
                        )

                await executor.execute(
                    command=command,
                    **kwargs
                )

    def get_executor(self, message: discord.Message) -> Executor:
        executor = self.command_executors.get(message.author)
        if not executor:
            executor = Executor(
                user=message.author,
                config=self.config
            )
            self.command_executors.update({
                message.author: executor
            })

        return executor

    async def handle(self, message: discord.Message):
        executor = self.get_executor(
            message=message
        )

        if self.is_command(message):
            await self.handle_command(
                raw_command=message.content,
                executor=executor
            )
