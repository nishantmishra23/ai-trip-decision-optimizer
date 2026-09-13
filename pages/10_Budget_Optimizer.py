from auth.authentication import require_login
from utils.ui import page_header

require_login()
page_header("💰 Budget Optimizer", "Allocate your trip budget more effectively.")
