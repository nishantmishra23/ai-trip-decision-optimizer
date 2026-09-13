from auth.authentication import require_login
from utils.ui import page_header

require_login()
page_header("🏨 Hotel Recommendations", "Find stays that fit your budget and style.")
