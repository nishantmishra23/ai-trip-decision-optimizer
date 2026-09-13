from auth.authentication import require_login
from utils.ui import page_header

require_login()
page_header("🌦️ Weather Intelligence", "Review weather conditions for smarter planning.")
