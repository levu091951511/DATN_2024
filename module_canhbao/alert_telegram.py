import requests
from datetime import datetime
import time
from telegram import Update

def request_api(url):
    response = requests.get(url)
    
    data = response.json()
    return data

def kiemtra_nguong(value1, giatringuong, cond):
    phan_tram_vuot = None

    if cond == ">":
        if value1 > giatringuong:
            phan_tram_vuot = ((value1 - giatringuong) / giatringuong) * 100
    elif cond == ">=":
        if value1 >= giatringuong:
            phan_tram_vuot = ((value1 - giatringuong) / giatringuong) * 100
    elif cond == "<":
        if value1 < giatringuong:
            phan_tram_vuot = ((giatringuong - value1) / giatringuong) * 100
    elif cond == "<=":
        if value1 <= giatringuong:
            phan_tram_vuot = ((giatringuong - value1) / giatringuong) * 100

    return phan_tram_vuot

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
                check = kiemtra_nguong(float(giatrichibao), item['GiaTriNguong'], item['DieuKienDatNguong'])

                if check is not None:
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
                    check = kiemtra_nguong(data_lichsugia['GiaMo'], item['GiaTriNguong'], item['DieuKienDatNguong'])
                    if check is not None:
                        send_alert(item['LoaiChiBao'], item['GiaTriNguong'], ngaygiaodich, item['BotToken'], item['ChatID'], check)
                elif item['LoaiChiBao'] == 'c':
                    check = kiemtra_nguong(data_lichsugia['GiaDong'], item['GiaTriNguong'], item['DieuKienDatNguong'])
                    if check is not None:
                        send_alert(item['LoaiChiBao'], item['GiaTriNguong'], ngaygiaodich, item['BotToken'], item['ChatID'], check)
                elif item['LoaiChiBao'] == 'h':
                    check = kiemtra_nguong(data_lichsugia['GiaCaoNhat'], item['GiaTriNguong'], item['DieuKienDatNguong'])
                    if check is not None:
                        send_alert(item['LoaiChiBao'], item['GiaTriNguong'], ngaygiaodich, item['BotToken'], item['ChatID'], check)
                elif item['LoaiChiBao'] == 'l':
                    check = kiemtra_nguong(data_lichsugia['GiaThapNhat'], item['GiaTriNguong'], item['DieuKienDatNguong'])
                    if check is not None:
                        send_alert(item['LoaiChiBao'], item['GiaTriNguong'], ngaygiaodich, item['BotToken'], item['ChatID'], check)
                elif item['LoaiChiBao'] == 'v':
                    check = kiemtra_nguong(data_lichsugia['KhoiLuong'], item['GiaTriNguong'], item['DieuKienDatNguong'])
                    if check is not None:
                        send_alert(item['LoaiChiBao'], item['GiaTriNguong'], ngaygiaodich, item['BotToken'], item['ChatID'], check)
            except:
                pass

def send_alert(loaichibao, giatricanhbao, phiengiaodich, bot_token, chat_id, phan_tram_vuot):
    message = f"🚨 Alert 🚨\n\n" \
              f"🔴 Chỉ báo: {loaichibao} đã đạt ngưỡng: {giatricanhbao}\n" \
              f"🔴 Vượt ngưỡng: {phan_tram_vuot:.2f}%\n\n" \
              f"🔴 Phiên giao dịch: {phiengiaodich}\n" \
              f"Trân trọng!"
    telegram_api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
    params = {
        "chat_id": chat_id,
        "text": message
    }
    requests.get(telegram_api_url, params=params)


data = request_api("http://127.0.0.1:8000/api/nguongcanhbao/all")
process_data(data)
