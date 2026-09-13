from auth.authentication import require_login
from utils.ui import page_header

require_login()
page_header("📜 Trip History", "Look back at your previous trip plans.")
