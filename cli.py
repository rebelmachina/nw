import pandas as pd
from datetime import date
from enum import Enum, auto

USERS_FILE = ".users.csv"
ASSETS_FILE = ".assets.csv"

class Command(Enum):
    ADD_USER = auto()
    ADD_ASSET = auto()
    GET_NETWORTH = auto()
    LIST_USERS = auto()
    HELP = auto()
    EXIT = auto()

    def __str__(self):
        return self.name.lower()

COMMAND_USAGE = {
    Command.ADD_USER: "add_user <username>",
    Command.ADD_ASSET: "add_asset <username> <asset_name> <value>",
    Command.GET_NETWORTH: "get_networth <username>",
    Command.LIST_USERS: "list_users",
    Command.HELP: "help",
    Command.EXIT: "exit"
}

COMMAND_DESCRIPTIONS = {
    Command.ADD_USER: "Adds a new user to the system.",
    Command.ADD_ASSET: "Adds a new asset for a specific user.",
    Command.GET_NETWORTH: "Calculates and displays the net worth of a specific user.",
    Command.LIST_USERS: "Displays a list of all users in the system.",
    Command.HELP: "Displays this help message.",
    Command.EXIT: "Exits the application."
}

COMMAND_EXAMPLES = {
    Command.ADD_USER: "add_user john",
    Command.ADD_ASSET: "add_asset john savings 5000",
    Command.GET_NETWORTH: "get_networth john",
    Command.LIST_USERS: "list_users",
    Command.HELP: "help",
    Command.EXIT: "exit"
}

def initialize_csv_files():
    try:
        pd.read_csv(USERS_FILE)
    except FileNotFoundError:
        pd.DataFrame(columns=["id", "username"]).to_csv(USERS_FILE, index=False)

    try:
        pd.read_csv(ASSETS_FILE)
    except FileNotFoundError:
        pd.DataFrame(columns=["id", "username", "asset", "value", "date"]).to_csv(
            ASSETS_FILE, index=False
        )


def add_user(username):
    users_df = pd.read_csv(USERS_FILE)
    new_id = users_df["id"].max() + 1 if not users_df.empty else 0
    new_user = pd.DataFrame({"id": [new_id], "username": [username]})
    users_df = pd.concat([users_df, new_user], ignore_index=True)
    users_df.to_csv(USERS_FILE, index=False)
    print(f"User {username} added successfully.")


def add_asset(username, asset_name, value):
    assets_df = pd.read_csv(ASSETS_FILE)
    new_id = assets_df["id"].max() + 1 if not assets_df.empty else 0
    new_asset = pd.DataFrame(
        {
            "id": [new_id],
            "username": [username],
            "asset": [asset_name],
            "value": [float(value)],
            "date": [date.today().strftime("%Y-%m-%d")],
        }
    )
    assets_df = pd.concat([assets_df, new_asset], ignore_index=True)
    assets_df.to_csv(ASSETS_FILE, index=False)
    print(f"Asset {asset_name} added for user {username}.")


def get_networth(username):
    assets_df = pd.read_csv(ASSETS_FILE)
    assets_df["date"] = pd.to_datetime(assets_df["date"])

    # Filter assets for the given user
    user_assets = assets_df[assets_df["username"] == username]

    # Group by asset and get the latest entry for each
    latest_assets = user_assets.loc[user_assets.groupby("asset")["date"].idxmax()]

    # Calculate total value of latest assets
    total_value = latest_assets["value"].sum()

    formatted_value = "{:,.2f}".format(total_value)
    current_date = date.today().strftime("%Y-%m-%d")
    print(f"Networth of {username} on {current_date} is ${formatted_value}")

def list_users():
    try:
        users_df = pd.read_csv(USERS_FILE)
        if users_df.empty:
            print("No users found.")
        else:
            print("\nUser List:")
            print(users_df.to_string(index=False))
    except FileNotFoundError:
        print("Users file not found. No users have been added yet.")

def print_help():
    help_text = "Net Worth Tracker CLI - Available Commands:\n\n"
    for command in Command:
        if command != Command.EXIT:
            help_text += f"{COMMAND_USAGE[command]}\n"
            help_text += f"   {COMMAND_DESCRIPTIONS[command]}\n"
            help_text += f"   Example: {COMMAND_EXAMPLES[command]}\n\n"
    help_text += f"{COMMAND_USAGE[Command.EXIT]}\n"
    help_text += f"   {COMMAND_DESCRIPTIONS[Command.EXIT]}"
    print(help_text)


def parse_command(input_string):
    parts = input_string.split()
    if not parts:
        return None, []
    
    command_str = parts[0].lower()
    
    try:
        command = next(cmd for cmd in Command if str(cmd) == command_str)
    except StopIteration:
        return None, []
    
    return command, parts[1:]

def main():
    initialize_csv_files()
    print("Welcome to the Net Worth Tracker CLI!")
    print_help()

    while True:
        input_string = input("Enter command (or 'exit' to quit, or 'help' to list the API): ")
        command, args = parse_command(input_string)

        if command == Command.EXIT:
            print("Thank you for using Net Worth Tracker CLI. Goodbye!")
            break
        elif command == Command.ADD_USER and len(args) == 1:
            add_user(args[0])
        elif command == Command.ADD_ASSET and len(args) == 3:
            add_asset(args[0], args[1], args[2])
        elif command == Command.GET_NETWORTH and len(args) == 1:
            get_networth(args[0])
        elif command == Command.LIST_USERS and len(args) == 0:
            list_users()
        elif command == Command.HELP and len(args) == 0:
            print_help()
        else:
            print(f"Invalid usage of '{command}'. Type 'help' for correct usage.")


if __name__ == "__main__":
    main()
