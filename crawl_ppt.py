'''
这个爬虫是为了爬取雨课堂里的ppt内容，将图片保存到文件夹中为1_n.jpg的格式，然后再将其整合为ppt
'''
# from selenium import webdriver
import requests
import shutil
import undetected_chromedriver as webdriver
from bs4 import BeautifulSoup

# 启动浏览器
driver = webdriver.Chrome()  # 根据你的浏览器类型选择相应的webdriver
driver.maximize_window()

# 访问网页
url = r"https://www.yuketang.cn"
driver.get(url)
input("Please get in the ppt!")
driver.switch_to.window(driver.window_handles[-1])

ppt_no = 1
while(input("Input q to quit!\n") != 'q'):
    # 获取网页源码
    html_content = driver.page_source
    # 使用Beautiful Soup解析HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    ppts = soup.find_all("div", {"class": "swiper-slide"})
    pic_num = 1
    pro_num = 0         # Error number
    for ppt in ppts:
        name = str(ppt_no) + '_' + str(pic_num)
        try:
            # 多个ppt会有开头几个不行
            # 会出现重复性的问题，不知道为什么
            pic_src = ppt.div.div.img['src']
        except Exception as error:
            print(error)
            pro_num += 1
            continue

        response = requests.get(pic_src, stream=True)
        if response.status_code == 200:
            with open('./fig/' + name + '.jpg', 'wb') as f:
                response.raw.decode_content = True
                shutil.copyfileobj(response.raw, f)
            print(f"图片已成功下载，{pic_num}/{int((len(ppts)-pro_num)/2)}")
        else:
            print("下载失败")
        pic_num += 1

        # Skip the last half, which is repetitive
        if pic_num > int((len(ppts)-pro_num)/2):
            break

    ppt_no += 1

driver.quit()
