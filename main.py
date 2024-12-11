import time
import configparser
import os
import sys
import zipfile
import tempfile
import webbrowser
from Static.Static import Static
from Modules.Usage import ProgramUsage
from Modules.BannersHandler import Handler
from Static.InitialInfo import InitialInfo
try:
    import hashlib
    import requests
    from tqdm import tqdm
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import pytesseract
    from PIL import Image
    from fake_headers import Headers
    import re
    from colorama import Fore, Style
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.common.exceptions import TimeoutException
    from selenium.common.exceptions import NoSuchElementException
    from selenium.common.exceptions import ElementNotInteractableException
    from datetime import datetime, timedelta
    from discordwebhook import Discord
    from Modules.VideoInfo import TikTokVideoInfo
    import uuid
except Exception as e:
    print(e)
    input()

# Configurations
config = configparser.ConfigParser()
config.read('config.cfg')

TYPE = config.get('Settings', 'TYPE')
VIDEO = config.get('Settings', 'VIDEO_URL')
if re.match(r'^https://tiktok\.com/', VIDEO):
    VIDEO = VIDEO.replace('https://tiktok.com/', 'https://www.tiktok.com/')
AMOUNT = config.getint('Settings', 'AMOUNT')
WEBHOOK = config.get('Settings', 'WEBHOOK')
EACH_VIEWS = config.getint('Settings', 'EACH_VIEWS')
MESSAGE = config.get('Settings', 'MESSAGE')

WAITING = f"{Fore.YELLOW}[WAITING] "
SUCCESS = f"{Fore.GREEN}[SUCCESS] "
INFO = f"{Fore.BLUE}[INFO] "
WARNING = f"{Fore.RED}[WARNING] "

SLEEP = 15
SKIP_WEBHOOK_VERIFICATION = config.getboolean('Settings', 'SKIP_WEBHOOK_CONFIGURATION')

def  is_first_run():
    """Check if it's the first run of the program"""
    file_path = os.path.join(tempfile.gettempdir(), 'Ttkbooster.txt')
    if not os.path.isfile(file_path):
        with open(file_path, "w") as file:
            file.write("Don't Worry, this isn't a virus, just a check to see if it's your first time. :)")
        print(f"{INFO}First Time Detected. Welcome! (This won't appear anymore){Style.RESET_ALL}")
        webbrowser.open("https://discord.gg/sneez")

def show_credits():
    """Display program credits"""
    print(f"{INFO}{Fore.BLUE}{ProgramUsage.Translations("credits",0)}{Fore.CYAN}Sneezedip.{Style.RESET_ALL}")
    print(f"{INFO}{Fore.BLUE}{ProgramUsage.Translations("credits",1)}{Fore.GREEN}"
          f"https://discord.gg/sneez{Style.RESET_ALL}")


def parse_cooldown(text):
    """Parse cooldown time from text"""
    minutes = 0
    seconds = 0

    minute_match = re.search(r'(\d+)\s*minute', text)
    if minute_match:
        minutes = int(minute_match.group(1))

    second_match = re.search(r'(\d+)\s*second', text)
    if second_match:
        seconds = int(second_match.group(1))

    return minutes * 60 + seconds



def check_version(current_version):
    """Check if a new version of the program is available"""
    response = requests.get("https://raw.githubusercontent.com/Sneezedip/Tiktok-Booster/main/VERSION")
    if response.text.strip() != current_version:
        while True:
            u = input(f"{datetime.now().strftime('%H:%M:%S')} {WARNING}{Fore.WHITE}"
                      f"{ProgramUsage.Translations("updates",0)}{Style.RESET_ALL}").lower()
            if u == "y":
                ProgramUsage.download(INFO,WAITING,SUCCESS,WARNING,"https://codeload.github.com/Sneezedip/Tiktok-Booster/zip/refs/heads/main", "./")
                sys.exit()
            elif u == "n":
                return


if not os.path.exists('Tesseract'):
    print(f'{INFO}{Fore.WHITE}{ProgramUsage.Translations("credits",1)}{Style.RESET_ALL}', end="\r")
    url = 'https://drive.usercontent.google.com/download?id=10X_TEAwUic4v3pt7TT4w3QNRcS1DNq87&export=download&authuser=0&confirm=t&uuid=19bcdcbd-e7ce-4617-8f41-caca15b5ab17&at=APZUnTWgmGxytaTOOxw-o87dMp8z%3A1720311459869'
    extract_to = './'
    ProgramUsage.download(INFO,WAITING,SUCCESS,WARNING,url, extract_to)


