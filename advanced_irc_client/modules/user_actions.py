from modules.connection import irc_socket

def send_message(message):
    if message:
        irc_socket.send(f"PRIVMSG #canal :{message}\r\n".encode("utf-8"))

def list_users():
    irc_socket.send("NAMES #canal\r\n".encode("utf-8"))
    response = irc_socket.recv(2048).decode("utf-8")
    users = response.split(":")[2].split()[2:]
    return users
