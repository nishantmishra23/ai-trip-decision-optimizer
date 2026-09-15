"""
Streamlit theme utilities for AI Trip Decision Optimizer.
Plotly chart theming uses native st.context.theme for light/dark awareness.
CSS injection has been replaced by .streamlit/config.toml native theming.
"""
import streamlit as st


def apply_plotly_theme(fig):
    """Apply active Light/Dark theme configuration to any Plotly chart."""
    try:
        is_dark = st.context.theme.type == "dark"
    except Exception:
        is_dark = True

    if is_dark:
        paper_bg = "rgba(0,0,0,0)"
        plot_bg = "rgba(0,0,0,0)"
        font_color = "#F1F5F9"
        grid_color = "rgba(255,255,255,0.07)"
        zeroline_color = "rgba(255,255,255,0.12)"
        categorical_colors = ["#818CF8", "#38BDF8", "#34D399", "#FBBF24", "#F87171", "#A78BFA", "#94A3B8"]
    else:
        paper_bg = "rgba(0,0,0,0)"
        plot_bg = "rgba(0,0,0,0)"
        font_color = "#111827"
        grid_color = "#E5E7EB"
        zeroline_color = "#D1D5DB"
        categorical_colors = ["#4F46E5", "#0EA5E9", "#10B981", "#F59E0B", "#EF4444", "#8B5CF6", "#64748B"]

    fig.update_layout(
        paper_bgcolor=paper_bg,
        plot_bgcolor=plot_bg,
        font=dict(color=font_color, family="Inter, sans-serif", size=12),
        margin=dict(t=40, b=25, l=15, r=15),
        hoverlabel=dict(font_color=font_color),
        colorway=categorical_colors,
    )
    fig.update_xaxes(showgrid=True, gridcolor=grid_color, zerolinecolor=zeroline_color, linecolor=grid_color)
    fig.update_yaxes(showgrid=True, gridcolor=grid_color, zerolinecolor=zeroline_color, linecolor=grid_color)
    return fig
