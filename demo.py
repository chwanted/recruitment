# -*- coding: utf-8 -*-
import asyncio
from pyppeteer import launch
from pyppeteer.network_manager import Request, Response

async def intercept_request(req: Request):
    await req.continue_()

async def intercept_response(res: Response):
    resourceType = res.request.resourceType
    if resourceType in ['xhr', 'fetch']:
        resp = await res.text()
        print(resp)

async def main():
    browser = await launch({
        'headless': False,
        'userDataDir':r'D:/ch',
        'args':[
            '--disable-infobars',
            '--no-sandbox',
            '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36',
        ]
    })

    # 打开一个页面
    page = await browser.newPage()
    # await page.goto('https://passport.zhaopin.com/login')
    # await asyncio.sleep(5)  # 扫码登录等待

    # 启用拦截器
    await page.setRequestInterception(True)
    page.on('request', intercept_request)
    page.on('response', intercept_response)
    await page.goto('https://sou.zhaopin.com/?jl=551&kw=etl&kt=3')
    await browser.close()

# 调用
asyncio.get_event_loop().run_until_complete(main())



