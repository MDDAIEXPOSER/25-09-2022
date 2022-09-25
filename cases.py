def main():
    data_dict = {}
    for i in range(5):
        data_dict[i] = "case"*i
    print(data_dict)
    print(list(reversed(data_dict)))
    data_dict["new_key"] = "new_value"
    print(data_dict)
if __name__ == "__main__":
    main()
