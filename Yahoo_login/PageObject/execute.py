from selenium.webdriver.common.by import By
from Base.base import Base

class Login(Base):
    #輸入帳號
    def type_id(self, i):
        self.findele(By.ID, "login-username").send_keys(i)
    '''按確認'''
    def next1(self):
        self.findele(By.ID, 'login-signin').click()
    '''輸入密碼'''
    def type_password(self, i):
        self.findele(By.ID, 'login-passwd').send_keys(i)
    '''在下一步'''
    def next2(self):
        self.findele(By.ID, 'login-signin').click()
    '''因輸入密碼後會回到首頁，此時點選進入信箱'''
    def enter_email(self):
        self.findele(By.XPATH, '//span[@class="D(ib) Fz(14px) Fw(b) Lh(24px) Pstart(38px)"]').click()

    def login_yahoo(self, id, password):
        self.type_id(id)
        self.next1()
        self.type_password(password)
        self.next2()
        self.enter_email()

