import re
import emoji
from termcolor import colored
from modules.connection import irc_socket
from modules.user_actions import send_message

def format_message(user, decrypted_message):
    formatted_message = f"{user}: {decrypted_message}"
    if user == "Você":
        formatted_message = colored(formatted_message, "blue", attrs=["bold"])
    elif "mencionar_seu_nome" in decrypted_message.lower():
        notify_mention(user, decrypted_message)
        formatted_message = colored(formatted_message, "red", attrs=["bold"])
    elif emoji.emoji_count(decrypted_message) > 0:
        formatted_message = colored(formatted_message, "yellow")
    return formatted_message

def notify_mention(user, message):
    send_message(f"Você foi mencionado por {user}: {message}")
