# encoding  = utf-8
import random, time, ddddocr
from DrissionPage import ChromiumPage, ChromiumOptions


def get_tracks(distance):
    value = round(random.uniform(0.55,0.75),2)
    v,t,sum1 = 0,0.3,0
    plus = []
    mid = distance * value
    while sum1 < distance:
        if sum1 <mid:
            a = round(random.uniform(2.5,3.5),1)
        else:
            a = -round(random.uniform(2.0,3.0),1)
        s = v * t + 0.5 * a * (t ** 2)
        v = v + a * t
        sum1 += s
        plus.append(round(s))
    return plus


co = ChromiumOptions()
page = ChromiumPage(co)

page.get("https://cszg.mca.gov.cn/biz/ma/csmh/g/cszzsearch.html?value=社会", retry=3, interval=2, timeout=15)

for i in range(1):
    background_bytes = page.ele('x://*[@id="oriImg"]').src()
    cut_bytes = page.ele('x://*[@id="cutImg"]').src()

    det = ddddocr.DdddOcr(det=False, ocr=False, show_ad=False)
    result = det.slide_match(cut_bytes, background_bytes, simple_target=True)
    print("滑块距离：", result)
    offset = result['target'][0]
    tracks = get_tracks(offset)
    print("滑块轨迹：", tracks)

    page.actions.hold('x://*[@id="slider"]')
    for track in tracks:
        page.actions.move(offset_x=track, offset_y=round(random.uniform(1.0, 3.0), 0), duration=.1)
    time.sleep(0.1)
    page.actions.release('x://*[@id="slider"]')
    page.ele('x://*[@id="captchadiv"]').get_screenshot(path='captcha1.jpg')
    time.sleep(3)
    if "验证" in page.ele('x://div[@class="path_content"]').text:
        print("滑动失败，刷新滑块")
        page.ele('x://img[@onclick="getSlideCaptcha()"]').click()
    else:
        print("滑块成功")
        break
