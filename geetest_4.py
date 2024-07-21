# encoding  = utf-8

# 可能禁用自动化浏览器

from DrissionPage import ChromiumPage, ChromiumOptions
from loguru import logger


# co = ChromiumOptions().headless()
# co.set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36')
co = ChromiumOptions()
page = ChromiumPage(co)
logger.info(page.user_agent)

page.get('https://www.geetest.com/adaptive-captcha-demo')
page.wait(2)