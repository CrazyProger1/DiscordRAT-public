import discord
from config import Config, SerializableObject
from message_handler import MessageHandler


class App:
    """
    Main application class
    """

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    config = SerializableObject.load(Config)
    message_handler = MessageHandler(config)

    async def on_message(self, message: discord.Message):
        if message.author == self.client:
            return

        await self.message_handler.handle(
            message=message
        )

    def run(self):
        self.client.event(self.on_message)
        self.client.run(
            token=self.config.token
        )


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
