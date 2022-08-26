import sys
import re


def inject_token(content: str, token: str) -> str:
    out = ''
    for line in content.split('\n'):
        if re.match(r'TOKEN\s+=\s+', line):
            out += f"TOKEN = '{token}'"
        else:
            out += line + '\n'
    return out


def main():
    try:
        token = sys.argv[1]

        if token:
            with open('./config.py', 'r') as cf_read:
                content = cf_read.read()
                content = inject_token(content, token)
                with open('./config.py', 'w') as cf_write:
                    cf_write.write(content)

                    print('[+] Injected')
    except IndexError:
        print('Usage: inject_token.py token')


if __name__ == '__main__':
    main()
