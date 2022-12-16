#Cai dat
1. Tao  moi truong ao
    chay cau lech python -m venv venv
    bat moi truong ao: venv\Scripts\activate.bat
 - Nếu co file requiremenrs.txt chay lech pip instal -r requiremenrs.txt
 - neu k co requiremenrs.txt
2. cai dat Flast tren moi truong ao
- Chay lech: pip install Flask


## Giữ trạng thái môi trường
Trong quá trình code, và cài thư viện, thư mục `venv` có thể lên đến vài GB. Ta không thể share thư mục này, chỉ có thể share phiên bản của các thư viện. Để share phiên bản, thì dùng câu lệnh: `pip freeze > requirements.txt`