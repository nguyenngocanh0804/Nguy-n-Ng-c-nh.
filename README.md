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
![ảnh](https://github.com/nguyenngocanh0804/Nguy-n-Ng-c-nh./blob/52e0394dfe3af4fa8f954a5144801e3b1a25dea1/%E1%BA%A2nh%20ch%E1%BB%A5p%20m%C3%A0n%20h%C3%ACnh%202025-10-03%20102752.png)
