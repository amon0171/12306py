# -*- coding: utf-8 -*-

from _12306.get_stations import *

'''
5-7 目的地 3  车次 6  出发地 8  出发时间 9  到达时间 10 历时 26 无坐 29 硬座
24 软座 28 硬卧 33 动卧 23 软卧 21 高级软卧 30 二等座 31 一等座 32 商务座特等座
'''
data = []
type_data = []


def query(date, from_station, to_station):

    data.clear()
    type_data.clear()
    headers = {
        'Cookie': "_uab_collina=163999108472034091142832; JSESSIONID=C5C4C5E7526DC0B7BFC6A5717D1F8380; "
                  "BIGipServerotn=368050698.24610.0000; BIGipServerpool_passport=115606026.50215.0000; "
                  "RAIL_EXPIRATION=1640270981777; "
                  "RAIL_DEVICEID=lbec11dld1VeM-sTt"
                  "-5XFnXTNwhNgpCur_gC8sJjGNMKKBV3uSi0ISD97wfIwWm3kwTRoZUeiv4uB7BtHpBl_bA_6px32mcN8aNpC6MMoP9VmpMINrZxxaQM_KNWIV7rZ7mND7kKrQxv5MTYmOMh6-I-KYFHkTvj; guidesStatus=off; highContrastMode=defaltMode; cursorStatus=off; route=495c805987d0f5c8c84b14f60212447d; _jc_save_fromDate=2021-12-20; _jc_save_toDate=2021-12-20; _jc_save_wfdc_flag=dc; _jc_save_fromStation=%u5317%u4EAC%2CBJP; _jc_save_toStation=%u4E0A%u6D77%2CSHH",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.62 "
    }
    # 查询请求地址
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={' \
          '}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
        date, from_station, to_station)
    # 发送查询请求
    response = requests.get(url=url, headers=headers)
    response.encoding = response.apparent_encoding
    # # 将json数据转换为字典类型，通过键值对取数据
    if response.status_code != 200:  # 直接返回空
        return data

    result = response.json()['data']['result']
    # for i in result:
    #     print(i)

    if isStations():
        stations = eval(read())  # 读取所有车站并转换为dic类型
        if len(result) != 0:  # 判断返回数据是否为空
            for i in result:
                # # 分割数据并添加到列表中
                tmp_list = i.split('|')
                from_station = list(stations.keys())[list(stations.values()).index(tmp_list[6])]
                to_station = list(stations.keys())[list(stations.values()).index(tmp_list[7])]
                seat = [tmp_list[3], from_station, to_station, tmp_list[8], tmp_list[9], tmp_list[10], tmp_list[32],
                        tmp_list[31], tmp_list[30], tmp_list[21], tmp_list[23], tmp_list[33], tmp_list[28],
                        tmp_list[24], tmp_list[29], tmp_list[26]]
                newSeat = []
                for s in seat:
                    if s == "":
                        s = "--"
                    else:
                        s = s
                    newSeat.append(s)  # 保存新的座位信息
                data.append(newSeat)
        return data  # 返回整理好的车次信息


# 获取高铁信息的方法
def g_vehicle():
    if len(data) != 0:
        for g in data:  # 循环所有火车数据
            i = g[0].startswith('G')  # 判断车次首字母是不是高铁
            if i:  # 如果是将该条信息添加到高铁数据中
                type_data.append(g)


# 移除高铁信息的方法
def r_g_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for g in data:
            i = g[0].startswith('G')
            if i:  # 移除高铁信息
                type_data.remove(g)


# 获取动车信息的方法
def d_vehicle():
    if len(data) != 0:
        for d in data:  # 循环所有火车数据
            i = d[0].startswith('D')  # 判断车次首字母是不是动车
            if i == True:  # 如果是将该条信息添加到动车数据中
                type_data.append(d)


# 移除动车信息的方法
def r_d_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for d in data:
            i = d[0].startswith('D')
            if i == True:  # 移除动车信息
                type_data.remove(d)


# 获取直达车信息的方法
def z_vehicle():
    if len(data) != 0:
        for z in data:  # 循环所有火车数据
            i = z[0].startswith('Z')  # 判断车次首字母是不是直达
            if i == True:  # 如果是将该条信息添加到直达数据中
                type_data.append(z)


# 移除直达车信息的方法
def r_z_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for z in data:
            i = z[0].startswith('Z')
            if i == True:  # 移除直达车信息
                type_data.remove(z)


# 获取特快车信息的方法
def t_vehicle():
    if len(data) != 0:
        for t in data:  # 循环所有火车数据
            i = t[0].startswith('T')  # 判断车次首字母是不是特快
            if i == True:  # 如果是将该条信息添加到特快车数据中
                type_data.append(t)


# 移除特快车信息的方法
def r_t_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for t in data:
            i = t[0].startswith('T')
            if i == True:  # 移除特快车信息
                type_data.remove(t)


# 获取快速车数据的方法
def k_vehicle():
    if len(data) != 0:
        for k in data:  # 循环所有火车数据
            i = k[0].startswith('K')  # 判断车次首字母是不是快车
            if i == True:  # 如果是将该条信息添加到快车数据中
                type_data.append(k)


# 移除快速车数据的方法
def r_k_vehicle():
    if len(data) != 0 and len(type_data) != 0:
        for k in data:
            i = k[0].startswith('K')
            if i == True:  # 移除快车信息
                type_data.remove(k)
