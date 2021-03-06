<h1>
Design Document
</h1>

<h3> qa327 Structure </h3>

```
.
├── __init__.py =================> defines our flask app instance.
├── __main__.py =================> defines the program entry point.
├── frontend.py =================> defines the routes their paths through Flask Blueprints (undefined routes are passed to 404 handler)
├── models.py ===================> defines our SQL object models (Tickets and Users)
├── library =====================> contains all backend logic that is used by front-end routes.
│   ├── authenticate.py
│   ├── tickets.py
│   ├── users.py
│   └── validation.py
├── views =======================> contains all logic related to route-destination handling.
│   ├── buy.py
│   ├── home.py
│   ├── login.py
│   ├── logout.py
│   ├── register.py
│   ├── sell.py
│   └── update.py
└── templates ===================> contains all rendered HTML files.
    ├── 404.html ================> defines a 404 error page.
    ├── base.html ===============> defines a base class that all templates are inserted into.
    ├── index.html ==============> defines the home/profile page.
    ├── login.html ==============> defines the login page.
    └── register.html ===========> defines the registration page.
```

<h3> Function definitions </h3>

| Directory | File | Method | Description |
|-----------|------|--------|-------------|
| `library`   | `authenticate.py` | `authenticate(inner_function)` | Takes a function, and only allows it to be run if the user is logged in. |
| | `tickets.py` | `get_all_tickets()` | Returns all the tickets in the database as a list of Ticket objects. |
| | | `prune_expired_tickets(tickets)` | Takes a list of Ticket objects and returns that same list with all expired tickets removed.|
| | | `get_existing_tickets(name, email)` | Takes a name for tickets and an owners email and returns all matching tickets in the database. |
| | | `add_ticket(ticket_name, quantity, price, expiration, owners_email)` | Adds a new Ticket object to the database from the specified parameters. |
| | | `buy_ticket(ticket_name, quanitity, user_balance, email)` | Gets the ticket the user wants to purchase, checks that their is enough available and that the user has enought money. If errors occur then return an error message, if not remove the tickets from the database and alter the users balance. |
| | | `update_ticket(ticket_name, quantity, price, expiration)` | Checks to see if a ticket exists in the database; if the ticket exists it updates the attributes of the ticket object and returns None, else it returns an error message indicating it failed to find a ticket update |
| | `users.py` | `get_user(email)` | Gets a user from the database from a given email address. |
| | | `login_user(email, password)` | Returns a user from the database if the username and password are valid. |
| | | `register_user(email, name, password, password2, balance)` | Adds a new user to the database. |
| | | `reduce_balance(email, cost)` | Takes a user's email and a integer for a dollar value. Reduces the user's balance by the given cost. |
| | `validation.py` | `validate_email_address(email)` | Tests to ensure that a given email meets RFC 5322 standards. |
| | | `validate_password(password)` | Tests to ensure that an email meets the specifications. |
| | | `validate_ticket(ticket)` | Tests to ensure that a given ticket is valid (valid name, date, price, quantity, etc). |
| | | `validate_name(name)` | Tests to ensure that a given ticket name meets specifications. |
| | | `validate_date(expiration_date)` | Tests to ensure that a given expiration date has not already passed. |
| | | `validate_quantity(qty)`  | Tests to ensure that a given number of tickets falls within the specified range. |
| | | `validate_price(price)` | Tests to ensure that a given price falls within the specified range. |
| | | |
| | | |
| `views` | `buy.py` | `buy_get()`| Redirects a user back to their homepage if they attempt to access the buy route through get request. |
| | | `buy_post()` | Validates the user input that is put into the buy form, gives an error message if their are any otherwise calls the buy_ticket() funciton. |
| | `home.py` | `profile(user)` | Displays a given users homepage; if that user is not logged in redirects to login. |
| | `login.py` | `login_get()` | Directs a user to the homepage route if they are logged in, otherwise displays the login screen. |
| | | `login_post()` | Attempts to log a user in (redirects to homepage if successful, else redirects to login page). |
| | `logout.py` | `logout()` | Logs a user out and revokes their session token, then redirects to login page. |
| | `register.py` | `register_get()` | Displays a registration page if the user is not logged in, otherwise redirects to homepage. |
| | | `register_post()` | Attempts to register a new user in the database. Displays the login screen if the registration was successful, otherwise reloads the page. |
| | `sell.py` | `sell_get()` | Redirects the user to the homepage if they attempt to access the sell route through GET request. |
| | | `sell_post()` | Attempts to list a new batch of tickets, then redirects the user back to the homepage; failure results in an error message, success results in a successful message. |
| | `update.py` | `update_get()` | Redirects the user to the homepage if they attempt to access the update route through GET request |
| | | `update_post()` | Checks that the parameters of the ticket object are all valid and then redirects the user back to the hompage; success results in a successful message returned, failure results in an error message |
