# dashboard_application/ids.py
# EOTS v2.5 - CANONICAL COMPONENT IDENTIFIERS (AUTHORITATIVE)

"""
Defines constant IDs for Dash components used throughout the EOTS dashboard application.
Centralizing IDs here prevents typos and simplifies component management across modules.
"""

# --- Core Application & State Management ---
ID_URL_LOCATION = "url-location-id"
ID_MAIN_DATA_STORE = "main-data-store-id"
ID_INTERVAL_LIVE_UPDATE = "interval-live-update-id"
ID_MANUAL_REFRESH_BUTTON = "manual-refresh-button-id"

# --- Layout Containers ---
ID_PAGE_CONTENT = "page-content-id"
ID_STATUS_ALERT_CONTAINER = "status-alert-container-id"
ID_MASTER_HEADER = "master-header-id"

# --- Control Panel (in Header) ---
ID_SYMBOL_INPUT = "symbol-input-id"
ID_REFRESH_INTERVAL_DROPDOWN = "refresh-interval-dropdown-id"

# --- Status Update Components ---
ID_STATUS_UPDATE_DISPLAY = "status-update-display"
ID_LAST_UPDATE_TIME = "last-update-time"
ID_CURRENT_SYMBOL = "current-symbol"
ID_CURRENT_DTE_RANGE = "current-dte-range"
ID_CURRENT_PRICE_RANGE = "current-price-range"
ID_CONTRACTS_COUNT = "contracts-count"
ID_STRIKES_COUNT = "strikes-count"
ID_PROCESSING_TIME = "processing-time"

# --- Main Dashboard Mode (Example Specific IDs) ---
# These are generated by main_dashboard_display.py
ID_REGIME_DISPLAY_CARD = "regime-display-card-id"
ID_VAPI_GAUGE = "vapi-gauge-id"
ID_DWFD_GAUGE = "dwfd-gauge-id"
ID_TW_LAF_GAUGE = "tw-laf-gauge-id"
ID_RECOMMENDATIONS_TABLE = "recommendations-table-id"
ID_MAIN_DASHBOARD_CONTAINER = "main-dashboard-container-id"
ID_GIB_GAUGE = "gib-gauge-id"
ID_HP_EOD_GAUGE = "hp-eod-gauge-id"
ID_SGDHP_HEATMAP = "sgdhp-heatmap-id"
ID_UGCH_HEATMAP = "ugch-heatmap-id"

# --- Elite Metrics Display IDs (New) ---
ID_ELITE_IMPACT_SCORE_DISPLAY = "elite-impact-score-display"
ID_INSTITUTIONAL_FLOW_SCORE_DISPLAY = "institutional-flow-score-display"
ID_FLOW_MOMENTUM_INDEX_DISPLAY = "flow-momentum-index-display"
ID_ELITE_MARKET_REGIME_DISPLAY = "elite-market-regime-display"
ID_ELITE_FLOW_TYPE_DISPLAY = "elite-flow-type-display"
ID_ELITE_VOLATILITY_REGIME_DISPLAY = "elite-volatility-regime-display"

# --- Chart Factory Constants ---
ALL_CHART_IDS_FOR_FACTORY = [
    "chart-1", "chart-2", "chart-3", "chart-4",
    "chart-5", "chart-6", "chart-7", "chart-8"
]

# --- Configuration Constants ---
CFG_TRADIER_IV_APPROX_TARGET_DTE_DEFAULT = 30
