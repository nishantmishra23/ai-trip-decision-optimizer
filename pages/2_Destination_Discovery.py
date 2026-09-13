from auth.authentication import require_login
from utils.ui import page_header

require_login()
page_header("🌍 Destination Discovery", "Explore destinations that match your preferences.")
