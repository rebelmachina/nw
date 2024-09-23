# nw
cli to track your networth 💸🪄

**Why use it?**
- it's dead simple, just add from time to time an asset, no need to connect your accounts to a an APP to pull the data every second.
- it's a cli, so whenever you feel bad, just run this and feel better or worse :)


## Usage

```python cli.py```

```
Welcome to the Net Worth Tracker CLI!
Net Worth Tracker CLI - Available Commands:

add_user <username>
   Adds a new user to the system.
   Example: add_user john

add_asset <username> <asset_name> <value>
   Adds a new asset for a specific user.
   Example: add_asset john savings 5000

get_networth <username>
   Calculates and displays the net worth of a specific user.
   Example: get_networth john

list_users
   Displays a list of all users in the system.
   Example: list_users

help
   Displays this help message.
   Example: help

exit
   Exits the application.
Enter command (or 'exit' to quit, or 'help' to list the API): get_networth john
Networth of john on 2024-09-23 is $10,800,254.00
```

## Roadmap
- [ ] create a backup of users and assets everytime the cli is started using names users-<YYYY-MM-DD-hh-mm>.csv and assets-<YYYY-MM-DD-hh-mm>.csv
- [ ] add endpoint `display` to display networth with a nice chart.
- [ ] do not add the same user twice to the users table.
- [ ] add endpoint `remove_asset` to remove an asset from the user's portfolio. Example `remove_asset <user> <asset> <date>(Optional: YYYY-MM-DD). If not given then it removes all assets of that type.

## Nice ideas
- [Whole Android App](https://play.google.com/store/apps/details?id=com.gianmarcodavid.networth&hl=en_US) looks pretty clean and I need to use the same categorization with assets, liabilities.
