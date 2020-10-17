url = 'https://www.hao4k.cn//k_misign-sign.html'
request_header = {
    'authority': 'www.hao4k.cn',
    'method': 'GET',
    'path': '//k_misign-sign.html',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
    'cache-control': 'max-age=0',
    'cookie': 'UM_distinctid=174631d43e7b5f-0c3dcf7382b685-58321f4d-1fa400-174631d43e8d36; HxHg_2132_connect_is_bind=1; HxHg_2132_smile=1D1; HxHg_2132_atarget=1; HxHg_2132_saltkey=WIQiIis6; HxHg_2132_lastvisit=1602143162; HxHg_2132_auth=de96CgRV0xVTJtNocd9RAxOFnRRHjjd2VowNsuqoo0awGBNxrFnUpd%2Bci5jVfUpiu%2FesXR2AIwK416fDvOy6N9MOBA4; HxHg_2132_forum_lastvisit=D_2_1602430493; HxHg_2132_curcountl=0; HxHg_2132_ulastactivity=1602904530%7C0; HxHg_2132_lastcheckfeed=335559%7C1602904531; HxHg_2132_noticeTitle=1; CNZZDATA1257400611=366883270-1599387434-https%253A%252F%252Fwww.hao4k.cn%252F%7C1602902528; HxHg_2132_lastact=1602905092%09plugin.php%09; HxHg_2132_creditnotice=0D0D0D0D2D0D0D0D0D335559; HxHg_2132_creditbase=0D0D3D0D21D0D0D0D0',
    'referer': 'https://www.hao4k.cn//k_misign-sign.html',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36 Edg/86.0.622.43',
}
import requests
html=requests.get(url,headers=request_header)
html.encoding='gbk'
print(html.status_code)
