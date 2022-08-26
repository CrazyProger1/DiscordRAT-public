import discord
from config import Config, SerializableObject
from message_handler import MessageHandler
from text import ONLINE


class App:
    """
    Main application class
    """

    intents = discord.Intents.default()
    intents.message_content = True
    intents.members = True
    client = discord.Client(intents=intents)
    config = SerializableObject.load(Config)
    message_handler = MessageHandler(config)

    async def on_message(self, message: discord.Message):
        if message.author == self.client:
            return

        await self.message_handler.handle(
            message=message
        )

    async def on_ready(self):
        for member in self.client.get_all_members():
            if member.name != self.client.user.name:
                await member.send(ONLINE.format(bot_name=self.config.bot_name))

    def run(self):
        self.client.event(self.on_message)
        self.client.event(self.on_ready)
        self.client.run(
            token=self.config.token
        )


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
