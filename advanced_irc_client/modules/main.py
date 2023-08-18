from modules.connection import connect, disconnect, receive_messages
from modules.user_actions import send_message, list_users
from modules.message_handling import format_message, notify_mention

def main():
    connect()
    receive_messages()

if __name__ == "__main__":
    main()
