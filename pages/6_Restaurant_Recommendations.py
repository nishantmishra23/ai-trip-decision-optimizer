from auth.authentication import require_login
from utils.ui import page_header

require_login()
page_header("🍴 Restaurant Recommendations", "Discover dining options at your destination.")
