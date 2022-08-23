import pickle
import discord
from config import Config, SerializableObject


class App:
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    config = SerializableObject.load(Config)

    @client.event
    async def on_message(self, message: discord.Message):
        pass

    def run(self):
        self.client.run(
            token=self.config.token
        )


def main():
    app = App()
    app.run()


if __name__ == '__main__':
    main()
