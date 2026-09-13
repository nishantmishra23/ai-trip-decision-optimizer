from auth.authentication import require_login
from utils.ui import page_header

require_login()
page_header("🎯 Activity Recommendations", "Choose activities aligned with your interests.")
