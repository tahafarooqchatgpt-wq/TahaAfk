import streamlit as st
import time
from datetime import datetime, timedelta

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="AlwaysOnline Bot Control",
    page_icon="🤖",
    layout="wide"
)

# --- STYLING ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; border: 1px solid #3e4251; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: bold; height: 3em; }
    #timer-text { font-size: 24px; font-weight: bold; color: #00ff00; }
    </style>
    """, unsafe_allow_html=True)

# --- SESSION STATE INITIALIZATION ---
if 'active' not in st.session_state:
    st.session_state.active = False
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

# --- HEADER ---
st.title("🤖 AlwaysOnline Control Panel")
st.markdown("**Owner/Developer:** `MTFGMAERZ75` | **Status:** `Dashboard Loaded`")
st.divider()

# --- SIDEBAR CONFIG ---
with st.sidebar:
    st.header("⚙️ Server Config")
    ip_mode = st.radio("Connection Type", ["Proxy IP", "Aternos Dyn IP"])
    
    if ip_mode == "Proxy IP":
        server_ip = st.text_input("IP", value="PrivateCrystalSmpS2.aternos.me")
    else:
        server_ip = st.text_input("Dyn IP", value="kahawai.aternos.host")
        
    server_port = st.number_input("Port", value=47365)
    
    st.divider()
    bot_name = st.text_input("Bot Name", value="AlwaysOnline")
    bot_ver = st.selectbox("MC Version", ["1.20.1", "1.19.4", "1.18.2", "1.16.5"])

# --- DASHBOARD UI ---
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Target IP", server_ip)
with col2:
    st.metric("Port", server_port)
with col3:
    st.metric("User", bot_name)

# --- TIMER SECTION ---
st.subheader("⏱️ Live Session Timer")
timer_placeholder = st.empty()

def update_timer():
    if st.session_state.active and st.session_state.start_time:
        now = datetime.now()
        # Adding 1 hour (3600 seconds) to the start as requested
        elapsed = now - st.session_state.start_time + timedelta(hours=1)
        
        # Format the time as HH:MM:SS
        hours, remainder = divmod(int(elapsed.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        time_str = f"{hours:02}:{minutes:02}:{seconds:02}"
        
        timer_placeholder.markdown(f"### Online Since: `{time_str}` (1h offset active)")
    else:
        timer_placeholder.markdown("### Status: `🔴 Offline`")

# --- CONTROLS ---
st.subheader("🎮 Bot Actions")
c1, c2, c3 = st.columns(3)

with c1:
    if st.button("🚀 Start Bot", type="primary"):
        st.session_state.active = True
        st.session_state.start_time = datetime.now()
        st.success(f"{bot_name} is Online!")

with c2:
    if st.button("🛑 Stop Bot"):
        st.session_state.active = False
        st.session_state.start_time = None
        st.error("Bot Offline.")

with c3:
    if st.button("🔄 Clear Cooldown"):
        if st.session_state.active:
            st.toast("Command: /skiprt cooldown clear AlwaysOnline")
        else:
            st.warning("Start the bot first!")

# --- LOGS ---
st.subheader("📜 Console")
status = "🟢 ONLINE" if st.session_state.active else "🔴 OFFLINE"
st.code(f"""
[SYSTEM] Dashboard Loaded.
[OWNER] MTFGMAERZ75
[SERVER] {server_ip}:{server_port}
[STATUS] {status}
""", language="bash")

# --- AUTO-REFRESH LOOP ---
if st.session_state.active:
    time.sleep(1)
    update_timer()
    st.rerun()
else:
    update_timer()
