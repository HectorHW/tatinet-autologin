def read_credentials(path:str):
    lines = None
    with open(path, 'r') as file:
        lines = list(file)
    return tuple([line.strip(" \n\r\t") for line in lines])

if __name__ == '__main__':
    login, passw = read_credentials("login.txt")
    print(login, passw)