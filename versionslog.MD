# Version 2.9.1
   -  Contribution by rowan0881:
      New Language! (Dutch)
   -  Added:
      More Languages! (French, Spanish, German, Italian, Russian, Arabic, Japanese )
   Info : 
      Not every phrase is translated, doing it in the future...

# Version 2.9.0
   -  Removed:
         Unused code.
         uBlock Origin Extension.
         Error message displayed when not selecting a history video.
   -  Added:
         New discord invite link
         TRANSLATIONS - beta !! (en,pt)
   -  Fixed:
         Some Color Resets

# Version 2.8.1.1
   - Fixed:
      - Minifix for update.

# Version 2.8.1
   - Fixed:
      - Key generation issue with wmic. (every key was revoked)
      - Fixed another key issue.
      - Fixed Blacklist Issue.

# Version 2.8.0
   - Removed:
      - Unused Exceptions
   - Added:
      - Added Video History.

# Version 2.7.3.4
   - Hotfix:
      - Fixed ElementNotInteractableException.

# Version 2.7.3.2
   - Hotfix:
      - fixed wmic not found.

# Version 2.7.3.2
   - Hotfix:
      - fixed --enable-unsafe-swiftshader. (again)

# Version 2.7.3.1
   - Hotfix:
      - fixed --enable-unsafe-swiftshader.
      
# Version 2.7.3
   - Fixed:
      - Fixed not accepting photo videos.

# Version 2.7.2
   - Fixed:
      - Fixed white screen when running the program with headless in true.
   - Bonus:
      - Replaced some errors.
      
# Version 2.7.1
   - Added:
      - When changing the Video URL inside Tiktok-Booster (when running in cmd) it'll update the config.cfg in realtime.
   - Fixed:
      - Fixed an unnecessary error that would cause the program to crash (Invalid Video URL).

# Version 2.7.0
   - Added:
      - New menu to select the TYPE.
   - Removed:
      - Sandbox errors when starting webdriver.rrrr   NNBÇRRRRRR

# Version 2.6.1
   - Fixed:
      - Fixed modules not installing.

# Version 2.6.0
   - Added:
      - Key Validation.
   - Fixed:
      - Fixed fake_useragent module not installing.
      
# Version 2.5.0
   - Added:
      - Added webhook check, so it doesn't delay the program even if the webhook is invalid.
      - Added Followers type (might not be available).
      - Added a new class (ProgramUsage) and moved many functions from main.py to Usage.py.
      - Added a new class (Handler) and moved many functions from main.py to BannersHandler.py.
   - Fixed:
      - Fixed estimated time math, to give more accurate results.
      - Fixed Webhook printing errors in banner
   - Removed:
      - Removed unnecessary delay's.
   - Bonus:
      - Explained more about each function.
      - Optimized functions in main.py.
      - Moved download function from main.py to Usage.py

# Version 2.4.1
      - Contribution by JJFilipek:
         - Implemented a retry mechanism in the GetViews method to handle TypeError exceptions. The program will now attempt to retry the operation up to 3 times if an issue occurs.
         - Updated the _gather_info function in the Program class to align with changes made in the TikTokVideoInfo class.
         - Refined exception handling throughout the code by narrowing overly broad except clauses to better handle specific types of exceptions.
         - Added comments to major functions in main.py to improve code readability and understanding.
         - Updated the requirements.txt file to include fake_useragent as a new dependency.
         - Refactored code to follow Pythonic conventions, including changing variable names to snake_case and ensuring consistency with PEP 8 guidelines.
         - Add browser reset logic after max retries in method

# Version 2.4.0
      -  Now the Auto Updater replaces all the files by itself!
      -  Added an option in config.cfg that bypasses Webhook Configuration when you start the program.
      -  Added a run.bat file to start the program.
      -  Added Progress bar when downloading Tesseract.
      -  Fixed program not updating the amount of views each time it boosts.
      -  Fixed some color styles and prints.
      -  Bug Fixes.

# Version 2.3.1
      -  Added more Errors handling.
      -  Fixed error 000 (Couldn't click final button when in Headless mode).

# Version 2.3.0
      - Fixed infinite loop in "Installing Libraries"
      - Now the program tells what TYPES are available if you choose one thats unavailable.

# Version 2.2.0
      - Contribution by 5k-omar which corrected many bugs and added new features!

# Version 2.1.1.2
      - Hotfix For Integers.

# Version 2.1.1.1
      - Hotfix for malfunction of Countik API

# Version 2.1.1
      - Added Hearts!

# Version 2.1.0
      - Fixed Shares not working properly.
      - Added Favorites.
      - Remastered menu to include shares and favorites.

# Version 2.0.3
      - Added Shares option in config.cfg
      - Bug fixes.

# Version 2.0.2
      - Fixed Colors.
      - Fixed import errors.
      - Fixed Initial Views Error.

# Version 2.0.0
      Now you can add a Webhook and configure how much views it takes to warn you about it!
      Created a mini menu to configure the webhook.

# Version 1.4.2
      - Added Percentage to keep track of progress.
      - Added Amount of views Gained.

# Version 1.4.1
    - Prettier hour format (HH:MM:SS)
    - Fixed Estimated time not working.

# Version 1.4.0
    - Created a menu that displays Video Creator,Views,Likes and Shares with confirmation that asks the user to start.
        - Menu also displays the amount of views it'll end with after program is done.
        - Menu will also display the Est. hours that it will take to finish.
    - Now it always displays the estimated time remaining.

# Version 1.3.0
    - Added more Delay to prevent crashing.
    - Added more exceptions to prevent crashing
    - More Logs (when updating)
    - Now program works with links starting with 'vm' (instead of 'www')

# Version 1.2.1
    - Minor Fix

# Version 1.2.0
    - Updated waiting time.
    - Now it prints the current amount of views.
    - Added 'cls' (for linux and windows).
    - Fixed SLEEP bug.

# Version 1.1.4
    - Minor bug fixes.

# Version 1.1.3
    - Started using WebDriverWait instead of time.sleep for better results.
    - Added Current time for all logs.

# Version 1.1.2
    - Added Style to every String
    - Added more logs!
    - If The program waits for too long, it will warn the user.
    - Added "\r" end to every string to prevent printing flood.

# Version 1.1.1
    - Added Auto Updater
    - Added Colors (colorama)
    - Added Credits

# Version 1.1.0
    - HEADLESS now works!
    - Program +~122,7% faster (Removed unused delays)
    - Added more Chrome Options (incognito and Disable GPU)
    - Added Update Checker.

# Version 1.0.1
    - Fixed crashing at random moments
    
# Version 1.0.0
    - Auto Captcha Completer
