#coding = utf-8
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os


class Auto:

    # 加载chrome配置
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get("https://a.weixin.qq.com")
        # 显性等待60s
        WebDriverWait(self.driver,60,0.5).until(
            EC.title_is('微信广告服务商平台')
        )

        self.h = self.driver.current_window_handle
    #传入公众号原始ID
    def put_ID(self,str):
        try:
            self.wait_class_name("TextInput_new__input-3wfiz")
            op = self.find_class_name("TextInput_new__input-3wfiz")
            op.send_keys(str)
        except Exception:
            print("输入原始ID异常")

    #通过link_text定位
    def find_link_text(self,str):
        try:
            mouse = self.driver.find_element_by_link_text(str)
            ActionChains(self.driver).move_to_element(mouse).perform()
            mouse.click()
            return mouse
        except Exception:
            print("定位元素异常")

    #通过id定位
    def find_id(self,str):
        try:
            mouse = self.driver.find_element_by_id(str)
            ActionChains(self.driver).move_to_element(mouse).perform()
            mouse.click()
            return mouse
        except Exception:
            print("定位元素异常")

    #通过class_name定位
    def find_class_name(self,str):
        try:
            mouse = self.driver.find_element_by_class_name(str)
            ActionChains(self.driver).move_to_element(mouse).perform()
            mouse.click()
            return mouse
        except Exception:
            print("定位元素异常")

    #通过css_selector定位
    def find_css_selector(self,str):
        try:
            mouse = self.driver.find_element_by_css_selector(str)
            ActionChains(self.driver).move_to_element(mouse).perform()
            mouse.click()
            return mouse
        except Exception:
            print("定位元素异常")

    # 通过xpath定位
    def find_xpath(self,str):
        try:
            mouse = self.driver.find_element_by_xpath(str)
            ActionChains(self.driver).move_to_element(mouse).perform()
            mouse.click()
            return mouse
        except Exception:
            print("定位元素异常")

    #创建等待ID方法
    def wait_ID(self,str):
        try:
            WebDriverWait(self.driver,15).until(
                EC.element_to_be_clickable((By.ID,str))
            )
        except Exception:
            print("定位元素异常")

    # 创建等待text方法
    def wait_text(self,str):
        try:
            WebDriverWait(self.driver,15).until(
                EC.element_to_be_clickable((By.LINK_TEXT,str))
            )
        except Exception:
            print("等待元素时异常")

    # 创建等待class_name方法
    def wait_class_name(self,str):
        try:
            WebDriverWait(self.driver,15).until(
                EC.element_to_be_clickable((By.CLASS_NAME,str))
            )
        except Exception:
            print("等待元素时异常")

    # 创建等待css_selector方法
    def wait_selector(self,str):
        try:
            WebDriverWait(self.driver,15).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR,str))
            )
        except Exception:
            print("等待元素时异常")

    # 创建等待xpath方法
    def wait_xpath(self,str):
        try:
            WebDriverWait(self.driver,15).until(
                EC.element_to_be_clickable((By.XPATH,str))
            )
        except Exception:
            print("等待元素时异常")

    #切换到当前窗口
    def changeWindow(self):
        try:
            all_h = self.driver.window_handles
            self.driver.switch_to.window(all_h[0])
        except Exception:
            print("等待元素时异常")

    # def changeWindow(self):
    #     try:
    #         # 定义所有句柄
    #         all_h = self.driver.window_handles
    #         for i in all_h:
    #             if i != self.h:
    #                 self.driver.switch_to.window(i)
    #     except Exception:
    #         print("未切换到当前窗口")

    #上传底部and小程序图片方法
    def upload_image(self,str):
        try:
            # 定位文件的所处文件夹的绝对路径
            file_path = os.path.abspath('.')
            # 上传图片
            js = 'document.querySelector("#wxadcontainer > div > div > div.Layout__content-2-HFB > main > div > div:nth-child(2) > div.CreativeEdit__wrapper-yYdbq > div.CreativeEdit__content-L-fNC > section > form > div:nth-child(2) > div > div:nth-child(1) > div > div.rc-upload.Upload__button-yFgla > input[type=\'file\']")'
            # 执行js
            self.driver.execute_script(js)
            time.sleep(1)
            # 定位元素
            upload = self.driver.find_element_by_css_selector("#wxadcontainer > div > div > div.Layout__content-2-HFB > main > div > div:nth-child(2) > div.CreativeEdit__wrapper-yYdbq > div.CreativeEdit__content-L-fNC > section > form > div:nth-child(2) > div > div:nth-child(1) > div > div.rc-upload.Upload__button-yFgla > input[type='file']")
            upload.send_keys(file_path + str)
            time.sleep(1)

        except Exception:
            print("上传图片异常")

    # 上传文中图片方法
    def upload_image_middle(self, str):
        try:
            # 定位文件的所处文件夹的绝对路径
            file_path = os.path.abspath('.')
            # 上传图片
                                          #wxadcontainer > div > div > div.Layout__content-2-HFB > main > div > div:nth-child(2) > div.CreativeEdit__wrapper-yYdbq > div.CreativeEdit__content-L-fNC > section > form > div:nth-child(1) > div > div:nth-child(1) > div > div.rc-upload.Upload__button-yFgla > input[type="file"]
            js = 'document.querySelector("#wxadcontainer > div > div > div.Layout__content-2-HFB > main > div > div:nth-child(2) > div.CreativeEdit__wrapper-yYdbq > div.CreativeEdit__content-L-fNC > section > form > div:nth-child(1) > div > div:nth-child(1) > div > div.rc-upload.Upload__button-yFgla > input[type=\'file\']")'
            # 执行js
            self.driver.execute_script(js)
            time.sleep(1)
            # 定位元素
            upload = self.driver.find_element_by_css_selector(
                 #wxadcontainer > div > div > div.Layout__content-2-HFB > main > div > div:nth-child(2) > div.CreativeEdit__wrapper-yYdbq > div.CreativeEdit__content-L-fNC > section > form > div:nth-child(1) > div > div:nth-child(1) > div > div.rc-upload.Upload__button-yFgla > input[type="file"]
                "#wxadcontainer > div > div > div.Layout__content-2-HFB > main > div > div:nth-child(2) > div.CreativeEdit__wrapper-yYdbq > div.CreativeEdit__content-L-fNC > section > form > div:nth-child(1) > div > div:nth-child(1) > div > div.rc-upload.Upload__button-yFgla > input[type='file']")
            upload.send_keys(file_path + str)
            time.sleep(1)

        except Exception:
            print("上传文中图片异常")

    #传入广告名称
    def put_ad_name(self,str):
        try:
            self.wait_class_name("EditableText__input-2lFnB")
            op = self.find_class_name("EditableText__input-2lFnB")
            # 调用键盘事件ctrl+a backspace
            op.send_keys(Keys.CONTROL, 'a')
            op.send_keys(Keys.BACKSPACE)
            op.send_keys(str)
        except Exception:
            print("传入广告名称异常")

    #点击上线时间框,修改上线时间
    def set_start_date(self,str):
        try:
            self.wait_class_name("el-input__inner")
            op = self.find_class_name("el-input__inner")
            # 调用键盘事件ctrl+a backspace
            op.send_keys(Keys.CONTROL, 'a')
            op.send_keys(Keys.BACKSPACE)
            op.send_keys(str)
        except Exception:
            print("传入上线时间异常")

    #点击结束时间框,修改结束时间
    def set_stop_date(self,str):
        try:
            self.wait_selector("#bid_end_time > div > div.el-date-picker-placement-bottomLeft > span > div > input")
            op = self.find_css_selector("#bid_end_time > div > div.el-date-picker-placement-bottomLeft > span > div > input")
            # 调用键盘事件ctrl+a backspace
            op.send_keys(Keys.CONTROL, 'a')
            op.send_keys(Keys.BACKSPACE)
            op.send_keys(str)
        except Exception:
            print("传入下线时间异常")

    #校验方法by_class_name
    def validate_class_name(self,str1,str2,str3):
        self.wait_class_name(str1)
        s = self.driver.find_element_by_class_name(str1).get_attribute('value')
        if s != str2:
            time.sleep(0.5)
            self.set_start_date(str3)
            # 点击页面空白处
            self.wait_class_name("Form__label-2NSY1")
            self.find_class_name("Form__label-2NSY1")

    # 校验方法by_css_selector
    def validate_css_selector(self, str1, str2,str3):
        self.wait_selector(str1)
        s = self.driver.find_element_by_css_selector(str1).get_attribute('value')
        if s != str2:
            time.sleep(0.5)
            self.set_stop_date(str3)
            # 点击页面空白处
            self.wait_class_name("Form__label-2NSY1")
            self.find_class_name("Form__label-2NSY1")

    #校验出价by_price
    def validate_price(self, str1, str2):
        # time.sleep(0.5)
        self.wait_selector(str1)
        s = self.driver.find_element_by_css_selector(str1).get_attribute('value')

        if s != str2:
            time.sleep(0.5)
            self.set_unit_price("0.5")

    #传入公众号原始ID->点击推广我的公众号
    def clickMyWechat(self,str1,str2):
        self.wait_xpath("//*[@id=\"root\"]/div/span/div/main/div/div[2]/div/div[3]/button")
        self.put_ID(str1)
        # 点击查询按钮
        # time.sleep(0.5)
        self.wait_class_name("TextInput_new__right-iVlUV")
        self.find_class_name("TextInput_new__right-iVlUV")


        self.wait_text("广告投放")
        # time.sleep(0.5)
        # 点击广告投放
        self.find_link_text("广告投放")

        time.sleep(1.5)

        try:
            self.driver.close()
        except Exception:
            print("关闭窗口异常")

        # time.sleep(0.5)

        # 切换到当前窗口
        self.changeWindow()

        # WebDriverWait(self.driver,60,0.5).until(
        #     EC.title_is('微信公众平台')
        # )


        # 点击创建广告
        self.wait_text("创建广告")
        time.sleep(0.5)
        self.find_link_text("创建广告")

        time.sleep(1.5)
        try:
            self.driver.close()
        except Exception:
            print("关闭窗口异常")


        self.changeWindow()

        #传入投放计划名称
        try:
            self.wait_class_name("EditableText__input-2lFnB")
            op = self.find_class_name("EditableText__input-2lFnB")
            # 调用键盘事件,ctrl+a backspace
            op.send_keys(Keys.CONTROL,'a')
            op.send_keys(Keys.BACKSPACE)
            op.send_keys(str2)
        except Exception:
            print("传入投放计划名称异常")

        # 点击推广我的公众号
        self.wait_ID("PRODUCTTYPE_WECHAT")
        self.find_id("PRODUCTTYPE_WECHAT")

    #输入每日预算
    def set_budget(self,str):
        try:
            self.wait_selector("#day_budget_input > div > input")
            op = self.find_css_selector("#day_budget_input > div > input")
            # 调用键盘事件ctrl+a backspace
            op.send_keys(Keys.CONTROL, 'a')
            op.send_keys(Keys.BACKSPACE)
            op.send_keys(str)
        except Exception:
            print("输入每日预算异常")

     #输入出价
    def set_unit_price(self,str):
        try:
            time.sleep(0.5)
            self.wait_selector("#price_input > div > input")
            op = self.find_css_selector("#price_input > div > input")
            # jquery设置不允许使用键盘事件,此处使用 send.clear()清空
            op.clear()
            time.sleep(0.5)
            op.send_keys(str)
            time.sleep(0.1)
        except Exception:
            print("输入出价异常")

    #进入广告服务商初始界面
    def again(self):
        try:
            self.driver.get("https://a.weixin.qq.com/client")
        except Exception:
            print("跳转到服务商初始界面异常")

    #处理弹出框
    def alert(self):
        try:
            result = EC.alert_is_present()(self.driver)
            while result:
                result.accept()
        except Exception:
            print("处理弹出框异常")

    #判断广告类型
    def judgment(self,str):
        try:
            if str == "底部":
                self.find_id("pos_0")
            elif str == "小程序":
                self.find_id("pos_7")
            elif str == "文中":
                self.find_id("pos_5")
        except Exception:
            pass

    # 校验元素是否存在
    def is_agree(self):
        s = self.driver.find_elements_by_class_name("Checkbox__selected-2FrMC")
        if len(s) == 0:
            return True
        elif len(s) == 1:
            return False
        else:
            return True

    #方法整合
    def auto_ad(self,id,position,start_date,stop_date,ad_name,is_ocpa):
        self.again()
        # 处理确认消息框
        self.alert()
        self.clickMyWechat(id,ad_name)
        #判断广告类型
        self.judgment(position)
        self.wait_ID("plan_next_step")

        # 点击下一步
        self.wait_ID("plan_next_step")
        self.find_id("plan_next_step")

        time.sleep(0.5)
        # 点击上线时间框,修改上线时间
        self.set_start_date(start_date)

        # 点击页面空白处
        self.wait_class_name("Form__label-2NSY1")
        self.find_class_name("Form__label-2NSY1")

        # 校验上线时间
        self.validate_class_name("el-input__inner", start_date, start_date)

        time.sleep(0.5)
        # 点击结束时间框,修改结束时间
        self.set_stop_date(stop_date)

        # 点击页面空白处
        self.wait_class_name("Form__label-2NSY1")
        self.find_class_name("Form__label-2NSY1")

        # 校验结束时间
        self.validate_css_selector("#bid_end_time > div > div.el-date-picker-placement-bottomLeft > span > div > input",stop_date, stop_date)

        # 传入广告名称
        self.put_ad_name(ad_name)

        # 点击地域选择框
        self.wait_class_name("choices2__selected-wrapper")
        self.find_class_name("choices2__selected-wrapper")

        # 点击全选
        self.wait_text("全选")
        self.find_link_text("全选")

        # 输入预算,选择出价方式 CPC
        try:
            if is_ocpa == "否":
                self.set_budget("50")
                self.wait_selector("#wxadcontainer > div > div > div.Layout__content-2-HFB > main > div > div > div:nth-child(3) > div > div:nth-child(2) > div > div.AdGroupEdit__content-tqhFz > section:nth-child(2) > section > form > div > div:nth-child(2) > div > div > div:nth-child(1) > label")
                self.find_css_selector("#wxadcontainer > div > div > div.Layout__content-2-HFB > main > div > div > div:nth-child(3) > div > div:nth-child(2) > div > div.AdGroupEdit__content-tqhFz > section:nth-child(2) > section > form > div > div:nth-child(2) > div > div > div:nth-child(1) > label")
                time.sleep(1)
                suffix = ''
            elif is_ocpa == "是":
                self.set_budget("1000")
                self.wait_selector("#wxadcontainer > div > div > div.Layout__content-2-HFB > main > div > div > div:nth-child(3) > div > div:nth-child(2) > div > div.AdGroupEdit__content-tqhFz > section:nth-child(2) > section > form > div > div:nth-child(2) > div > div > div:nth-child(2) > label")
                self.find_css_selector("#wxadcontainer > div > div > div.Layout__content-2-HFB > main > div > div > div:nth-child(3) > div > div:nth-child(2) > div > div.AdGroupEdit__content-tqhFz > section:nth-child(2) > section > form > div > div:nth-child(2) > div > div > div:nth-child(2) > label")
                time.sleep(1)
                suffix = 'ocpa'
        except Exception:
            pass

        # 输入出价
        self.set_unit_price("0.5")
        #校验出价
        # time.sleep(0.5)
        self.validate_price("#price_input > div > input",'0.5')

        # 点击下一步
        self.wait_ID("target_next_step")
        self.find_id("target_next_step")
        time.sleep(1)

        #文中上传图片
        if position == "文中":
            self.upload_image_middle("/" + position + suffix + "/" + ad_name)
            time.sleep(0.5)

            try:
                self.wait_class_name("TreeSelect__input-1Ii4m")
                op = self.find_class_name("TreeSelect__input-1Ii4m")
                op.send_keys("生活服务-休闲娱乐")

                self.wait_selector("#wxadcontainer > div > div > div.Layout__content-2-HFB > main > div > div:nth-child(2) > div.CreativeEdit__wrapper-yYdbq > div.CreativeEdit__content-L-fNC > section > form > div:nth-child(2) > div > label")
                self.find_css_selector("#wxadcontainer > div > div > div.Layout__content-2-HFB > main > div > div:nth-child(2) > div.CreativeEdit__wrapper-yYdbq > div.CreativeEdit__content-L-fNC > section > form > div:nth-child(2) > div > label")
                time.sleep(1)
            except Exception as e:
                print(e)

        else:
            # 底部和小程序上传图片
            self.upload_image("/"+position+ suffix +"/" + ad_name)
            time.sleep(1)


        # 点击下一步
        self.wait_class_name("Button_new__primary-2diSJ")
        self.find_class_name("Button_new__primary-2diSJ")


        # 点击我同意
        if self.is_agree():
            self.wait_class_name("Checkbox__label-3_Crb")
            self.find_class_name("Checkbox__label-3_Crb")

        # self.wait_class_name("Checkbox__selected-2FrMC")
        # time.sleep(5)
        # 点击提交
        self.wait_selector("#test_submit_all > span")
        self.find_css_selector("#test_submit_all > span")
        time.sleep(1)






