# DiscordRAT-public

Discord Remote Access Tool - simple RAT written in Python using discord.py lib

## Build

> **NOTE:** *Before building, make sure you have pyinstaller installed and all requirements satisfied. See [requirements](#requirements) section.*

Before building, you need to put your discord bot token into file ["config.py"](config.py). This can be done using
the ["inject_token.py"](scripts/inject_token.py) script.


> **NOTE:** *All scripts must be run from the project's root directory.*

- ["inject_token.py"](scripts/inject_token.py) usage:

```commandline
python inject_token.py <Your token>
```

Then, you can start building. For this you need to run [build.bat](scripts/build.bat) script:

```commandline
scripts/build.bat
```

## Requirements

To install the requirements, run the following command.

```commandline
pip install -r requirements.txt
```

Also, if you want to build, you need to install pyinstaller:

```commandline
pip install pyinstaller
```

## Licence

DiscordRAT uses the MIT license. See the bundled [LICENSE](LICENSE) file for details.