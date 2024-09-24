# nw
cli to track networth

## Roadmap
- [x] create a backup of users and assets everytime the cli is started using names users-<YYYY-MM-DD-hh-mm>.csv and assets-<YYYY-MM-DD-hh-mm>.csv
- [ ] add endpoint `display` to display networth with a nice chart.
- [x] do not add the same user twice to the users table.
- [ ] add endpoint `remove_asset` to remove an asset from the user's portfolio. Example `remove_asset <user> <asset> <date>(Optional: YYYY-MM-DD). If not given then it removes all assets of that type.
