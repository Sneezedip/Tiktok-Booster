from fake_headers import Headers
class Static():
    def GenerateHeaders():
        #Thanks to some user on StackOverflow
        header = Headers(
            browser="chrome",
            os="win",
            headers=False
        )
        return header.generate()['User-Agent']
    
    typeValues = {
        'views' : '/html/body/div[6]/div/div[2]/div/div/div[6]/div/button',
        'commenthearts' : '/html/body/div[6]/div/div[2]/div/div/div[4]/div/button',
        'favorites': '/html/body/div[6]/div/div[2]/div/div/div[8]/div/button',
        'shares' : '/html/body/div[6]/div/div[2]/div/div/div[7]/div/button'
    }
    ChromeOptions = ["--disable-gpu","--incognito",f"user-agent={GenerateHeaders}"]
