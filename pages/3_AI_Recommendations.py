from auth.authentication import require_login
from utils.ui import page_header

require_login()
page_header("🤖 AI Recommendations", "Get AI-ranked destination suggestions.")
