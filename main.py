import time,configparser,os,sys,zipfile,tempfile,webbrowser
from Static.Static import Static
try:
    import requests
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    import pytesseract
    from PIL import Image
    from fake_headers import Headers
    import re
    from colorama import Fore,Style
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from datetime import datetime,timedelta
    from discordwebhook import Discord
except:
    print('Installing Libraries...')
    os.system("pip install -r requirements.txt")
    print('Libraries installed. Restart the program!')
    sys.exit()

config = configparser.ConfigParser()
config.read('config.cfg')

TYPE = config.get('Settings','TYPE')
VIDEO = config.get('Settings','VIDEO_URL')
if re.match(r'^https://tiktok\.com/', VIDEO):
    VIDEO = VIDEO.replace('https://tiktok.com/', 'https://www.tiktok.com/')
AMOUNT = config.getint('Settings','AMOUNT')
WEBHOOK = config.get('Settings','WEBHOOK')
EACH_VIEWS = config.getint('Settings','EACH_VIEWS')
MESSAGE = config.get('Settings','MESSAGE')

WAITING= f"{Fore.YELLOW}[WAITING] "
SUCCESS = f"{Fore.GREEN}[SUCCESS] "
INFO = f"{Fore.BLUE}[INFO] "
WARNING = f"{Fore.RED}[WARNING] "

SLEEP = 15
def IsFirst():
    file_path = os.path.join(tempfile.gettempdir(), 'Ttkbooster.txt')
    file_exists = os.path.isfile(file_path)
    if file_exists:
        return
    else:
        with open(os.path.join(tempfile.gettempdir(), 'Ttkbooster.txt'),"w") as file:
            file.write("Don't Worry, this isn't a virus, just a check to see if it's your first time. :)")
            print(f"{INFO}First Time Detected. Welcome! (This won't appear anymore)")
        webbrowser.open("https://discord.gg/nAa5PyxubF")

def Credits():
    print(f"{INFO}{Fore.BLUE}Provided to you by {Fore.CYAN}Sneezedip.{Style.RESET_ALL}")
    print(f"{INFO}{Fore.BLUE}Join Our Discord For More Tools! {Fore.GREEN}https://discord.gg/nAa5PyxubF{Style.RESET_ALL}")

def Download(url, extract_to='.'):
    response = requests.get(url)
    zip_path = os.path.join(extract_to, "downloaded_file.zip")
    with open(zip_path, 'wb') as file:
        file.write(response.content)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    os.remove(zip_path)
def CheckVersion(current_version):
    response = requests.get("https://raw.githubusercontent.com/Sneezedip/Tiktok-Booster/main/VERSION")
    if response.text.strip() != current_version:
        while True:
            u = input(f"{datetime.now().strftime("%H:%M:%S")} {WARNING}{Fore.WHITE}NEW VERSION FOUND. Want to update? (y/n){Style.RESET_ALL}").lower()
            if u == "y":
                print(f"{datetime.now().strftime("%H:%M:%S")} {WAITING}Updating...{Style.RESET_ALL}")
                Download("https://codeload.github.com/Sneezedip/Tiktok-Booster/zip/refs/heads/main","./")
                print(f"{datetime.now().strftime("%H:%M:%S")} {INFO}Updated. Check the new folder created.{Style.RESET_ALL}")
                sys.exit()
            elif u == "n":
                return
if not os.path.exists('Tesseract'):
    print(f'{INFO}{Fore.WHITE}Downloading Tesseract, please wait..{Style.RESET_ALL}')
    url = 'https://drive.usercontent.google.com/download?id=10X_TEAwUic4v3pt7TT4w3QNRcS1DNq87&export=download&authuser=0&confirm=t&uuid=19bcdcbd-e7ce-4617-8f41-caca15b5ab17&at=APZUnTWgmGxytaTOOxw-o87dMp8z%3A1720311459869'
    extract_to = './'
    Download(url, extract_to)

