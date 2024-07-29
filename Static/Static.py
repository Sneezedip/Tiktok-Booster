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
    firstStep = {
        'views': '/html/body/div[10]/div/form/div/input',
        'shares' : '/html/body/div[11]/div/form/div/input',
        'favorites' : '/html/body/div[12]/div/form/div/input'
    }
    secondStep = {
        'views': '/html/body/div[10]/div/form/div/div/button',
        'shares' : '/html/body/div[11]/div/form/div/div/button',
        'favorites' : '/html/body/div[12]/div/form/div/div/button'
    }
    thirdStep = {
        'views': '/html/body/div[10]/div/div/span',
        'shares' : '/html/body/div[11]/div/div/span',
        'favorites': '/html/body/div[12]/div/div/span'
    }
    fourthStep = {
        'views': '/html/body/div[10]/div/form/div/div/button',
        'shares' : '/html/body/div[11]/div/form/div/div/button',
        'favorites' : '/html/body/div[12]/div/form/div/div/button'
    }
    readyValues = {
        'views' : '//*[@id="c2VuZC9mb2xeb3dlcnNfdGlrdG9V"]/span[1]',
        'shares' : '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/span[1]',
        'favorites' : '//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9L"]/span[1]'
    }
    finalButton = {
        'views' : '//*[@id="c2VuZC9mb2xeb3dlcnNfdGlrdG9V"]/div[1]/div/form/button',
        'shares' : '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/div[1]/div/form/button',
        'favorites' : '//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9L"]/div[1]/div/form/button'
    }
    ChromeOptions = ["--disable-gpu","--incognito",f"user-agent={GenerateHeaders}"]
