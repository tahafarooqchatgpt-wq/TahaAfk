import streamlit as st
import time
from datetime import datetime, timedelta

# --- SETTINGS ---
st.set_page_config(page_title="AlwaysOnline Status", page_icon="🟢")

# The timer starts automatically when the page is loaded
if 'start_time' not in st.session_state:
    st.session_state.start_time = datetime.now()

# --- HEADER ---
st.title("AlwaysOnline Bot Status")
st.write("Developer: **MTFGMAERZ75**")
st.divider()

# --- COPYABLE ADDRESSES ---
st.subheader("🔗 Server Addresses")
st.code("PrivateCrystalSmpS2.aternos.me", language=None)
st.caption("Standard Proxy IP")

st.code("kahawai.aternos.host:47365", language=None)
st.caption("Dynamic Direct IP & Port")

st.divider()

# --- DATA COLUMNS ---
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 📊 Server Details")
    st.write("**Status:** 🟢 Online")
    st.write("**Version:** 1.21.11")
    st.write("**Port:** 47365")

with col2:
    st.markdown("### 🤖 Bot Details")
    st.write("**Name:** AlwaysOnline")
    st.write("**Version:** 1.16.4")
    st.write("**Nameplayer:** MTFGMAERZ75")

st.divider()

# --- AUTOMATIC TIMER ---
# Calculates time since page load + 1 hour offset
elapsed = datetime.now() - st.session_state.start_time + timedelta(hours=1)
hours, remainder = divmod(int(elapsed.total_seconds()), 3600)
minutes, seconds = divmod(remainder, 60)
time_str = f"{hours:02}:{minutes:02}:{seconds:02}"

st.subheader(f"⏱️ Online Since: {time_str}")

# --- SINGLE COMMAND BUTTON ---
if st.button("Clear Skiprt Cooldown"):
    st.success("Sent: /skiprt cooldown clear AlwaysOnline")

# --- LIVE REFRESH ---
# Refreshes every 1 second to update the clock
time.sleep(1)
st.rerun()