class Program():
    def __init__(self):
        self.COUNTER2 = 0
        self.WEBHOOK = WEBHOOK
        self.EACH_VIEWS = EACH_VIEWS
        try:
            self.MESSAGE = MESSAGE.format(self.EACH_VIEWS)
        except:
            self.MESSAGE = MESSAGE
        self.Webhook = Discord(url=self.WEBHOOK)
        self._menu()
        self.INDEX = 0
        self.VIDEOID = VIDEO.split("/")[5] if self._checkVideo() == "www" else self._getVMID()
        if TYPE == 'views':
            self.INITIALVIEWS = self._getvideoInfo(Views=True)
        elif TYPE == 'shares':
            self.INITIALVIEWS = self._getvideoInfo(Shares=True)
        elif TYPE == 'favorites':
            self.INITIALVIEWS = '0'
        if self.INITIALVIEWS == 'Unable to gather.':
            self.INITIALVIEWS = 0
        self.Options = webdriver.ChromeOptions()
        for option in Static.ChromeOptions:
            self.Options.add_argument(option)
        if config.getboolean('Settings','HEADLESS'): self.Options.add_argument("--headless")
        print(f'\n{datetime.now().strftime("%H:%M:%S")} {WAITING}{Fore.WHITE}Installing Extensions...{Style.RESET_ALL}',end="\r")
        self.Options.add_extension('Extensions/ub.crx')
        print(f"{datetime.now().strftime("%H:%M:%S")} {SUCCESS}{Fore.WHITE}Extensions Installed Sucessfully!{Style.RESET_ALL}")
        self.driver = webdriver.Chrome(options=self.Options)

        self._showMenu()

        self.driver.get('https://zefoy.com/')
        pytesseract.pytesseract.tesseract_cmd = r'Tesseract/tesseract.exe'
        try:
            WebDriverWait(self.driver, SLEEP).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[8]/div[2]/div[1]/div[3]/div[2]/button[1]'))).click()
        except:
            pass
        time.sleep(0.5)
        

        while not self.PassCaptcha():
            self.driver.refresh()
            time.sleep(1.5)
            continue
        time.sleep(3)
        self.SelectType()

    def PassCaptcha(self):
        with open('Captcha/captcha.png', 'wb') as file:
            file.write(WebDriverWait(self.driver, SLEEP).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[2]/form/div/div/img'))).screenshot_as_png)
        WebDriverWait(self.driver, SLEEP).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[5]/div[2]/form/div/div/div/input'))).send_keys(pytesseract.image_to_string(Image.open('Captcha/captcha.png')))
        print(f"{datetime.now().strftime("%H:%M:%S")} {WAITING}{Fore.WHITE}Passing Captcha..{Style.RESET_ALL}",end="\r")
        if self.PassedCaptcha():
            print(F"{datetime.now().strftime("%H:%M:%S")} {SUCCESS}{Fore.WHITE}Captcha Passed Successfully!{Style.RESET_ALL}")
            return True
        return False
    def PassedCaptcha(self):
        try:
            WebDriverWait(self.driver, SLEEP).until(EC.presence_of_element_located((By.ID,'errorcapthcaclose'))).click()
            return False
        except:
            return True
        
    def SelectType(self):
        WebDriverWait(self.driver, SLEEP).until(EC.presence_of_element_located((By.XPATH,Static.typeValues[TYPE]))).click()
        time.sleep(0.3)
        self.GetViews()

    def GetViews(self):
        time.sleep(0.5)
        WebDriverWait(self.driver, SLEEP).until(EC.presence_of_element_located((By.XPATH,Static.firstStep[TYPE]))).send_keys(VIDEO)
        for _ in range(AMOUNT):
            os.system("cls") if os.name == 'nt' else os.system("clear")
            self._banner(self.INDEX)
            time.sleep(0.5)
            WebDriverWait(self.driver, SLEEP).until(EC.presence_of_element_located((By.XPATH,Static.secondStep[TYPE]))).click()
            time.sleep(3)
            try:
                element = WebDriverWait(self.driver, SLEEP).until(
                   EC.presence_of_element_located((By.XPATH, Static.thirdStep[TYPE]))
                )
                text = element.text
                if text:
                  print(f"{Fore.RED}[Error] {Style.RESET_ALL}{text}")
            except:
               pass
            waiting_timer = 0
            while True:
                if not self.isReady():
                    print(f"{datetime.now().strftime("%H:%M:%S")} {WAITING}{Fore.WHITE}Waiting Timer... (x{waiting_timer}){Style.RESET_ALL}",end="\r")
                    time.sleep(3)
                    waiting_timer += 1
                    if waiting_timer >= 70:
                        print(f"{datetime.now().strftime("%H:%M:%S")} {WARNING}Program is waiting for more than 5 minutes. Check Video Link!{Style.RESET_ALL}")
                        sys.exit()
                else:
                    time.sleep(1.5)
                    break
            waiting_timer = 0
            time.sleep(2)
            WebDriverWait(self.driver, SLEEP).until(EC.presence_of_element_located((By.XPATH,Static.fourthStep[TYPE]))).click()
            time.sleep(2)
            try:
                WebDriverWait(self.driver, SLEEP).until(EC.presence_of_element_located((By.XPATH,Static.finalButton[TYPE]))).click()
                if TYPE == 'views':print(F"{datetime.now().strftime("%H:%M:%S")} {SUCCESS}{Fore.WHITE}+1000 Views Added Successfully!{Style.RESET_ALL}")
                if TYPE == 'shares':print(F"{datetime.now().strftime("%H:%M:%S")} {SUCCESS}{Fore.WHITE}+50 Shares Added Successfully!{Style.RESET_ALL}")
                if TYPE == 'favorites':print(F"{datetime.now().strftime("%H:%M:%S")} {SUCCESS}{Fore.WHITE}+100 Favorites Added Successfully!{Style.RESET_ALL}")
                if TYPE == 'views': self.COUNTER2 += 1000
                if TYPE == 'shares': self.COUNTER2 += 50
                if TYPE == 'favorites': self.COUNTER2 += 100
                if self.COUNTER2 >= self.EACH_VIEWS:
                    self.Webhook.post(content=self.MESSAGE)
                    self.COUNTER2 = 0
            except:
                self.driver.refresh()
                time.sleep(2)
                self.SelectType()
            self.INDEX += 1
            time.sleep(3)
    def isReady(self):
         return WebDriverWait(self.driver, SLEEP).until(EC.presence_of_element_located((By.XPATH,Static.readyValues[TYPE]))).text.__contains__('READY') or len(WebDriverWait(self.driver, SLEEP).until(EC.presence_of_element_located((By.XPATH,Static.readyValues[TYPE]))).text) <= 0
    def _showMenu(self):
        os.system("cls") if os.name == 'nt' else os.system("clear")
        print(f"{datetime.now().strftime("%H:%M:%S")} {WAITING}{Fore.WHITE}Gathering Video Info...",end="\r")
        def _gather(type):
            try:
                if type == 'views':
                    return int(self._getvideoInfo(Views=True))
                elif type == 'likes':
                    return int(self._getvideoInfo(Likes=True))
                elif type == 'shares':
                    return int(self._getvideoInfo(Shares=True))
                elif type == 'creator':
                    return self._getvideoInfo(Creator=True)
            except:
                return 'Unable to Gather'
        creator = _gather('creator')
        views = _gather('views')
        likes = _gather('likes')
        shares = _gather('shares')
        try:
            viewsMulti = int(views) + (1000*AMOUNT)
        except: viewsMulti = '----'
        try:
            sharesMulti = int(shares) + (50*AMOUNT)
        except: sharesMulti = '----'
        try:
            favoritesMulti = 0 + (100*AMOUNT)
        except: favoritesMulti = '----'
        os.system("cls")
        views_extra = f"(Based on .cfg file you'll end up with {Style.BRIGHT}{Fore.GREEN}{viewsMulti} views) {Fore.LIGHTMAGENTA_EX}(Est. {self._convertHours(round(AMOUNT * 2 / 60,2))}){Fore.WHITE} "
        shares_extra = f"(Based on .cfg file you'll end up with {Style.BRIGHT}{Fore.GREEN}{sharesMulti} shares) {Fore.LIGHTMAGENTA_EX}(Est. {self._convertHours(round(AMOUNT * 2 / 60,2))}){Fore.WHITE} "
        favorites_extra = f"(I can't Gather Favorites but you'll get + {Style.BRIGHT}{Fore.GREEN}{favoritesMulti} Favorites) {Fore.LIGHTMAGENTA_EX}(Est. {self._convertHours(round(AMOUNT * 2 / 60,2))}){Fore.WHITE} "
        print(f"""{INFO}{Style.BRIGHT}{Fore.WHITE}Video Info
    {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}- Creator : {Style.RESET_ALL}{Fore.WHITE}{creator}
    {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}- Views : {Fore.WHITE}{views} {Style.RESET_ALL} {views_extra if TYPE == 'views' else ''}
    {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}- Likes : {Style.RESET_ALL}{Fore.WHITE}{likes}
    {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}- Shares : {Style.RESET_ALL}{Fore.WHITE}{shares} {shares_extra if TYPE == 'shares' else ''}
    {Style.BRIGHT}{Fore.LIGHTYELLOW_EX}- Favorites : {Style.RESET_ALL}{Fore.WHITE}--- {favorites_extra if TYPE == 'favorites' else ''}
                {Style.RESET_ALL}""")
        while True:
            us = input(f"{WAITING}Want to start? (y/n)\n-> {Style.RESET_ALL}").lower()
            if us == 'y':
                return
            elif us == 'n':
                sys.exit()
        
    def _banner(self,I):
        if TYPE == 'views' : views = self._getvideoInfo(Views = True)
        if TYPE == 'views' : print(f"{INFO}[{round((I/AMOUNT)*100,1)}%] {Fore.WHITE}Video Views : {Fore.WHITE}{views} {Fore.GREEN}[+{int(views-self.INITIALVIEWS)}] {Style.BRIGHT}{Fore.MAGENTA}(Est. {self._convertHours(round((AMOUNT-I) * 2 / 60,2))} Remaining.{Style.RESET_ALL})")
        if TYPE == 'shares' : shares = self._getvideoInfo(Shares = True)
        if TYPE == 'shares' : print(f"{INFO}[{round((I/AMOUNT)*100,1)}%] {Fore.WHITE}Video Shares : {Fore.WHITE}{shares} {Fore.GREEN}[+{int(shares-self.INITIALVIEWS)}] {Style.BRIGHT}{Fore.MAGENTA}(Est. {self._convertHours(round((AMOUNT-I) * 2 / 60,2))} Remaining.{Style.RESET_ALL})")
        if TYPE == 'favorites' : favorites = 0
        if TYPE == 'favorites' : print(f"{INFO}[{round((I/AMOUNT)*100,1)}%] {Fore.WHITE}Video Favorites : {Fore.WHITE}{favorites} {Fore.GREEN}[+{self.COUNTER2}] {Style.BRIGHT}{Fore.MAGENTA}(Est. {self._convertHours(round((AMOUNT-I) * 2 / 60,2))} Remaining.{Style.RESET_ALL})")
    def _checkVideo(self):
        if VIDEO.split("/")[2].__contains__("vm"):
            return "vm"
        return "www"
    def _getVMID(self):
        response = requests.post("https://countik.com/api/video/exist",json={'url': f"{VIDEO}"}).json()
        try:
            return response['id']
        except:
            print(f"{WARNING}Unable to get Video ID{Style.RESET_ALL}")
            return
    def _getvideoInfo(self,Creator = False,Views = False,Likes = False,Shares = False):
        retry = 0
        while True:
            if retry > 5:
                break
            try:
                response = requests.get(f"https://countik.com/api/videoinfo/{self.VIDEOID}").json()
            except:
                retry += 1
                continue
            try:
                if Creator : return response['creator']
                elif Views : return response['plays']
                elif Likes : return response['likes']
                elif Shares : return response['shares']
            except :
                retry += 1
        return "Unable to gather."
    def _convertHours(self,hours):
        td = timedelta(seconds=int(hours * 3600))

        hours, remainder = divmod(td.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        hhmmss = f"{hours:02}:{minutes:02}:{seconds:02}"
        
        return hhmmss
    def _menu(self):
        while True:
            try:
                msg = self.MESSAGE.format(self.EACH_VIEWS)
            except:
                msg = self.MESSAGE
            os.system("cls") if os.name == 'nt' else os.system("clear") 
            print(f"""
            {Fore.BLUE}Program Configuration (Select an Option){Style.RESET_ALL}

            {Fore.GREEN}[1] {Fore.BLACK}-{Fore.MAGENTA} Webhook [{Fore.RESET}{self.WEBHOOK}{Fore.MAGENTA}{Fore.RESET}]
            {Fore.GREEN}[2] {Fore.BLACK}-{Fore.MAGENTA} Test Webhook
            {Fore.GREEN}[3] {Fore.BLACK}-{Fore.MAGENTA} Warn Each {Fore.RESET}{self.EACH_VIEWS}{Fore.MAGENTA} {TYPE}
            {Fore.GREEN}[4] {Fore.BLACK}-{Fore.MAGENTA} Message [{Fore.RESET}{msg}{Fore.MAGENTA}]{Fore.RESET}

            {Fore.GREEN}[5] {Fore.BLACK}-{Fore.LIGHTYELLOW_EX} Save Current Config{Fore.RESET}

            {Fore.GREEN}[99] {Fore.BLACK}-{Fore.LIGHTYELLOW_EX} Start!{Fore.RESET}

            """)
            
            try:
                u = int(input("-> "))

                if (u >= 1 and u <= 5) or (u == 99):
                    if u == 1:
                        self.WEBHOOK = input("Insert new -> ")
                        self.Webhook = Discord(url=self.WEBHOOK)
                    if u == 2: 
                        try:
                            self.Webhook.post(content="**Test Message To Webhook From TikTok Booster**")
                            print(Fore.GREEN+"Valid!")
                        except:
                            print(Fore.RED+"Invalid Webhook!"+Style.RESET_ALL)
                            time.sleep(0.5)
                        time.sleep(1)
                    if u == 3: 
                        try: self.EACH_VIEWS = int(input("Insert new -> "))
                        except: pass
                    if u == 4: 
                        self.MESSAGE = input("Insert new -> ")
                        try:
                            msg = self.MESSAGE.format(self.EACH_VIEWS)
                        except:
                            msg = self.MESSAGE
                    if u == 5:
                        try:
                            config.set("Settings","WEBHOOK",str(self.WEBHOOK))
                            config.set("Settings","EACH_VIEWS",str(self.EACH_VIEWS))
                            config.set("Settings","MESSAGE",str(self.MESSAGE))
                            with open("config.cfg", "w") as configfile:
                                config.write(configfile)
                            print("Saved!")
                            time.sleep(1)
                        except Exception as e:
                            print(e)
                            input()
                    if u == 99: break
            except:
                pass

if __name__ == "__main__": 
    os.system("cls") if os.name == 'nt' else os.system("clear") 
    CheckVersion("2.1.0")     
    Credits() 
    IsFirst()        
    Program()
