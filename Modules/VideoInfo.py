import os,sys
try:
    import requests
    from bs4 import BeautifulSoup
    import re
    from fake_useragent import UserAgent
except ImportError:
    print('Installing Libraries...')
    os.system("pip install -r requirements.txt")
    print('Libraries installed. Restart the program!')
    sys.exit()

class TikTokVideoInfo:
    def __init__(self, video_url):
        self.video_url = video_url
        self.VIDEOID = self._extract_video_id()
        self.data = None

    def _extract_video_id(self):
        match = re.search(r'tiktok\.com/@[^/]+/video/(\d+)', self.video_url) or re.search(r'tiktok\.com/@[^/]+/photo/(\d+)', self.video_url)
        if match:
            return match.group(1)
        else:
            raise ValueError("Invalid video URL")

    @staticmethod
    def get_csrf_token_and_cookies():
        url = "https://www.trollishly.com/tiktok-counter/"
        headers = {
            'User-Agent': UserAgent().random,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Connection': 'keep-alive'
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('meta', {'name': 'csrf-token'})
        if csrf_token:
            csrf_token = csrf_token.get('content')
        else:
            raise Exception("CSRF token not found")

        return csrf_token, response.cookies

    def post_tiktok_data(self, csrf_token, cookies):
        url = "https://www.trollishly.com/nocache/search_tiktok_user_counter_val/"
        payload = {
            'username': self.VIDEOID
        }
        headers = {
            'User-Agent': UserAgent().random,
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Language': 'en-US,en;q=0.9',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Referer': 'https://www.trollishly.com/tiktok-counter/',
            'Connection': 'keep-alive',
            'X-CSRF-Token': csrf_token,
            'X-Requested-With': 'XMLHttpRequest'
        }

        try:
            response = requests.post(url, data=payload, headers=headers, cookies=cookies)
            response.raise_for_status()

            if response.status_code == 200:
                return response.json()
            else:
                return {'error': 'Failed to retrieve data'}
        except requests.exceptions.RequestException as e:
            print(f"Request Exception: {e}")
            return {'error': 'Error during request'}

    def _get_video_info(self, Creator=False, Views=False, Likes=False, Shares=False, Comments=False,
                        post_new_data=False):
        if self.data is None or post_new_data:
            max_retries = 7
            retry = 0

            while retry <= max_retries:
                try:
                    csrf_token, cookies = self.get_csrf_token_and_cookies()
                    self.data = self.post_tiktok_data(csrf_token, cookies)

                    # print(f"Data Retrieved: {self.data}") # For debugging :)

                    if 'error' in self.data:
                        return self.data['error']
                    break
                except requests.RequestException as e:
                    retry += 1
                    if retry > max_retries:
                        return "Unable to gather information after multiple attempts."

        if Creator:
            try:
                return re.search(r'tiktok\.com/@([^/]+)/video/', self.video_url).group(1)
            except:
                return re.search(r'tiktok\.com/@([^/]+)/photo/', self.video_url).group(1)
        elif Views:
            return self.data.get('video_views_count', 'View count not available')
        elif Likes:
            return self.data.get('video_likes_count', 'Like count not available')
        elif Shares:
            return self.data.get('video_share_count', 'Share count not available')
        elif Comments:
            return self.data.get('video_comment_count', 'Comment count not available')

    def get_video_info(self, Creator=False, Views=False, Likes=False, Shares=False, Comments=False,
                       post_new_data=False):
        """Public method to safely access _get_video_info."""
        return self._get_video_info(Creator=Creator, Views=Views, Likes=Likes, Shares=Shares, Comments=Comments,
                                    post_new_data=post_new_data)
