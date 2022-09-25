data_dict = {
    "place": 0,
    "singer" : 0,
    "sing": 0
}



while True:
    enter = input()
    if enter != "off":
        data = input().split(",")
        print(data)
        data_dict["place"] = data[0]
        data_dict["singer"] = data[1]
        data_dict["sing"] = data[2]
    else:
        print(data_dict)
        exit()
