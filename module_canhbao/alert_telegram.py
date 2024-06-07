import requests
from datetime import datetime
import time
from telegram import Update

def request_api(url):
    response = requests.get(url)
    
    data = response.json()
    return data

def kiemtra_nguong(value1, giatringuong):
    if value1 >= giatringuong:
        return True
    return False

def process_data(data):
    for item in data['nguongcanhbao']:
        if item['LoaiChiBao'] not in ['c', 'o', 'h', 'l', 'v']:
            try:
                # Xử lý request cho trường hợp loại chỉ báo khác
                mack = item['MaChungKhoan']
                loaichibao = item['LoaiChiBao']
                ngaygiaodich = datetime.now().strftime('%Y-%m-%d')
                new_api_url = f"http://127.0.0.1:8000/api/chibao/{mack}/{loaichibao}/{ngaygiaodich}"

                chibao = request_api(new_api_url)
                # print(chibao['giatrichibao'])
                giatrichibao = chibao['giatrichibao'][0]['GiaTriChiBao']
                check = kiemtra_nguong(float(giatrichibao), item['GiaTriNguong'])

                if check:
                    send_alert(item['LoaiChiBao'], item['GiaTriNguong'], ngaygiaodich, item['BotToken'], item['ChatID'])
            except:
                pass
        else:
            try:
                # Xử lý request cho trường hợp loại chỉ báo là c, o, h, l hoặc v
                mack = item['MaChungKhoan']
                ngaygiaodich = datetime.now().strftime('%Y-%m-%d')
                new_api_url = f"http://127.0.0.1:8000/api/lichsugia/{mack}/{ngaygiaodich}"
                data_lichsugia = request_api(new_api_url)
                data_lichsugia=data_lichsugia['factlichsugia'][0]
                
                if item['LoaiChiBao'] == 'o':
                    if kiemtra_nguong(data_lichsugia['GiaMo'], item['GiaTriNguong']):
                        send_alert(item['LoaiChiBao'], item['GiaTriNguong'], ngaygiaodich, item['BotToken'], item['ChatID'])
                elif item['LoaiChiBao'] == 'c':
                    if kiemtra_nguong(data_lichsugia['GiaDong'], item['GiaTriNguong']):
                        send_alert(item['LoaiChiBao'], item['GiaTriNguong'], ngaygiaodich, item['BotToken'], item['ChatID'])
                elif item['LoaiChiBao'] == 'h':
                    if kiemtra_nguong(data_lichsugia['GiaCaoNhat'], item['GiaTriNguong']):
                        send_alert(item['LoaiChiBao'], item['GiaTriNguong'], ngaygiaodich, item['BotToken'], item['ChatID'])

                elif item['LoaiChiBao'] == 'l':
                    if kiemtra_nguong(data_lichsugia['GiaThapNhat'], item['GiaTriNguong']):
                        send_alert(item['LoaiChiBao'], item['GiaTriNguong'], ngaygiaodich, item['BotToken'], item['ChatID'])
                elif item['LoaiChiBao'] == 'v':
                    if kiemtra_nguong(data_lichsugia['KhoiLuong'], item['GiaTriNguong']):
                        send_alert(item['LoaiChiBao'], item['GiaTriNguong'], ngaygiaodich, item['BotToken'], item['ChatID'])
            except:
                pass

def send_alert(loaichibao, giatricanhbao, phiengiaodich, bot_token, chat_id):
    mesage = f"🚨 Alert 🚨\n\n" \
            f"🔴 Chỉ báo: " + str(loaichibao) + " đã đạt ngưỡng: " + str(giatricanhbao) + "\n" \
            f"🔴 Phiên giao dịch: " + str(phiengiaodich) +  "\n\n" \
            f"Trân trọng !"
    telegram_api_url = 'https://api.telegram.org/bot' + bot_token + "/sendMessage"
    params = {
        "chat_id": chat_id,
        "text": mesage
    }
    requests.get(telegram_api_url, params=params)

while True:
    data = request_api("http://127.0.0.1:8000/api/nguongcanhbao/all")
    process_data(data)
    time.sleep(60)