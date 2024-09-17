import os,sys
try:
    from selenium.common.exceptions import TimeoutException
    from selenium.common.exceptions import NoSuchElementException
    from colorama import Fore,Style
    from discordwebhook import Discord
    from Modules.Usage import ProgramUsage
except ImportError:
    print('Installing Libraries...')
    os.system("pip install -r requirements.txt")
    print('Libraries installed. Restart the program!')
    sys.exit()
class Handler:
    def info_banner(views,shares,likes,AMOUNT,INFO,creator,TYPE):
        views_multi = views + (1000 * AMOUNT) if views else '----'
        shares_multi = shares + (50 * AMOUNT) if shares else '----'
        favorites_multi = 0 + (100 * AMOUNT) if shares else '----'
        hearts_multi = likes + (10 * AMOUNT) if likes else '----'

        os.system("cls")
        views_extra = f"(Based on .cfg file you'll end up with {Style.BRIGHT}{Fore.GREEN}{views_multi} views) {Fore.LIGHTMAGENTA_EX}(Est. {ProgramUsage.convert_hours(round(AMOUNT * 2 / 60, 2))}){Fore.WHITE} "
        shares_extra = f"(Based on .cfg file you'll end up with {Style.BRIGHT}{Fore.GREEN}{shares_multi} shares) {Fore.LIGHTMAGENTA_EX}(Est. {ProgramUsage.convert_hours(round(AMOUNT * 2 / 60, 2))}){Fore.WHITE} "
        favorites_extra = f"(I can't Gather Favorites but you'll get + {Style.BRIGHT}{Fore.GREEN}{favorites_multi} Favorites) {Fore.LIGHTMAGENTA_EX}(Est. {ProgramUsage.convert_hours(round(AMOUNT * 2 / 60, 2))}){Fore.WHITE} "
        hearts_extra = f"(Based on .cfg file you'll end up with {Style.BRIGHT}{Fore.GREEN}{hearts_multi} hearts) {Fore.LIGHTMAGENTA_EX}(Est. {ProgramUsage.convert_hours(round(AMOUNT * 14 / 60, 2))}){Fore.WHITE} "
        print(f"""{INFO}{Style.BRIGHT}{Fore.WHITE}Video Info
        {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}- Creator : {Style.RESET_ALL}{Fore.WHITE}{creator}
        {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}- Views : {Fore.WHITE}{views} {Style.RESET_ALL} {views_extra if TYPE == 'views' else ''}
        {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}- Likes : {Style.RESET_ALL}{Fore.WHITE}{likes} {hearts_extra if TYPE == 'hearts' else ''}
        {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}- Shares : {Style.RESET_ALL}{Fore.WHITE}{shares} {shares_extra if TYPE == 'shares' else ''}
        {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}- Favorites : {Style.RESET_ALL}{Fore.WHITE}--- {favorites_extra if TYPE == 'favorites' else ''}
        {Style.RESET_ALL}""")

    def webhook_banner(webhook,each_views,TYPE,msg):
        print(f"""
                {Fore.BLUE}Program Configuration (Select an Option){Style.RESET_ALL}

                {Fore.GREEN}[1] {Fore.BLACK}-{Fore.MAGENTA} Webhook [{Fore.RESET}{str(webhook)}{Fore.MAGENTA}]{Fore.RESET}
                {Fore.GREEN}[2] {Fore.BLACK}-{Fore.MAGENTA} Test Webhook
                {Fore.GREEN}[3] {Fore.BLACK}-{Fore.MAGENTA} Warn Each {Fore.RESET}{each_views}{Fore.MAGENTA} {TYPE}
                {Fore.GREEN}[4] {Fore.BLACK}-{Fore.MAGENTA} Message [{Fore.RESET}{msg}{Fore.MAGENTA}]{Fore.RESET}

                {Fore.GREEN}[5] {Fore.BLACK}-{Fore.LIGHTYELLOW_EX} Save Current Config{Fore.RESET}

                {Fore.GREEN}[99] {Fore.BLACK}-{Fore.LIGHTYELLOW_EX} Start!{Fore.RESET}

                """)