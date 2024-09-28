from cli import display_networth
from datetime import datetime

# Example usage:
display_networth(
    "JohnDoe", datetime.now().strftime("%Y-%m-%d"), 259826.00, 80
)  # 80 characters wide line
