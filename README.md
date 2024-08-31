<p align="center"><a href="https://github.com/Sneezedip/Tiktok-Booster"><img src="https://static.vecteezy.com/system/resources/previews/024/273/794/non_2x/tiktok-logo-transparent-free-png.png" alt="TTKVB" height="150"/></a></p>
<h1 align="center">Tiktok-Booster</h1>

TikTok View Booster is a Python-based tool designed to increase the view count of TikTok videos. This tool utilizes Tesseract OCR to recognize and bypass CAPTCHA challenges, ensuring a seamless and automated process for boosting video views.

<div align="center">

[![Paypal](https://img.shields.io/badge/PayPal-Donate-blue.svg?logo=PayPal)](https://paypal.me/sneezedip)

[![Discord](https://img.shields.io/discord/1107726482224197642?label=discord&color=9089DA&logo=discord&style=for-the-badge)](https://discord.gg/nAa5PyxubF)

</div>

## Features

- **Automated Views:** Automatically increases the view count of specified TikTok videos.
- **CAPTCHA Bypass:** Utilizes Pillow and Tesseract OCR to accurately solve CAPTCHA challenges.
- **Easy to Use:** Simple configuration and setup for quick deployment.

![showcase1](SHOWCASE/showcase1.png)

![showcase2](SHOWCASE/showcase2.png)

![showcase3](SHOWCASE/showcase3.png)

![showcase4](SHOWCASE/showcase4.png)

## Usage

To run the program, follow these steps:

1. **Configure `config.cfg`:**
   - Open the `config.cfg` file in a text editor of your choice.
   - Adjust the settings as needed to suit your preferences and requirements.

2. **Open Command Prompt in `tiktokbooster` Folder:**
   - Navigate to the `tiktokbooster` folder.
   - Open a command prompt (cmd) in this folder. You can do this by:
     - Typing `cmd` in the address bar of the File Explorer and pressing Enter.
     - Right-clicking inside the folder, selecting "Open in Terminal" or "Open Command Window Here".

3. **Run the Program:**
   - In the command prompt, execute the following command:
     ```sh
     python3 main.py
     ```
   - (or you can use Visual Studio Code)

4. **Wait:**
   - Allow the program to run and complete its tasks. This may take some time depending on the configurations and operations being performed.

# Version 2.4.1
      - Contribution by JJFilipek:
         - Implemented a retry mechanism in the GetViews method to handle TypeError exceptions. The program will now attempt to retry the operation up to 3 times if an issue occurs.
         - Updated the _gather_info function in the Program class to align with changes made in the TikTokVideoInfo class.
         - Refined exception handling throughout the code by narrowing overly broad except clauses to better handle specific types of exceptions.
         - Added comments to major functions in main.py to improve code readability and understanding.
         - Updated the requirements.txt file to include fake_useragent as a new dependency.
         - Refactored code to follow Pythonic conventions, including changing variable names to snake_case and ensuring consistency with PEP 8 guidelines.
         - Add browser reset logic after max retries in method
      
### for more info check [*versionslog.md*](https://github.com/Sneezedip/Tiktok-Booster/blob/main/versionslog.MD)

**Please note: This project is not intended for commercial use. It is provided for educational and personal use only.**
