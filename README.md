###**HƯỚNG DẪN CHẠY TEST**  
# Selenium Login Test

## Mô tả
Bộ test tự động kiểm tra các chức năng đăng nhập trên trang **102.html**:
1. Đăng nhập thành công.
2. Sai mật khẩu.
3. Bỏ trống thông tin username.
4. Kiểm tra link "Forgot password?".
5. Kiểm tra link "SIGN UP".
6. Kiểm tra nút đăng nhập mạng xã hội: Facebook, Twitter, Google.

---

## Yêu cầu
- Python 3.13+  
- Trình duyệt Chrome cùng với ChromeDriver
- Thư viện Python:
  - selenium
  - webdriver-manager

---

## Cài đặt thư viện
Mở CMD 
Gõ các lệnh  
- pip install selenium webdriver-manager  
- cd C:\selenium  
- python test_login.py -v    
- Màn hình sẽ hiện ra kết quả:
![ảnh](https://github.com/nguyenngocanh0804/Nguy-n-Ng-c-nh./blob/7ac467ebb8dafda0b0126716bc081d0387ef8ee4/%E1%BA%A2nh%20ch%E1%BB%A5p%20minh%20ch%E1%BB%A9ng.png)
