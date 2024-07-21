# encoding  = utf-8
from DrissionPage import ChromiumPage, ChromiumOptions
from loguru import logger


co = ChromiumOptions().headless()
co.set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36')
# co = ChromiumOptions()
page = ChromiumPage(co)
logger.info(page.user_agent)

page.get('https://www.expedia.com/')
page.wait(2)

# 点击航线
page.ele('x://*[@id="multi-product-search-form-1"]/div/div/div[1]/ul/li[2]/a/span').click()
# page.wait(2)
logger.info('点击航线')

# 点击出发点
page.ele('x://*[@id="FlightSearchForm_ROUND_TRIP"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/button').click()
# page.wait(1)
logger.info('点击出发点')

# 输入出发点
page.ele('x://*[@id="origin_select"]').input('huanghua')
# page.wait(1)
logger.info('输入出发点')

page.ele('x://*[@id="origin_select-menu"]/section/div/div[2]/div/ul/div[1]/li/div/div/button').click()
# page.wait(1)

# 点击目的地
page.ele('x://*[@id="FlightSearchForm_ROUND_TRIP"]/div/div[1]/div/div[2]/div/div/div[2]/div[1]/button').click()
# page.wait(1)
logger.info('点击目的地')

# 输入目的地
page.ele('x://*[@id="destination_select"]').input('jeju')
# page.wait(1)
logger.info('输入目的地')

page.ele('x://*[@id="destination_select-menu"]/section/div/div[2]/div/ul/div[1]/li/div/div/button').click()
# page.wait(1)

# 点击搜索
page.ele('x://*[@id="search_button"]').click()
page.wait(2)
logger.info('点击搜索')

for li in page.eles('x://*[@id="app-layer-base"]/div[3]/div[3]/div[1]/div/div[2]/main/ul//li')[1:2]:
    logger.info(li.text)
