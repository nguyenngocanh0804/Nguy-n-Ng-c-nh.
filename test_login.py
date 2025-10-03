import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# --- THIẾT LẬP CẤU HÌNH BAN ĐẦU ---
BASE_URL = "file:///C:/selenium/102.html" 

# Dữ liệu đăng nhập
VALID_USER = "sv1@ptit.edu.vn"  
VALID_PASS = "P@ssw0rd"      
INVALID_PASS = "SaiPass123"    

# --- KHỞI TẠO CLASS TEST ---
class LoginTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.get(BASE_URL)
        self.driver.maximize_window()
        time.sleep(1)  # load ban đầu

    def tearDown(self):
        self.driver.quit()

    # --- 6 TEST CASE ---

    def test_01_login_success(self):
        """1. Đăng nhập thành công"""
        self.driver.find_element(By.ID, "username").send_keys(VALID_USER)
        self.driver.find_element(By.ID, "password").send_keys(VALID_PASS)
        self.driver.find_element(By.ID, "btnLogin").click()
        
        # Dùng WebDriverWait thay cho sleep
        success_msg = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.ID, "msg-success"))
        )

        success_msg_style = success_msg.get_attribute("style")
        self.assertIn("block", success_msg_style, "Test 1 FAILED: Đăng nhập thành công nhưng không thấy thông báo thành công.")

    def test_02_login_invalid_password(self):
        """2. Sai thông tin đăng nhập (Sai Password)"""
        self.driver.get(BASE_URL) 
        self.driver.find_element(By.ID, "username").send_keys(VALID_USER)
        self.driver.find_element(By.ID, "password").send_keys(INVALID_PASS)
        self.driver.find_element(By.ID, "btnLogin").click()
        
        error_message = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "msg-error"))
        ).text
        self.assertIn("Invalid credentials.", error_message, "Test 2 FAILED: Thông báo lỗi không đúng.")

    def test_03_login_empty_username(self):
        """3. Bỏ trống trường (Username)"""
        self.driver.get(BASE_URL) 
        self.driver.find_element(By.ID, "username").send_keys("")  
        self.driver.find_element(By.ID, "password").send_keys(VALID_PASS)
        self.driver.find_element(By.ID, "btnLogin").click()
        
        error_message = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "msg-error"))
        ).text
        self.assertIn("Please fill all required fields.", error_message, "Test 3 FAILED: Không thấy cảnh báo yêu cầu nhập.")

    def test_04_forgot_password_link(self):
        """4. Link Forgot password?"""
        self.driver.get(BASE_URL) 
        forgot_link = self.driver.find_element(By.ID, "linkForgot")
        self.assertTrue(forgot_link.is_displayed(), "Test 4 FAILED: Link 'Forgot password?' không hiển thị.")
        self.assertNotEqual(forgot_link.get_attribute("href"), None, "Test 4 FAILED: Link không có thuộc tính href.")

    def test_05_signup_link(self):
        """5. Link SIGN UP"""
        self.driver.get(BASE_URL) 
        signup_link = self.driver.find_element(By.ID, "linkSignup")
        self.assertTrue(signup_link.is_displayed(), "Test 5 FAILED: Link 'SIGN UP' không hiển thị.")
        self.assertNotEqual(signup_link.get_attribute("href"), None, "Test 5 FAILED: Link không có thuộc tính href.")

    def test_06_social_login_buttons(self):
        """6. Nút Social login (Facebook, Twitter, Google)"""
        self.driver.get(BASE_URL) 
        buttons = {
            "Facebook": "btnFacebook",
            "Twitter": "btnTwitter",
            "Google": "btnGoogle"
        }
        
        for name, button_id in buttons.items():
            try:
                button = self.driver.find_element(By.ID, button_id)
                self.assertTrue(button.is_displayed(), f"Test 6 FAILED: Nút {name} không hiển thị.")
                
                button.click()
                time.sleep(1)
                
                self.driver.get(BASE_URL) 
                time.sleep(1)
                
            except Exception as e:
                self.fail(f"Test 6 FAILED: Lỗi xảy ra khi kiểm tra nút {name}. Chi tiết: {e}")

if __name__ == '__main__':
    unittest.main(verbosity=2)

