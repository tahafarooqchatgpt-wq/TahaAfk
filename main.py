import streamlit as st
import time

# --- PAGE CONFIGURATION ---
# This sets the browser tab title and icon
st.set_page_config(
    page_title="AlwaysOnline Bot Control",
    page_icon="🤖",
    layout="wide"
)

# --- CUSTOM STYLING (CSS) ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { 
        background-color: #1e2130; 
        padding: 15px; 
        border-radius: 10px; 
        border: 1px solid #3e4251; 
    }
    .stButton>button { 
        width: 100%; 
        border-radius: 8px; 
        font-weight: bold; 
        height: 3em;
    }
    .status-box {
        padding: 10px;
        border-radius: 5px;
        text-align: center;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_True=True)

# --- APP HEADER ---
st.title("🤖 AlwaysOnline Control Panel")
st.markdown(f"""
**Developer:** `MTFGMAERZ75` | **Bot System:** `AlwaysOnline v1.0`
""")
st.divider()

# --- SIDEBAR: CONFIGURATION ---
with st.sidebar:
    st.header("⚙️ Connection Settings")
    
    # IP Selection Logic
    ip_mode = st.radio("Server Connection Mode", ["Standard/Proxy", "Aternos Dynamic IP"])
    
    if ip_mode == "Standard/Proxy":
        server_ip = st.text_input("Server IP", value="PrivateCrystalSmpS2.aternos.me")
    else:
        server_ip = st.text_input("Dynamic IP", value="kahawai.aternos.host")
        
    server_port = st.number_input("Port", value=47365)
    
    st.divider()
    
    st.header("🤖 Bot Identity")
    bot_name = st.text_input("Bot Username", value="AlwaysOnline")
    mc_version = st.selectbox("Minecraft Version", ["1.20.1", "1.19.4", "1.18.2", "1.16.5"])

# --- MAIN DASHBOARD AREA ---
# Top Row Metrics
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Target Host", value=server_ip)
with col2:
    st.metric(label="Network Port", value=server_port)
with col3:
    st.metric(label="Creator", value="MTFGMAERZ75")

st.info(f"🔗 **Current Connection String:** `{server_ip}:{server_port}`")

# --- ACTION CENTER ---
st.subheader("🎮 Live Bot Controls")

# Initialize session state for the bot status if it doesn't exist
if 'bot_active' not in st.session_state:
    st.session_state.bot_active = False

btn_col1, btn_col2, btn_col3 = st.columns(3)

with btn_col1:
    if st.button("🚀 Start AlwaysOnline", type="primary"):
        with st.spinner("Connecting to Minecraft Server..."):
            time.sleep(1.5) # Simulating connection delay
            st.session_state.bot_active = True
            st.success(f"{bot_name} is now ONLINE.")

with btn_col2:
    if st.button("🛑 Stop Bot"):
        st.session_state.bot_active = False
        st.error("Bot connection terminated.")

with btn_col3:
    if st.button("🔄 Clear Skiprt Cooldown"):
        if st.session_state.bot_active:
            st.toast("Command Sent: /skiprt cooldown clear AlwaysOnline")
            st.write("✅ **Console:** Cooldowns cleared for current session.")
        else:
            st.warning("Bot must be online to clear cooldowns.")

# --- LIVE STATUS & LOGS ---
st.divider()
st.subheader("📜 System Terminal")

current_status = "🟢 ONLINE" if st.session_state.bot_active else "🔴 OFFLINE"

log_data = f"""
[SYSTEM] Initializing Dashboard...
[USER] MTFGMAERZ75 Authenticated.
[NET] IP set to {server_ip}
[NET] Port set to {server_port}
[STATUS] Bot is currently {current_status}
"""

if st.session_state.bot_active:
    log_data += f"[GAME] {bot_name} joined the server.\n[GAME] Ready for Skiprt commands."

st.code(log_data, language="bash")

# Footer
st.markdown("---")
st.caption(f"AlwaysOnline Bot Panel | Developed for PrivateCrystalSmpS2 by MTFGMAERZ75")
