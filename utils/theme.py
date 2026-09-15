"""
Centralized Theme & Visual Design Manager for AI Trip Decision Optimizer.
Provides Light & Dark theme tokens, global CSS injection, dynamic Plotly styling, and theme switcher widgets.
"""
import streamlit as st

def init_theme():
    """Ensure theme state is initialized in session_state."""
    if "theme_mode" not in st.session_state:
        st.session_state["theme_mode"] = "dark"


def get_current_theme() -> str:
    """Return the active theme mode: 'dark' or 'light'."""
    init_theme()
    return st.session_state.get("theme_mode", "dark")


def render_theme_switcher():
    """Render a clean theme mode toggle in the sidebar."""
    init_theme()
    current = st.session_state["theme_mode"]
    
    st.sidebar.markdown("### :material/palette: Visual Mode")
    selected = st.sidebar.radio(
        "Theme Switcher",
        options=["🌙 Dark Mode", "☀️ Light Mode"],
        index=0 if current == "dark" else 1,
        key="theme_radio_switcher",
        label_visibility="collapsed"
    )
    
    new_mode = "dark" if "Dark" in selected else "light"
    if new_mode != current:
        st.session_state["theme_mode"] = new_mode
        st.rerun()


def inject_theme_css():
    """Inject global CSS rules tailored to the active Light / Dark theme."""
    mode = get_current_theme()
    
    base_css = """
    <style>
        /* Hide Streamlit Header, Top 3-Dots Hamburger Menu & Footer */
        #MainMenu { visibility: hidden !important; display: none !important; }
        header[data-testid="stHeader"] { visibility: hidden !important; display: none !important; height: 0 !important; }
        [data-testid="stHeader"] { display: none !important; }
        [data-testid="stToolbar"] { visibility: hidden !important; display: none !important; }
        [data-testid="stDecoration"] { display: none !important; }
        [data-testid="stStatusWidget"] { display: none !important; }
        footer { visibility: hidden !important; display: none !important; }
        button[title="View fullscreen"] { display: none !important; }

        /* General Typography & Immersion */
        body, .stApp {
            font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif !important;
        }

        /* Hero Header Banner Component */
        .app-hero-banner {
            padding: 1.75rem 2rem;
            border-radius: 16px;
            margin-bottom: 1.5rem;
            border: 1px solid var(--border-color);
            background: linear-gradient(135deg, var(--bg-hero-start) 0%, var(--bg-hero-end) 100%);
            box-shadow: 0 8px 24px -6px rgba(0, 0, 0, 0.15);
        }
        .app-hero-title {
            font-size: 2rem !important;
            font-weight: 800 !important;
            margin: 0 0 0.4rem 0 !important;
            line-height: 1.2 !important;
        }
        .app-hero-subtitle {
            font-size: 1.05rem !important;
            opacity: 0.88;
            margin: 0 !important;
        }
        
        /* Activity Timeline Card */
        .activity-card {
            border-radius: 12px;
            padding: 1rem 1.25rem;
            margin-bottom: 0.75rem;
            border-left: 4px solid var(--accent-primary);
            background-color: var(--bg-card);
            box-shadow: var(--card-shadow);
        }
    </style>
    """
    
    if mode == "light":
        theme_css = """
        <style>
            /* Light Theme Tokens */
            :root {
                --bg-primary: #F8FAFC;
                --bg-secondary: #FFFFFF;
                --bg-card: #FFFFFF;
                --bg-sidebar: #F1F5F9;
                --bg-hero-start: #E0F2FE;
                --bg-hero-end: #F0F9FF;
                --text-primary: #0F172A;
                --text-secondary: #334155;
                --text-muted: #64748B;
                --accent-primary: #0284C7;
                --accent-hover: #0369A1;
                --border-color: #E2E8F0;
                --card-shadow: 0 4px 12px -2px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
                --hover-shadow: 0 12px 20px -3px rgba(2, 132, 199, 0.12), 0 4px 6px -2px rgba(0, 0, 0, 0.04);
            }

            .stApp {
                background-color: var(--bg-primary) !important;
                color: var(--text-primary) !important;
            }

            [data-testid="stSidebar"] {
                background-color: var(--bg-sidebar) !important;
                border-right: 1px solid var(--border-color) !important;
            }

            /* Container & Card Styling */
            [data-testid="stVerticalBlockBorderWrapper"] > div {
                background-color: var(--bg-card) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: 14px !important;
                box-shadow: var(--card-shadow) !important;
                transition: transform 0.2s ease, box-shadow 0.2s ease !important;
            }

            [data-testid="stVerticalBlockBorderWrapper"] > div:hover {
                box-shadow: var(--hover-shadow) !important;
            }

            /* Typography */
            h1, h2, h3, h4, h5, h6, .stMarkdown, p, span, label {
                color: var(--text-primary) !important;
            }

            .stCaption, caption, small {
                color: var(--text-muted) !important;
            }

            /* Metrics */
            [data-testid="stMetric"] {
                background: #FFFFFF !important;
                border: 1px solid var(--border-color) !important;
                padding: 0.85rem 1rem !important;
                border-radius: 12px !important;
            }
            
            [data-testid="stMetricValue"] {
                color: var(--accent-primary) !important;
                font-weight: 800 !important;
            }

            [data-testid="stMetricLabel"] {
                color: var(--text-secondary) !important;
                font-weight: 600 !important;
            }

            /* Buttons */
            .stButton > button {
                border-radius: 10px !important;
                font-weight: 600 !important;
                transition: all 0.2s ease !important;
            }

            .stButton > button[kind="primary"] {
                background: linear-gradient(135deg, #0284C7 0%, #0369A1 100%) !important;
                color: #FFFFFF !important;
                border: none !important;
                box-shadow: 0 4px 12px rgba(2, 132, 199, 0.25) !important;
            }

            .stButton > button[kind="secondary"] {
                background-color: #FFFFFF !important;
                color: #0F172A !important;
                border: 1px solid #CBD5E1 !important;
            }

            .stButton > button:hover {
                transform: translateY(-1px) !important;
            }

            /* Inputs & Widgets */
            .stTextInput input, .stNumberInput input, .stSelectbox select, .stTextArea textarea {
                background-color: #FFFFFF !important;
                color: #0F172A !important;
                border: 1px solid #CBD5E1 !important;
                border-radius: 10px !important;
            }

            /* Dataframes & Tables */
            [data-testid="stDataFrame"] {
                background-color: #FFFFFF !important;
                border-radius: 12px !important;
                border: 1px solid #E2E8F0 !important;
            }
        </style>
        """
    else:
        theme_css = """
        <style>
            /* Dark Theme Tokens */
            :root {
                --bg-primary: #090D16;
                --bg-secondary: #111827;
                --bg-card: #131B2E;
                --bg-sidebar: #070C16;
                --bg-hero-start: #0F172A;
                --bg-hero-end: #1E293B;
                --text-primary: #F8FAFC;
                --text-secondary: #E2E8F0;
                --text-muted: #94A3B8;
                --accent-primary: #38BDF8;
                --accent-hover: #0EA5E9;
                --border-color: #1E293B;
                --card-shadow: 0 4px 14px -2px rgba(0, 0, 0, 0.4);
                --hover-shadow: 0 12px 24px -4px rgba(56, 189, 248, 0.15), 0 4px 8px -2px rgba(0, 0, 0, 0.4);
            }

            .stApp {
                background-color: var(--bg-primary) !important;
                color: var(--text-primary) !important;
            }

            [data-testid="stSidebar"] {
                background-color: var(--bg-sidebar) !important;
                border-right: 1px solid var(--border-color) !important;
            }

            /* Container & Card Styling */
            [data-testid="stVerticalBlockBorderWrapper"] > div {
                background-color: var(--bg-card) !important;
                border: 1px solid var(--border-color) !important;
                border-radius: 14px !important;
                box-shadow: var(--card-shadow) !important;
                transition: transform 0.2s ease, box-shadow 0.2s ease !important;
            }

            [data-testid="stVerticalBlockBorderWrapper"] > div:hover {
                box-shadow: var(--hover-shadow) !important;
            }

            /* Typography */
            h1, h2, h3, h4, h5, h6, .stMarkdown, p, span, label {
                color: var(--text-primary) !important;
            }

            .stCaption, caption, small {
                color: var(--text-muted) !important;
            }

            /* Metrics */
            [data-testid="stMetric"] {
                background: #111827 !important;
                border: 1px solid var(--border-color) !important;
                padding: 0.85rem 1rem !important;
                border-radius: 12px !important;
            }

            [data-testid="stMetricValue"] {
                color: var(--accent-primary) !important;
                font-weight: 800 !important;
            }

            [data-testid="stMetricLabel"] {
                color: var(--text-secondary) !important;
                font-weight: 600 !important;
            }

            /* Buttons */
            .stButton > button {
                border-radius: 10px !important;
                font-weight: 600 !important;
                transition: all 0.2s ease !important;
            }

            .stButton > button[kind="primary"] {
                background: linear-gradient(135deg, #0EA5E9 0%, #0284C7 100%) !important;
                color: #FFFFFF !important;
                border: none !important;
                box-shadow: 0 4px 14px rgba(14, 165, 233, 0.3) !important;
            }

            .stButton > button[kind="secondary"] {
                background-color: #1E293B !important;
                color: #F8FAFC !important;
                border: 1px solid #334155 !important;
            }

            .stButton > button:hover {
                transform: translateY(-1px) !important;
            }

            /* Inputs & Widgets */
            .stTextInput input, .stNumberInput input, .stSelectbox select, .stTextArea textarea {
                background-color: #1E293B !important;
                color: #F8FAFC !important;
                border: 1px solid #334155 !important;
                border-radius: 10px !important;
            }

            /* Dataframes & Tables */
            [data-testid="stDataFrame"] {
                background-color: #131B2E !important;
                border-radius: 12px !important;
                border: 1px solid #1E293B !important;
            }
        </style>
        """
        
    st.markdown(base_css + theme_css, unsafe_allow_html=True)


def apply_plotly_theme(fig):
    """Apply active Light/Dark theme configuration to any Plotly chart."""
    mode = get_current_theme()
    
    if mode == "light":
        paper_bg = "rgba(255,255,255,0)"
        plot_bg = "rgba(255,255,255,0)"
        font_color = "#0F172A"
        grid_color = "#E2E8F0"
        zeroline_color = "#CBD5E1"
    else:
        paper_bg = "rgba(0,0,0,0)"
        plot_bg = "rgba(0,0,0,0)"
        font_color = "#F8FAFC"
        grid_color = "rgba(255,255,255,0.08)"
        zeroline_color = "rgba(255,255,255,0.15)"
        
    fig.update_layout(
        paper_bgcolor=paper_bg,
        plot_bgcolor=plot_bg,
        font=dict(color=font_color, family="Inter, sans-serif", size=12),
        margin=dict(t=40, b=25, l=15, r=15),
        hoverlabel=dict(font_color=font_color),
    )
    fig.update_xaxes(showgrid=True, gridcolor=grid_color, zerolinecolor=zeroline_color)
    fig.update_yaxes(showgrid=True, gridcolor=grid_color, zerolinecolor=zeroline_color)
    return fig
