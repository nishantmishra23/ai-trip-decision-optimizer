from auth.authentication import require_login
from utils.ui import page_header

require_login()
page_header("🗓️ AI Itinerary", "Generate a day-by-day itinerary.")
