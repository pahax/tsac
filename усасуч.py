import socket, os, keyboard

file = open("ipu.txt", "r")
ip = file.readline()
ip = ip.replace("\n", "")
file.close()

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((ip, 55000))
sock.listen(10) 
while True:
    conn, addr = sock.accept()
    print('connected:', addr)
    data = conn.recv(1024)
    print(str(data))
    com = str(data).replace('b\'', '').replace('\'', '')
    if com == 'off':
        os.system('shutdown /s')
    elif com == 'close':
        keyboard.press_and_release('alt + f4')
    elif com == 'oi':
        os.system("taskkill /IM kb.exe /f")
    elif com == 'ki':
        os.startfile("kb.exe")
    elif 'send ' in com:
        com = com.replace("send ", "")
        text = com
        text = text.replace("10 ", "и")
        text = text.replace("11 ", "й")
        text = text.replace("12 ", "к")
        text = text.replace("13 ", "л")
        text = text.replace("14 ", "м")
        text = text.replace("15 ", "н")
        text = text.replace("16 ", "о")
        text = text.replace("17 ", "п")
        text = text.replace("18 ", "р")
        text = text.replace("19 ", "с")
        text = text.replace("20 ", "т")
        text = text.replace("21 ", "у")
        text = text.replace("22 ", "ф")
        text = text.replace("23 ", "х")
        text = text.replace("24 ", "ц")
        text = text.replace("25 ", "ч")
        text = text.replace("26 ", "ш")
        text = text.replace("27 ", "щ")
        text = text.replace("28 ", "ъ")
        text = text.replace("29 ", "ы")
        text = text.replace("30 ", "ь")
        text = text.replace("31 ", "э")
        text = text.replace("32 ", "ю")
        text = text.replace("33 ", "я")
        text = text.replace("1 ", "а")
        text = text.replace("2 ", "б")
        text = text.replace("3 ", "в")
        text = text.replace("4 ", "г")
        text = text.replace("5 ", "д")
        text = text.replace("6 ", "е")
        text = text.replace("7 ", "ё")
        text = text.replace("8 ", "ж")
        text = text.replace("9 ", "з")
        f = open('text.txt', 'w')
        f.write(text)
        f.close()
        os.startfile("mes.exe")
    conn.send(data)
conn.close()