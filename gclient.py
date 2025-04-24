import socket

host = "192.168.1.56"  
port = 7777

s = socket.socket()
s.connect((host, port))

difficulty_prompt = s.recv(1024).decode()
print(difficulty_prompt)

bot_choice = input("Enter difficulty choice: ").strip()
s.sendall(f"{bot_choice}\n".encode())  

if bot_choice == '1':
    low = 1
    high = 10
elif bot_choice == '2':
    low = 1
    high = 50
else:
    low = 1
    high = 100

banner = s.recv(1024).decode()
print(banner)

while True:
    guess = (low + high) // 2
    print(f"Bot guesses: {guess}")
    s.sendall(f"{guess}\n".encode())

    response = s.recv(1024).decode().strip()
    print(response)

    if "CORRECT!" in response:
        break
    elif "Lower" in response:
        high = guess - 1
    elif "Higher" in response:
        low = guess + 1
    else:
        print("Unexpected response from server.")
        break

s.close()
