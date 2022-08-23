import discord
import re

from config import Config
from command_executor import Executor


class MessageHandler:
    def __init__(self, config: Config):
        self.config = config
        self.command_executors: dict[discord.User, Executor] = {}

    @staticmethod
    def is_command(message: discord.Message):
        return message.content.startswith('$')

    @staticmethod
    def parse_command(command_with_args: str) -> tuple[str, dict]:
        command = ''
        kwargs = {}

        result = re.match(r'\$[\w]+', command_with_args)
        if result:
            command = result.group()[1::]

        arguments = re.findall(r'\s*[\w]+\s*=\s*[\w]+\s*', command_with_args[len(command) + 1::])
        arguments.extend(
            map(lambda e: e.replace("'", ''),
                re.findall(r'\s*[\w]+\s*=\s*\'[\S\s]+\'\s*', command_with_args[len(command) + 1::]))
        )

        for arg_string in arguments:
            key_value: str = arg_string.split('=')
            kwargs.update({key_value[0].strip(): key_value[1].strip()})

        return command, kwargs

    async def handle_command(self, command_with_args: str, executor: Executor):
        command, kwargs = self.parse_command(
            command_with_args=command_with_args
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
                command_with_args=message.content,
                executor=executor
            )
