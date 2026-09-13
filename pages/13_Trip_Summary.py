from auth.authentication import require_login
from utils.ui import page_header

require_login()
page_header("📝 Trip Summary", "Review the optimized trip at a glance.")
