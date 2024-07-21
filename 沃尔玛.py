# encoding  = utf-8
from DrissionPage import ChromiumPage, ChromiumOptions
from loguru import logger
import string,random,os,csv,re


def generate_internal_id(num):
    characters = string.ascii_lowercase + string.digits
    internal_id = ''.join(random.choice(characters) for _ in range(num))
    return internal_id

def mkdir(path):
    folder = os.path.exists(path)
    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)

# co = ChromiumOptions().headless()
# co.set_user_agent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36')
co = ChromiumOptions()
page = ChromiumPage(co)
logger.info(page.user_agent)

page.get('https://www.walmart.com/')

page.ele('x://*[@id="__next"]/div[1]/div/span/header/form/div/input').input('cat food')
page.ele('x://*[@id="__next"]/div[1]/div/span/header/form/div/button[2]').click()

cat_food = page.eles('x:/html/body/div/div[1]/div/div/div[2]/div/main/div/div[2]/div/div/div[1]/div[2]/div/section/div/div')
logger.info(len(cat_food))

img_url,price,title,reviews,id = [],[],[],[],[]

for food in cat_food:
    if food.attr('class') == 'mb0 ph0-xl pt0-xl bb b--near-white w-25 pb3-m ph1':
        img_url_0 = food.ele('x://div/div/div/div[1]/div[2]/div[1]/img').attr('src')
        # logger.info(img_url_0)
        price_0 = food.ele('x://div/div/div/div[2]/div[1]/div[1]/span[3]').text + '.' + food.ele('x://div/div/div/div[2]/div[1]/div[1]/span[4]').text
        logger.info(price_0)
        title_0 = food.ele('x://div/div/div/div[2]/span/span').text
        if food.ele('x://div/div/div/div[2]/div[3]/span[3]'):
            reviews_0 = food.ele('x://div/div/div/div[2]/div[3]/span[3]').text
        else:
            reviews_0 = food.ele('x://div/div/div/div[2]/div[2]/span[3]').text
        logger.info(reviews_0)
        id_0 = generate_internal_id(8)

        img_url.append(img_url_0)
        price.append(price_0)
        title.append(title_0)
        reviews.append(reviews_0)
        id.append(id_0)

logger.info('所有数据获取完毕')


csv_filename = 'D:\从pycharm脚本中获得的网页数据\walmart_catfood.csv'
with open(csv_filename, mode='w', newline='',encoding='utf-8') as file:
    writer = csv.writer(file)

    # 写入表头，假设这里是每个列表的名称
    writer.writerow(['产品图片URL','价格（美元）','商品标题', '评分', '系统随机编号'])

    # 写入数据行
    for row in zip(img_url, price, title, reviews, id):
        writer.writerow(row)

logger.info(f"CSV 文件 {csv_filename} 写入完成。")

