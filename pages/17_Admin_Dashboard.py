from auth.authentication import require_admin
from utils.ui import page_header

require_admin()
page_header("👨‍💼 Admin Dashboard", "Administrator tools for AI Trip Decision Optimizer.")
