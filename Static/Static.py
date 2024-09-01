from fake_useragent import UserAgent
class Static(): 
    typeValues = {
        'followers' : '/html/body/div[6]/div/div[2]/div/div/div[2]/div/button',
        'views' : '/html/body/div[6]/div/div[2]/div/div/div[6]/div/button',
        # 'commenthearts' : '/html/body/div[6]/div/div[2]/div/div/div[4]/div/button', broken!!!
        'favorites': '/html/body/div[6]/div/div[2]/div/div/div[8]/div/button',
        'shares' : '/html/body/div[6]/div/div[2]/div/div/div[7]/div/button',
        'hearts' : '/html/body/div[6]/div/div[2]/div/div/div[3]/div/button'
    }
    firstStep = {
        'views': '/html/body/div[10]/div/form/div/input',
        'shares' : '/html/body/div[11]/div/form/div/input',
        'favorites' : '/html/body/div[12]/div/form/div/input',
        'hearts' : '/html/body/div[8]/div/form/div/input'
    }
    secondStep = {
        'views': '/html/body/div[10]/div/form/div/div/button',
        'shares' : '/html/body/div[11]/div/form/div/div/button',
        'favorites' : '/html/body/div[12]/div/form/div/div/button',
        'hearts' : '/html/body/div[8]/div/form/div/div/button'
    }
    thirdStep = {
        'views': '/html/body/div[10]/div/div/span',
        'shares' : '/html/body/div[11]/div/div/span',
        'favorites': '/html/body/div[12]/div/div/span',
        'hearts' : '/html/body/div[8]/div/div/span'
    }
    fourthStep = {
        'views': '/html/body/div[10]/div/form/div/div/button',
        'shares' : '/html/body/div[11]/div/form/div/div/button',
        'favorites' : '/html/body/div[12]/div/form/div/div/button',
        'hearts' : '/html/body/div[8]/div/form/div/div/button'
    }
    readyValues = {
        'views' : '//*[@id="c2VuZC9mb2xeb3dlcnNfdGlrdG9V"]/span[1]',
        'shares' : '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/span[1]',
        'favorites' : '//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9L"]/span[1]',
        'hearts' : '//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/span'
    }
    finalButton = {
        'views' : '//*[@id="c2VuZC9mb2xeb3dlcnNfdGlrdG9V"]/div[1]/div/form/button',
        'shares' : '//*[@id="c2VuZC9mb2xsb3dlcnNfdGlrdG9s"]/div[1]/div/form/button',
        'favorites' : '//*[@id="c2VuZF9mb2xsb3dlcnNfdGlrdG9L"]/div[1]/div/form/button',
        'hearts' : '//*[@id="c2VuZE9nb2xsb3dlcnNfdGlrdG9r"]/div[1]/div/form/button'
    }
    ChromeOptions = ["--window-size=1920,1080","--disable-gpu","--incognito",f"user-agent={UserAgent().random}"]
