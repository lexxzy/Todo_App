def cal_temp():
    with open("files/data.txt", "r") as file:
        cal_temp = file.readlines()
    cal_temp = cal_temp[1:]
    cal_temp = [float(temp.strip("\n")) for temp in cal_temp ]
    avarage_temp = sum(cal_temp) / len(cal_temp)
    return avarage_temp

print(cal_temp())