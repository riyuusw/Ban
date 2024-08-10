from banana import Banana, print_timestamp
from colorama import Fore, Style, init
from time import sleep
import sys


def main():
    init(autoreset=True)

    ban = Banana()
    tokens = ban.login()
    for index, token in enumerate(tokens):
        get_user = ban.get_user_info(token=token)

        print_timestamp(
            f"{Fore.CYAN + Style.BRIGHT}[ {get_user['data']['username']} 🤖 ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
            f"{Fore.YELLOW + Style.BRIGHT}[ Peel {get_user['data']['peel']} 🍌 ]{Style.RESET_ALL}"
            f"{Fore.WHITE + Style.BRIGHT} | {Style.RESET_ALL}"
            f"{Fore.GREEN + Style.BRIGHT}[ USDT {get_user['data']['usdt']} 🤑 ]{Style.RESET_ALL}"
        )

        if get_user['data']['max_click_count'] > get_user['data']['today_click_count']:
            ban.do_click(token=token, click_count=get_user['data']['max_click_count'] - get_user['data']['today_click_count'])
        else:
            print_timestamp(f"{Fore.RED + Style.BRIGHT}[ Out Of Clicks, Banana Break 😋 ]{Style.RESET_ALL}")

        ban.get_lottery_info(token=token)
        lottery = ban.get_user_info(token=token)
        if lottery['data']['lottery_info']['remain_lottery_count'] != 0:
            while lottery['data']['lottery_info']['remain_lottery_count'] > 0:
                ban.do_lottery(token=token)
                lottery['data']['lottery_info']['remain_lottery_count'] -= 1
        else:
            print_timestamp(f"{Fore.RED + Style.BRIGHT}[ You Need More Harvest! 💩 ]{Style.RESET_ALL}")

        ban.get_banana_list(token=token)

    for _ in range(30 * 60, 0, -1):
        hours, remainder = divmod(_, 3600)
        minutes, seconds = divmod(remainder, 60)
        print(f"{Fore.YELLOW + Style.BRIGHT}[ {int(hours)} Hours {int(minutes)} Minutes {int(seconds)} Seconds Remaining To Process All Account ]{Style.RESET_ALL}", end="\r", flush=True)
        sleep(1)

    print('')


if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            continue
        except KeyboardInterrupt:
            sys.exit(0)