from os import environ as env

def main():
    load_env_file()
    print(f"{env.get('MSG1')}, {env.get('MSG2')}!")


def load_env_file():
    with open(".env", "r") as env_file:
        for line in env_file:
            if "=" in line:
                key, value = line.strip().split("=", 1)
                env[key] = value


if __name__ == '__main__':
    main()
