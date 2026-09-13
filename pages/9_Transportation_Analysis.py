from auth.authentication import require_login
from utils.ui import page_header

require_login()
page_header("🚆 Transportation Analysis", "Compare transport options and estimated costs.")
