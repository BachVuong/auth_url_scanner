import streamlit as st
from scanner.auth_scanner import load_paths, scan_sensitive_paths

st.set_page_config(page_title="Auth URL Scanner", page_icon="🔐")

st.title("🔐 Broken Auth URL Scanner")
st.markdown("Nhập URL để kiểm tra các đường dẫn dễ bị bỏ sót bảo mật (admin, backup, config...)")

target = st.text_input("🌐 Nhập URL gốc:", "http://testphp.vulnweb.com")

if st.button("🚀 Quét đường dẫn nhạy cảm"):
    st.info("🔍 Đang quét...")
    paths = load_paths("payloads/paths.txt")
    results = scan_sensitive_paths(target, paths)

    st.markdown("## ✅ Kết quả")

    if results:
        for url, code in results:
            st.warning(f"⚠️ Tồn tại: {url} (status: {code})")
    else:
        st.success("🎉 Không phát hiện đường dẫn nhạy cảm nào tồn tại.")

