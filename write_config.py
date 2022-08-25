import sys

from config import Config


def main():
    try:
        token = sys.argv[1]
        config = Config()
        config.token = token
        config.dump()
    except IndexError:
        print('Usage: write_config.py token')


if __name__ == '__main__':
    main()