class TikTokBooster:
    def __init__(self):
        self.history_selected = None
        global VIDEO
        self.elements = []
        while True:
            self.history = ProgramUsage.get_history()
            if not self.history:
                break
            else:
                print(f"\n{Fore.YELLOW}{ProgramUsage.Translations("history",0)}{Fore.RESET}")
                for index, record in enumerate(self.history, start=1):
                    if isinstance(record, dict):
                        print(f"\n{Fore.CYAN}[{index}] {Fore.WHITE}{Style.BRIGHT}Video Link: {Style.RESET_ALL}https://www.tiktok.com/@{record["creator"]}/video/{record["video_id"]}\n"
                            f"{Fore.WHITE}{Style.BRIGHT}Creator: {Style.RESET_ALL}{record['creator']} \n"
                            f"{Fore.WHITE}{Style.BRIGHT}Views: {Style.RESET_ALL}{Fore.LIGHTYELLOW_EX}{record['views_before']} {Fore.WHITE}-> {Fore.GREEN}{record['views_after']} {Fore.RESET}\n"
                            f"{Fore.WHITE}{Style.BRIGHT}Last Time Used: {Style.RESET_ALL}{record['last_time_used']}{Fore.RESET}")
                        
                try:
                    choice = int(input(f"\n{ProgramUsage.Translations("history",1)}{Fore.RED} {ProgramUsage.Translations("history",2)} {Style.RESET_ALL}"))
                    if choice == 0:
                        self.history_selected = False
                        VIDEO = ""
                        break
                    if 1 <= choice <= len(self.history):
                        self.history_selected = True
                        VIDEO = f"https://www.tiktok.com/@{self.history[choice - 1]["creator"]}/video/{self.history[choice - 1]["video_id"]}"
                        break
                    else:
                        print(f"{ProgramUsage.Translations("errors",0)}")
                except ValueError:
                    print(f"{ProgramUsage.Translations("errors",1)}")
        while True:
            try:
                self.tiktok_info = TikTokVideoInfo(VIDEO)
                ProgramUsage.change_video_url(VIDEO)
                break
            except ValueError:
                os.system("cls") if os.name == 'nt' else os.system("clear")
                if self.history_selected == None:
                    print(f"{WARNING}{ProgramUsage.Translations("errors",2)}{Fore.BLUE}\nOLD URL : {Fore.WHITE}{VIDEO}")
                VIDEO = input(f"{Fore.BLUE}{ProgramUsage.Translations("errors",3)}{Fore.WHITE}")
        self.counter = 0
        self.webhook = WEBHOOK
        self.webhook_text = WEBHOOK
        self.each_views = EACH_VIEWS
        try:
            self.message = MESSAGE.format(self.each_views)
        except KeyError:
            self.message = MESSAGE
        self.webhook = Discord(url=self.webhook)
        if not SKIP_WEBHOOK_VERIFICATION:
            self._menu()
        self.index = 0
        self.video_id = VIDEO.split("/")[5] if ProgramUsage.check_video(VIDEO) == "www" else ProgramUsage.get_vmid(VIDEO)
        self.initial_views = self._get_initial_views()

        self.options = webdriver.ChromeOptions()
        for option in Static.ChromeOptions:
            self.options.add_argument(option)
        if config.getboolean('Settings', 'HEADLESS'):
            self.options.add_argument("--headless=old")

        self.driver = webdriver.Chrome(options=self.options)


        self.driver.get('https://zefoy.com/')

        time.sleep(2)

        pytesseract.pytesseract.tesseract_cmd = r'Tesseract/tesseract.exe'
        try:
            WebDriverWait(self.driver, SLEEP).until(ec.presence_of_element_located(
                (By.XPATH, '/html/body/div[8]/div[2]/div[2]/div[3]/div[2]/button[1]'))).click()
        except (TimeoutException, NoSuchElementException):
            pass
        
        try:
            self.webhook.post(content="Tiktok-Booster Started!") # Quick check on webhook
            self.is_webhook_valid = True    
        except (TimeoutException):
            self.is_webhook_valid = False

        while not self._handle_captcha():
            self.driver.refresh()
            time.sleep(1)
        self._check_available()
        self._show_typeconfig()
        self._show_menu()
        time.sleep(1)
        self._select_type()

    def _get_initial_views(self):
        """Get initial views based on the type"""
        if TYPE == 'views':
            return ProgramUsage.get_numeric_value(self.tiktok_info.get_video_info(Views=True))
        elif TYPE == 'shares':
            return ProgramUsage.get_numeric_value(self.tiktok_info.get_video_info(Shares=True))
        elif TYPE == 'hearts':
            return ProgramUsage.get_numeric_value(self.tiktok_info.get_video_info(Likes=True))
        elif TYPE == 'favorites':
            return 0

    def _check_available(self):
        """Check if the required features are available"""
        # available = False
        for type,xpath in Static.typeValues.items():
            if WebDriverWait(self.driver, SLEEP).until(ec.presence_of_element_located(
                (By.XPATH, xpath))).is_enabled():
                self.elements.append(type)

    def _handle_captcha(self):
        """Handle the captcha on the page"""
        with open('Captcha/captcha.png', 'wb') as file:
            file.write(WebDriverWait(self.driver, SLEEP).until(ec.presence_of_element_located(
                (By.XPATH, '/html/body/div[5]/div[2]/form/div/div/img'))).screenshot_as_png)
        try:
            WebDriverWait(self.driver, SLEEP).until(
                ec.presence_of_element_located((By.XPATH, '/html/body/div[5]/div[2]/form/div/div/div/input'))).send_keys(
                pytesseract.image_to_string(Image.open('Captcha/captcha.png')))
        except (ElementNotInteractableException):
            self._reset_browser()
        print(f"{datetime.now().strftime('%H:%M:%S')} {WAITING}{Fore.WHITE}{ProgramUsage.Translations("main",0)}"
              f"{Style.RESET_ALL}", end="\r")
        return self._is_captcha_passed()

    def _is_captcha_passed(self):
        """Check if captcha was passed successfully"""
        try:
            WebDriverWait(self.driver, SLEEP).until(
                ec.presence_of_element_located((By.ID, 'errorcapthcaclose'))).click()
            return False
        except (TimeoutException, NoSuchElementException):
            return True

    def _reset_browser(self):
        """Closes and restarts the browser."""
        try:
            self.driver.quit()  # Close the current session
        except Exception as e:
            print(f"{WARNING}Error while closing the browser: {e}")

        # Create a new instance of the browser
        self.driver = webdriver.Chrome(options=self.options)

        # Log back in to the site
        self.driver.get('https://zefoy.com/')
        pytesseract.pytesseract.tesseract_cmd = r'Tesseract/tesseract.exe'
        try:
            WebDriverWait(self.driver, SLEEP).until(ec.presence_of_element_located(
                (By.XPATH, '/html/body/div[8]/div[2]/div[1]/div[3]/div[2]/button[1]'))).click()
        except (TimeoutException, NoSuchElementException):
            pass

        while not self._handle_captcha():
            self.driver.refresh()
            time.sleep(1)
        time.sleep(1)
        self._check_available()

    def _select_type(self):
        """Select the type of action to perform"""
        max_retries = 3
        retries = 0

        while retries < max_retries:
            try:
                WebDriverWait(self.driver, SLEEP).until(
                    ec.presence_of_element_located((By.XPATH, Static.typeValues[TYPE]))).click()
                time.sleep(0.3)
                self._get_views()
                break
            except (TimeoutException, NoSuchElementException) as e:
                retries += 1
                print(f"{WARNING}Unable to find the button for {TYPE}.. Retrying.. (retry {retries}/{max_retries})")
                print(f"Exception details: {e}")
                time.sleep(2 ** retries)  # exponential backoff
                if retries >= max_retries:
                    print(f"{WARNING} Max retries reached. Resetting the browser...")
                    self._reset_browser()
                    retries = 0  # Reset the retry counter after resetting the browser

    def _get_views(self):
        """Perform the main action of getting views, shares, etc."""
        max_retries = 3
        retries = 0

        while retries < max_retries:
            try:
                time.sleep(0.5)
                WebDriverWait(self.driver, SLEEP).until(
                    ec.presence_of_element_located((By.XPATH, Static.firstStep[TYPE]))).send_keys(VIDEO)

                for _ in range(AMOUNT):
                    os.system("cls") if os.name == 'nt' else os.system("clear")
                    self._show_banner(self.index)
                    time.sleep(0.5)
                    WebDriverWait(self.driver, SLEEP).until(
                        ec.presence_of_element_located((By.XPATH, Static.secondStep[TYPE]))).click()
                    time.sleep(3)

                    try:
                        element = WebDriverWait(self.driver, SLEEP).until(
                            ec.presence_of_element_located((By.XPATH, Static.thirdStep[TYPE]))
                        )
                        text = element.text
                        if text:
                            total_seconds = parse_cooldown(text)

                            if total_seconds > 0:
                                while total_seconds > 0:
                                    minutes, seconds = divmod(total_seconds, 60)
                                    print(
                                        f"\r{WAITING} {ProgramUsage.Translations("main",1)} {minutes} {ProgramUsage.Translations("main",2)} {seconds} {ProgramUsage.Translations("main",3)} "
                                        f"{Style.RESET_ALL}", end='')
                                    time.sleep(1)
                                    total_seconds -= 1
                                print()
                                ProgramUsage.t()

                    except Exception as e:
                        print(f"{WARNING}An exception occurred: {e}")
                        continue

                    time.sleep(2)
                    WebDriverWait(self.driver, SLEEP).until(
                        ec.presence_of_element_located((By.XPATH, Static.fourthStep[TYPE]))).click()
                    time.sleep(2)

                    try:
                        if not ProgramUsage.vk():
                            os.system("cls") if os.name == 'nt' else os.system("clear")  
                            print("No more uses. Contact Sneezedip.")
                            sys.exit()
                        WebDriverWait(self.driver, SLEEP).until(
                            ec.presence_of_element_located((By.XPATH, Static.finalButton[TYPE]))).click()

                        if TYPE == 'views':
                            print(
                                f"{datetime.now().strftime('%H:%M:%S')} {SUCCESS}{Fore.WHITE}{ProgramUsage.Translations("main",4)}"
                                f"{Style.RESET_ALL}")
                            self.counter += 1000
                        elif TYPE == 'shares':
                            print(
                                f"{datetime.now().strftime('%H:%M:%S')} {SUCCESS}{Fore.WHITE}{ProgramUsage.Translations("main",5)}"
                                f"{Style.RESET_ALL}")
                            self.counter += 50
                        elif TYPE == 'favorites':
                            print(f"{datetime.now().strftime('%H:%M:%S')} {SUCCESS}{Fore.WHITE}{ProgramUsage.Translations("main",6)}"
                                f"{Style.RESET_ALL}")
                            self.counter += 100
                        elif TYPE == 'hearts':
                            print(
                                f"{datetime.now().strftime('%H:%M:%S')} {SUCCESS}{Fore.WHITE}{ProgramUsage.Translations("main",7)}"
                                f"{Style.RESET_ALL}")
                            self.counter += 10

                        if self.is_webhook_valid:
                            if self.counter >= self.each_views:
                                self.webhook.post(content=self.message)
                                self.counter = 0

                    except Exception as e:
                        if "element click intercepted" in str(e).lower():
                            print(f"{Fore.RED}[Error] {Style.RESET_ALL} "
                                  f"Program couldn't proceed. Restart the program and if the error persists, "
                                  f"please set HEADLESS to False in the config.cfg file. (ERROR 000)")
                        else:
                            print(f"{Fore.RED}[Error] Browser handling error, restart the program..."
                                  f"{Style.RESET_ALL}An exception occurred: {e}")
                        self.driver.refresh()
                        time.sleep(2)
                        self._select_type()

                    self.index += 1
                    time.sleep(3)

                break  # If everything went well, break the loop

            except TypeError as te:
                print(f"{WARNING} A TypeError occurred: {te}. Retrying... (Attempt {retries + 1}/{max_retries})")
                retries += 1
                if retries >= max_retries:
                    print(f"{WARNING} Failed after {max_retries} attempts. Exiting.")
                    sys.exit(1)  # Exit the program or handle it as required

    def _is_ready(self):
        """Check if the system is ready to perform the action"""
        return WebDriverWait(self.driver, SLEEP).until(
            ec.presence_of_element_located((By.XPATH, Static.readyValues[TYPE]))).text.__contains__('READY') or len(
            WebDriverWait(self.driver, SLEEP).until(
                ec.presence_of_element_located((By.XPATH, Static.readyValues[TYPE]))).text) <= 0
    def _show_typeconfig(self):
        global TYPE
        us = 0
        def available_color(type):
            if type in self.elements:
                return Fore.GREEN
            return Fore.RED
        """Show the program configuration menu"""
        os.system("cls") if os.name == 'nt' else os.system("clear")
        print("Type Configuration : \n")
        print(f"{available_color('views')}[{'1' if available_color('views') == Fore.GREEN else '-'}] {'Views'} {f'[{ProgramUsage.Translations("main",9)}]' if TYPE.lower() == 'views' else ''}")
        print(f"{available_color('followers')}[{'2' if available_color('followers') == Fore.GREEN else '-'}] {'Followers'} {f'[{ProgramUsage.Translations("main",9)}]' if TYPE.lower() == 'followers' else ''}")
        print(f"{available_color('favorites')}[{'3' if available_color('favorites') == Fore.GREEN else '-'}] {'Favorites'} {f'[{ProgramUsage.Translations("main",9)}]' if TYPE.lower() == 'favorites' else ''}")
        print(f"{available_color('shares')}[{'4' if available_color('shares') == Fore.GREEN else '-'}] {'Shares'} {f'[{ProgramUsage.Translations("main",9)}]' if TYPE.lower() == 'shares' else ''}")
        print(f"{available_color('hearts')}[{'5' if available_color('hearts') == Fore.GREEN else '-'}] {'Hearts'} {f'[{ProgramUsage.Translations("main",9)}]' if TYPE.lower() == 'hearts' else ''}")
        print(Fore.CYAN,f"\n[99] - {ProgramUsage.Translations("main",8)}!",Style.RESET_ALL)
        print("\n")
        while True:
            try:
                us = int(input(f"{WAITING}Select an option \n-> {Style.RESET_ALL}").lower())
                if us >= 1 and us <= 99:
                    if us >= 6 and us <= 98:
                        pass
                    else:
                        break
            except:
                pass
        match us:
            case 1: 
                if 'views' in self.elements:
                    TYPE = 'views'
            case 2:
                if 'followers' in self.elements: 
                    TYPE = 'followers'
            case 3:
                if 'favorites' in self.elements: 
                    TYPE = 'favorites'
            case 4:
                if 'shares' in self.elements: 
                    TYPE = 'shares'
            case 5:
                if 'hearts' in self.elements:
                    TYPE = 'hearts'
            case 99: return
        self._show_typeconfig()

    def _show_menu(self):
        """Show the program configuration menu"""
        os.system("cls") if os.name == 'nt' else os.system("clear")
        print(f"{datetime.now().strftime('%H:%M:%S')} {WAITING}{Fore.WHITE}Gathering Video Info...", end="\r")

        def _gather_info(info_type):
            try:
                if info_type == 'views':
                    return int(self.tiktok_info.get_video_info(Views=True))
                elif info_type == 'likes':
                    return int(self.tiktok_info.get_video_info(Likes=True))
                elif info_type == 'shares':
                    return int(self.tiktok_info.get_video_info(Shares=True))
                elif info_type == 'creator':
                    return self.tiktok_info.get_video_info(Creator=True)
            except ValueError:
                return 0
        InitialInfo.CREATOR = self.tiktok_info.get_video_info(Creator=True)
        InitialInfo.VIEWS_BEFORE = self.tiktok_info.get_video_info(Views=True)
        Handler.info_banner(_gather_info('views'),_gather_info('shares'),_gather_info('likes'),AMOUNT,INFO,_gather_info('creator'),TYPE) # Show Info Banner

        while True:
            us = input(f"{WAITING}Want to start? (y/n)\n-> {Style.RESET_ALL}").lower()
            if us == 'y':
                return
            elif us == 'n':
                sys.exit()

    def _show_banner(self, index):
        """Show the progress banner"""
        temp = TikTokVideoInfo(VIDEO)
        ProgramUsage.save_or_replace_history(self.video_id,InitialInfo.CREATOR,InitialInfo.VIEWS_BEFORE,ProgramUsage.get_numeric_value(temp.get_video_info(Views=True)),ProgramUsage.get_numeric_value(temp.get_video_info(Likes=True)),ProgramUsage.get_numeric_value(temp.get_video_info(Shares=True)))
        if TYPE == 'views':
            views = ProgramUsage.get_numeric_value(temp.get_video_info(Views=True))
            print(f"{INFO}[{round((index / AMOUNT) * 100, 1)}%] {Fore.WHITE}Video Views : {Fore.WHITE}{views} {Fore.GREEN}[+{int(views - self.initial_views)}] {Style.BRIGHT}{Fore.MAGENTA}(Est. {ProgramUsage.convert_hours(round((AMOUNT - index) * 2 / 60, 2))} Remaining.{Style.RESET_ALL})")
        if TYPE == 'shares':
            shares = ProgramUsage.get_numeric_value(temp.get_video_info(Shares=True))
            print(f"{INFO}[{round((index / AMOUNT) * 100, 1)}%] {Fore.WHITE}Video Shares : {Fore.WHITE}{shares} {Fore.GREEN}[+{int(shares - self.initial_views)}] {Style.BRIGHT}{Fore.MAGENTA}(Est. {ProgramUsage.convert_hours(round((AMOUNT - index) * 2 / 60, 2))} Remaining.{Style.RESET_ALL})")
        if TYPE == 'favorites':
            favorites = 0
            print(f"{INFO}[{round((index / AMOUNT) * 100, 1)}%] {Fore.WHITE}Video Favorites : {Fore.WHITE}{favorites} {Fore.GREEN}[+{self.counter}] {Style.BRIGHT}{Fore.MAGENTA}(Est. {ProgramUsage.convert_hours(round((AMOUNT - index) * 2 / 60, 2))} Remaining.{Style.RESET_ALL})")
        if TYPE == 'hearts':
            hearts = ProgramUsage.get_numeric_value(temp.get_video_info(Likes=True))
            print(
                f"{INFO}[{round((index / AMOUNT) * 100, 1)}%] {Fore.WHITE}Video Hearts : {Fore.WHITE}{hearts} {Fore.GREEN}[+{int(hearts - self.initial_views)}] {Style.BRIGHT}{Fore.MAGENTA}(Est. {ProgramUsage.convert_hours(round((AMOUNT - index) * 2 / 60, 2))} Remaining.{Style.RESET_ALL})")

    def _menu(self):
        """Program configuration menu"""
        while True:
            try:
                msg = self.message.format(self.each_views)
            except KeyError:
                msg = self.message
            os.system("cls") if os.name == 'nt' else os.system("clear")

            Handler.webhook_banner(self.webhook_text,self.each_views,TYPE,msg)

            try:
                user_input = int(input("-> "))

                if user_input in range(1, 6) or user_input == 99:
                    if user_input == 1:
                        self.webhook_text = input("Insert new -> ")
                        self.webhook = Discord(url=self.webhook_text)
                    if user_input == 2:
                        try:
                            self.webhook.post(content="**Test Message To Webhook From TikTok Booster**")
                            print(Fore.GREEN + "Valid!")
                        except (TimeoutException, NoSuchElementException):
                            print(Fore.RED + "Invalid Webhook!" + Style.RESET_ALL)
                            time.sleep(0.5)
                    if user_input == 3:
                        try:
                            self.each_views = int(input("Insert new -> "))
                        except ValueError:
                            pass
                    if user_input == 4:
                        self.message = input("Insert new -> ")
                        try:
                            msg = self.message.format(self.each_views)
                        except KeyError:
                            msg = self.message
                    if user_input == 5:
                        try:
                            config.set("Settings", "WEBHOOK", str(self.webhook))
                            config.set("Settings", "EACH_VIEWS", str(self.each_views))
                            config.set("Settings", "MESSAGE", str(self.message))
                            with open("config.cfg", "w") as configfile:
                                config.write(configfile)
                            print("Saved!")
                            time.sleep(1)
                        except Exception as e:
                            print(e)
                            input()
                    if user_input == 99:
                        break
            except ValueError:
                pass


if __name__ == "__main__":
    check_version("2.10.0")
    if not ProgramUsage.vk():
        os.system("cls") if os.name == 'nt' else os.system("clear")  
        print("No more uses. Contact Sneezedip.")
        sys.exit()
    os.system("cls") if os.name == 'nt' else os.system("clear")
    show_credits()
    is_first_run()
    TikTokBooster()
