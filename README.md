Broken Authentication URL Scanner

Một ứng dụng web đơn giản viết bằng **Python + Streamlit**, giúp dò tìm các **đường dẫn nhạy cảm** trên website như `/admin`, `/config`, `/backup.zip`, `/test.php`, v.v... nhằm hỗ trợ kiểm thử **lỗ hổng Broken Authentication URL** hoặc **Security Misconfiguration**.

---

## Tính năng

- Dò các đường dẫn nhạy cảm từ wordlist
- Kiểm tra phản hồi HTTP (status code, nội dung)
- Cảnh báo nếu đường dẫn tồn tại (HTTP 200)


---

## Công nghệ

- Python 3.x
- Streamlit
- Requests


---

## Cài đặt

### 1. Tạo môi trường ảo

```bash
python3 -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
