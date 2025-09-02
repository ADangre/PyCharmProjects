def process_file():
    try:
        f = open("C:\\DAta\\input.txt", "w+")
        result =100/0
        f.write(str(result))
        f.close()
    except FileNotFoundError as e:
        print(e)
    finally:
        f.close()
        print("file closed irrespective of operation not completed and exception not handled")
process_file()
