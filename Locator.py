from selenium.webdriver.common.by import By

# --- Trường nhập ---
USERNAME = (By.ID, "username")        # ô nhập username
PASSWORD = (By.ID, "password")        # ô nhập password

# --- Nút ---
BTN_LOGIN = (By.ID, "btnLogin")       # nút LOGIN

# --- Thông báo ---
MSG_ERROR   = (By.ID, "msg-error")    # thông báo lỗi
MSG_SUCCESS = (By.ID, "msg-success")  # thông báo thành công

# --- Link điều hướng ---
LINK_FORGOT = (By.ID, "linkForgot")   # Forgot password?
LINK_SIGNUP = (By.ID, "linkSignup")   # Sign Up

# --- Nút Social Login ---
BTN_FACEBOOK = (By.ID, "btnFacebook") # Facebook
BTN_TWITTER  = (By.ID, "btnTwitter")  # Twitter
BTN_GOOGLE   = (By.ID, "btnGoogle")   # Google
