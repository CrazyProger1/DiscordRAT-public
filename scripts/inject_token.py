import sys


def main():
    token = sys.argv[1]

    if token:
        with open('config.py', 'r') as cf_read:
            content = cf_read.read()
            content.format(TOKEN=token)
            with open('config.py', 'w') as cf_write:
                cf_write.write(content)


if __name__ == '__main__':
    main()
