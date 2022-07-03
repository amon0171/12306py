from PyQt5.QtCore import QObject
from selenium import webdriver
import time
from selenium.webdriver import ActionChains  # 导入鼠标事件
from selenium.webdriver.common.keys import Keys  # 键盘功能键封装的一个函数
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
url = 'https://kyfw.12306.cn/otn/resources/login.html'  # 铁路12306网址


class APITool_Main():
    UserName = ''
    PassWord = ''
    @classmethod
    def check_login(self, account, pwd):
        # 反爬虫
        driver = webdriver.Chrome(options=options)  # 驱动
        driver.get(url)
        script = 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined,});'
        driver.execute_script(script)
        # 窗口最小化
        # driver.maximize_window()
        driver.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[2]/div[2]/ul/li[1]/a').click()  # 点击账号密码登录
        # x = input('---输入你的用户名---\n')
        username = driver.find_element(By.ID, 'J-userName')
        username.send_keys(account)
        # y = input('---输入你的密码---\n')
        time.sleep(0.5)
        password = driver.find_element(By.ID, 'J-password')
        password.send_keys(pwd)
        time.sleep(0.5)
        driver.find_element(By.ID, 'J-login').click()
        time.sleep(5)
        # try:
        #     driver.find_element(By.CLASS_NAME, "modal-close").click()
        #     time.sleep(1)
        # except:
        #     print('---程序正在运行---')
        # driver.find_element(By.XPATH, '//*[@id="J-index"]/a').click()
        # 最小化窗口
        # driver.minimize_window()
        return driver.current_url
        time.sleep(5)

    @classmethod
    def check_buy_trick(self, buy_trick_num, from_where, to_where, get_data, isStudent_trick):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        driver = webdriver.Chrome(options=options)  # 驱动
        WAIT = WebDriverWait(driver, 10)
        url = 'https://kyfw.12306.cn/otn/resources/login.html'  # 铁路12306网址
        driver.get(url)
        # 反爬虫
        script = 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined,});'
        driver.execute_script(script)
        # 窗口最小化
        driver.maximize_window()
        driver.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[2]/div[2]/ul/li[1]/a').click()  # 点击账号密码登录
        # x = input('---输入你的用户名---\n')
        x = self.UserName
        username = driver.find_element(By.ID, 'J-userName')
        username.send_keys(x)
        # y = input('---输入你的密码---\n')
        y = self.PassWord
        password = driver.find_element(By.ID, 'J-password')
        password.send_keys(y)
        time.sleep(0.5)
        driver.find_element(By.ID, 'J-login').click()
        # 窗口最大化
        driver.maximize_window()
        # 滑动验证码
        # 定位验证码的头位置元素
        time.sleep(1)
        # picture_start = driver.find_element(By.ID,'nc_1_n1z')
        # # 移动到相应的位置，并左键鼠标按住往右边拖
        # ActionChains(driver).move_to_element(picture_start).click_and_hold(picture_start).move_by_offset(300,
        #                                                                                                  0).release().perform()
        # 有页面有个窗口 把他叉掉或者确定掉
        time.sleep(3)
        try:
            driver.find_element(By.CLASS_NAME, "modal-close").click()
            time.sleep(1)
        except:
            print('---程序正在运行---')
        driver.find_element(By.XPATH, '//*[@id="J-index"]/a').click()
        # 最小化窗口
        # driver.minimize_window()
        time.sleep(1)
        # here_place = input('---你的出发地---\n')
        here_place = from_where
        driver.find_element(By.XPATH, '//*[@id="fromStationText"]').send_keys(Keys.CONTROL, 'a')
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="fromStationText"]').send_keys(Keys.BACKSPACE)
        driver.find_element(By.XPATH, '//*[@id="fromStationText"]').send_keys(here_place)  # 输入你的出发地
        # 因为12306输入出发地存在一个下拉框问题，所以这里我们使用keys这个封装好的函数，来调用键盘上的回车键，这样就避免了鼠标点击空白处 这个操作
        driver.find_element(By.XPATH, '//*[@id="fromStationText"]').send_keys(Keys.ENTER)
        # there_place = input('---你的目的地---\n')
        there_place = to_where
        driver.find_element(By.XPATH, '//*[@id="toStationText"]').clear()
        driver.find_element(By.XPATH, '//*[@id="toStationText"]').send_keys(there_place)
        driver.find_element(By.XPATH, '//*[@id="toStationText"]').send_keys(Keys.ENTER)
        # 买哪天的票，出发日期填写
        # travel_date = input('由于疫情目前12306只支持提前15天买票\n出发日期格式：20xx-05-07\n')
        travel_date = get_data
        time.sleep(1)
        # 这里用的是keys函数，调用ctrl+a全选，然后按删除键，删除原对话框内容
        driver.find_element(By.XPATH, '//*[@id="train_date"]').send_keys(Keys.CONTROL, 'a')  # control+a全选
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="train_date"]').send_keys(Keys.BACKSPACE)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="train_date"]').send_keys(travel_date)
        driver.find_element(By.XPATH, '//*[@id="train_date"]').click()
        time.sleep(1)
        print('等待中')
        time.sleep(0.5)

        '''
        这里注意，就算你输入了订票日期，下拉框也依旧存在，这里我们使用以下方法，解决这个问题，详细解释
        https://blog.csdn.net/weixin_43784564/article/details/120352680
        '''

        try:
            # 不能一次性到链接，那就中间再点两次无用的静态文字
            driver.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[4]/div[3]/div[1]/h3').click()
            time.sleep(2)
            driver.find_element(By.XPATH, '//*[@id="index_ads"]').click()
            time.sleep(2)
            # 点击页面上的静态图片(没有内含超链接)，为了把上面车票的日期下拉框给去掉
            driver.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[5]/div[1]/div/h2').click()
        except:
            driver.find_element(By.XPATH, '//*[@id="index_ads"]').click()
            time.sleep(2)
            # 点击页面上的静态图片(没有内含超链接)，为了把上面车票的日期下拉框给去掉
            driver.find_element(By.XPATH, '//*[@id="toolbar_Div"]/div[5]/div[1]/div/h2').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="search_one"]').click()
        # 叉掉疫情提示
        time.sleep(2)

        '''
        为什么要获得窗口句柄，详细解释详见我上一条csdn博客https://blog.csdn.net/weixin_43784564/article/details/120368372
        '''
        # 获取打开的多个窗口句柄
        windows = driver.window_handles
        # 切换到当前最新打开的窗口
        driver.switch_to.window(windows[-1])
        time.sleep(2)

        # 窗口最大化
        driver.maximize_window()
        time.sleep(2)

        # 这里打开页面会有一个温馨提示，把他叉掉
        try:
            driver.find_element(By.XPATH, '//*[@id="gb_closeDefaultWarningWindowDialog_id"]').click()
        except:
            print('---这个温馨提示我没叉掉/不存在温馨提示---')

        # 现在来到了购票页面，点击查询按钮
        # 这里出现一个问题，会出现页面查询超时，所以我们应该搞个功能，即点击按钮，直到出现车次情况！！！用到自己写的一个函数

        driver.find_element(By.XPATH, '//*[@id="query_ticket"]').click()
        time.sleep(2)
        # driver.minimize_window()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="query_ticket"]').click()
        time.sleep(2)

        # 如果页面查询超时，就用下面这个函数
        def refresh_yemian():
            successful_search = ''
            try:
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="float"]/th[1]').click()
                time.sleep(1)
                successful_search = '---查询页面正常，可正常查询车次---'
                time.sleep(1)
            except:
                print('---正在点击查询按钮---', end='\r')
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="query_ticket"]').click()
                time.sleep(1)
                refresh_yemian()
            return successful_search

        refresh_yemian()
        time.sleep(1)

        # 看乘车人是否为学生，是否想购买学生票
        def student():
            time.sleep(1)
            # stu = input('是否购买学生票，请输入是或否\n')
            stu = isStudent_trick
            if stu == '否':
                driver.find_element(By.XPATH, '//*[@id="query_ticket"]').click()
                accept_stu = '已选择成人票'
            else:
                stu_element = driver.find_element(By.XPATH, '//*[@id="sf2"]')
                stu_element.click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="query_ticket"]').click()
                accept_stu = '已勾选购买学生票'
            return accept_stu

        student()
        time.sleep(1)

        # 注意，本抢票脚本只适用于开始售票的那几分钟有用，毕竟抢票就抢那几分钟
        # 注意，本抢票脚本还差一个定时执行任务脚本。需要你定个时

        # 定义一个函数，如果发现目前页面没票了，就不断刷新页面，给你查询是否有票现在.
        def refresh_search_ticket(train_message, train_number):
            global success_message
            for times in range(0, 31):
                success_message = ''
                if times < 30:
                    driver.find_element(By.XPATH, '//*[@id="query_ticket"]').click()
                    time.sleep(1)
                    if '有' == train_message[10] or '有' == train_message[9]:
                        print('---您选的车次二等座有票了，正在为您预定---')
                        time.sleep(0.5)
                        button = train_number.find_element(By.XPATH,
                                                           './/td[13]/a[@class="btn72"]')  # 已经锁定车次，对当前车次进行车票预定
                        time.sleep(0.5)
                        button.click()
                        # .//a[@class="btn72"]意思就是取a标签的属性为class的值为btn72的元素xpath
                        time.sleep(1)
                        success_message = '---预定成功，现在正在选择乘车人---'
                        print('---预定成功，现在正在选择乘车人---')
                        break
                    else:
                        print('继续点击查询按钮，刷新余票', end='\r')

                else:
                    time.sleep(1)
                    success_message = '---查询时间已到！抱歉，您所选的车次，目前没有二等座的票了，您可去12306官网，继续查询---'
                    time.sleep(0.5)
                    print('---查询时间已到！抱歉，您所选的车次，目前没有二等座的票了，您可去12306官网，继续查询---')
                    break
            return success_message

        # 输入你想乘坐的车次，订票
        def order_ticket():
            # train_num = input('---输入你想乘坐的火车车次---\n')
            train_num = buy_trick_num
            train_numbers = driver.find_elements(By.XPATH, '//tbody[@id="queryLeftTable"]/tr[not(@datatran)]')
            # 记得在元素element后面加s，因为有好多个元素，这里定位的是不含datatran的所有元素
            # train_buttons = driver.find_elements(By.XPATH,'.//a[@class="btn72"]')

            for train_number in train_numbers:
                order_ticket_message = ''
                train_messages = train_number.text.replace('\n', ' ')  # 把换行符替换成空格
                train_message = train_messages.split(' ')  # split切割函数，用' '来切片，并返回字符串列表
                print(train_message)
                if train_num == train_message[0]:
                    print('---找到你想要的车次了---')
                    if '有' == train_message[10] or '有' == train_message[9]:
                        # 这里的列表数值，各个车可能有出入，到时候大家打印下整个车次列表，然后再改下数字就行了，一般来说是不用改的
                        print('---该车次现在有二等座---')
                        order_ticket_message = choice(train_number)
                        print('1')
                        break
                    else:
                        print('---抱歉，您所选的车次车票，目前没票了，存在有候补票这种情况，正在为你刷新页面，实时更新车票情况---')
                        result = '---查询时间已到！抱歉，您所选的车次，目前没有二等座的票了，您可去12306官网，继续查询---'
                        time.sleep(1)
                        # 没票了，现在调用不断刷新页面的函数，来给你查询余票，并返回值
                        success_messages = refresh_search_ticket(train_message, train_number)

                        if result == success_messages:
                            time.sleep(1)
                            order_ticket_message = '---本次抢票已结束,祝你好运---'
                            print('---本次抢票已结束,祝你好运---')
                            break
                        else:
                            order_ticket_message = '查到票了，预定成功，开始选乘坐人'
                            print('查到票了，预定成功，开始选乘坐人')
                            break
                else:
                    print('---正在查询你所需要的车次---', end='\r')  # 覆盖前面一句---正在查询你所需要的车次---，不然每循环一次，就会打印一次这句话

            return order_ticket_message

        def choice(train_number):
            while True:
                try:
                    # / html / body / div[2] / div[8] / div[8] / table / tbody[1] / tr[7] / td[13] / a
                    button = train_number.find_element(By.XPATH, './/a[@class="btn72"]')  # 已经锁定车次，对当前车次进行车票预定
                    button.click()
                    button.click()
                    time.sleep(2)
                    order_ticket_message = '预定成功，现在正在选择乘车人'
                    print('预定成功，现在正在选择乘车人')
                    return order_ticket_message
                except:
                    pass

        # driver.find_element(By.XPATH,'//*[@id="login_user"]').click()

        finally_message = order_ticket()

        if finally_message == '---本次抢票已结束,祝你好运---':
            print('---即将关闭浏览器打开的所有窗口---')
            driver.quit()
            time.sleep(1)
            print('---浏览器已关闭---')
        else:
            time.sleep(2)
            # 点击乘车人信息，默认第一个为本人

            driver.find_element(By.XPATH, '//*[@id="normalPassenger_0"]').click()
            time.sleep(1)
            print('---乘车人选择成功，默认选择12306上面乘车人列表的第一位---')
            try:
                driver.find_element(By.CLASS_NAME, "modal-close").click()
                time.sleep(1)
            except:
                print('---关闭提示窗口---')
            time.sleep(1)
            # 点击提交订单
            driver.find_element(By.XPATH, '//*[@id="submitOrder_id"]').click()
            time.sleep(2)
            print('---已提交订单---')
            time.sleep(2)

            # 下面可能存在逻辑错误
        # 选座

        decision_true = '//*[@id="qr_submit_id"]'  # 确定

        choice_button = driver.find_element(By.XPATH, decision_true)
        driver.implicitly_wait(4)
        choice_button.click()
        pay_money = '---选座成功！宝贝，快来付钱---'
        print('---选座成功！宝贝，快来付钱---')
        time.sleep(1)

        if pay_money != '---选座成功！宝贝，快来付钱---':
            print(pay_money)
            driver.find_element(By.XPATH, decision_true).click()
            time.sleep(1)
            print('15分钟内，快去扫码付钱!')
        else:
            print('15分钟内，快去扫码付钱!')

        pay_result = input('---付款是否成功，选择是或否---')
        if pay_result == '是':
            driver.quit()
        else:
            print('---selenium不稳定---')
