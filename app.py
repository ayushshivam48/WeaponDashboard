import streamlit as st
import pandas as pd
import os

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="ARMORY DB // TACTICAL",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 2. DATA LOADING LOGIC ---
@st.cache_data
def load_data():
    csv_file = "weapons_500.csv"
    
    # 1. Try to load the external CSV (500 items)
    if os.path.exists(csv_file):
        try:
            df = pd.read_csv(csv_file)
            return df
        except Exception as e:
            st.error(f"Error loading CSV: {e}")
            return get_fallback_data()
    
    # 2. If no CSV found, load the hardcoded fallback (23 items)
    else:
        return get_fallback_data()

def get_fallback_data():
    data = [
        {"Name": "AK-47", "Type": "Assault Rifle", "Caliber": "7.62×39mm", "Weight": "3.47kg", "Range": "350m", "Velocity": "715m/s", "ROF": "600 rpm", "Origin": "Soviet Union", "Year": "1949", "Manufacturer": "Izhmash/Kalashnikov Concern", "Mechanism": "Gas-operated, rotating bolt", "Feed System": "30-round detachable box magazine"},
        {"Name": "M16A4", "Type": "Assault Rifle", "Caliber": "5.56×45mm NATO", "Weight": "3.77kg", "Range": "550m", "Velocity": "948m/s", "ROF": "700-950 rpm", "Origin": "USA", "Year": "1997", "Manufacturer": "Colt", "Mechanism": "Gas-operated, rotating bolt", "Feed System": "30-round detachable box magazine"},
        {"Name": "M4 Carbine", "Type": "Carbine", "Caliber": "5.56×45mm NATO", "Weight": "2.88kg", "Range": "500m", "Velocity": "940m/s", "ROF": "700-950 rpm", "Origin": "USA", "Year": "1994", "Manufacturer": "Colt", "Mechanism": "Gas-operated, rotating bolt", "Feed System": "30-round detachable box magazine"},
        {"Name": "FN SCAR-L", "Type": "Assault Rifle", "Caliber": "5.56×45mm NATO", "Weight": "3.60kg", "Range": "600m", "Velocity": "900m/s", "ROF": "600-650 rpm", "Origin": "Belgium", "Year": "2009", "Manufacturer": "FN Herstal", "Mechanism": "Gas-operated, rotating bolt", "Feed System": "30-round detachable box magazine"},
        {"Name": "HK416", "Type": "Assault Rifle", "Caliber": "5.56×45mm NATO", "Weight": "3.80kg", "Range": "600m", "Velocity": "905m/s", "ROF": "700-900 rpm", "Origin": "Germany", "Year": "2005", "Manufacturer": "Heckler & Koch", "Mechanism": "Gas-operated short-stroke piston", "Feed System": "30-round detachable box magazine"},
        {"Name": "Steyr AUG", "Type": "Assault Rifle", "Caliber": "5.56×45mm NATO", "Weight": "3.60kg", "Range": "500m", "Velocity": "970m/s", "ROF": "650-700 rpm", "Origin": "Austria", "Year": "1977", "Manufacturer": "Steyr Mannlicher", "Mechanism": "Short-stroke gas piston", "Feed System": "30/42-round detachable box magazine"},
        {"Name": "IWI Tavor", "Type": "Assault Rifle", "Caliber": "5.56×45mm NATO", "Weight": "3.46kg", "Range": "500m", "Velocity": "900m/s", "ROF": "700-950 rpm", "Origin": "Israel", "Year": "2001", "Manufacturer": "IWI", "Mechanism": "Long-stroke gas piston", "Feed System": "30-round detachable box magazine"},
        {"Name": "FAMAS", "Type": "Assault Rifle", "Caliber": "5.56×45mm NATO", "Weight": "3.61kg", "Range": "400m", "Velocity": "960m/s", "ROF": "900-1100 rpm", "Origin": "France", "Year": "1978", "Manufacturer": "GIAT", "Mechanism": "Flechette-type lever-delayed blowback", "Feed System": "25/30-round detachable box magazine"},
        {"Name": "SIG MCX", "Type": "Assault Rifle", "Caliber": "5.56×45mm NATO", "Weight": "3.30kg", "Range": "600m", "Velocity": "910m/s", "ROF": "600-700 rpm", "Origin": "USA", "Year": "2015", "Manufacturer": "SIG Sauer", "Mechanism": "Short-stroke gas piston", "Feed System": "30-round detachable box magazine"},
        {"Name": "Beretta ARX160", "Type": "Assault Rifle", "Caliber": "5.56×45mm NATO", "Weight": "3.50kg", "Range": "500m", "Velocity": "930m/s", "ROF": "700-900 rpm", "Origin": "Italy", "Year": "2008", "Manufacturer": "Beretta", "Mechanism": "Short-stroke gas piston", "Feed System": "30-round detachable box magazine"},
        {"Name": "M1 Garand", "Type": "Battle Rifle", "Caliber": ".30-06 Springfield", "Weight": "4.37kg", "Range": "500m", "Velocity": "853m/s", "ROF": "40-50 rpm", "Origin": "USA", "Year": "1936", "Manufacturer": "Springfield Armory", "Mechanism": "Gas-operated, rotating bolt", "Feed System": "8-round en bloc clip"},
        {"Name": "FN FAL", "Type": "Battle Rifle", "Caliber": "7.62×51mm NATO", "Weight": "4.85kg", "Range": "600m", "Velocity": "840m/s", "ROF": "650-700 rpm", "Origin": "Belgium", "Year": "1953", "Manufacturer": "FN Herstal", "Mechanism": "Gas-operated, tilting bolt", "Feed System": "20/30-round detachable box magazine"},
        {"Name": "G3", "Type": "Battle Rifle", "Caliber": "7.62×51mm NATO", "Weight": "4.50kg", "Range": "400m", "Velocity": "800m/s", "ROF": "600 rpm", "Origin": "Germany", "Year": "1959", "Manufacturer": "Heckler & Koch", "Mechanism": "Roller-delayed blowback", "Feed System": "20/30-round detachable box magazine"},
        {"Name": "M14", "Type": "Battle Rifle", "Caliber": "7.62×51mm NATO", "Weight": "4.50kg", "Range": "500m", "Velocity": "850m/s", "ROF": "700-750 rpm", "Origin": "USA", "Year": "1959", "Manufacturer": "Springfield Armory", "Mechanism": "Gas-operated, rotating bolt", "Feed System": "20-round detachable box magazine"},
        {"Name": "M249 SAW", "Type": "Light Machine Gun", "Caliber": "5.56×45mm NATO", "Weight": "7.50kg", "Range": "800m", "Velocity": "890m/s", "ROF": "700-1000 rpm", "Origin": "USA", "Year": "1984", "Manufacturer": "FN Herstal", "Mechanism": "Gas-operated, rotating bolt", "Feed System": "Belt-fed or 30/200-round magazine"},
        {"Name": "PKM", "Type": "General Purpose MG", "Caliber": "7.62×54mmR", "Weight": "7.50kg", "Range": "1000m", "Velocity": "825m/s", "ROF": "600 rpm", "Origin": "Soviet Union", "Year": "1969", "Manufacturer": "Kalashnikov", "Mechanism": "Long-stroke gas piston", "Feed System": "100/200/250-round non-disintegrating belt"},
        {"Name": "MG42", "Type": "General Purpose MG", "Caliber": "7.62×51mm NATO", "Weight": "11.57kg", "Range": "1000m", "Velocity": "755m/s", "ROF": "1200 rpm", "Origin": "Germany", "Year": "1942", "Manufacturer": "Mauser", "Mechanism": "Short-stroke gas piston", "Feed System": "50/250-round non-disintegrating belt"},
        {"Name": "M240", "Type": "General Purpose MG", "Caliber": "7.62×51mm NATO", "Weight": "12.25kg", "Range": "1100m", "Velocity": "853m/s", "ROF": "650-950 rpm", "Origin": "USA/Belgium", "Year": "1977", "Manufacturer": "FN Herstal", "Mechanism": "Short-stroke gas piston", "Feed System": "100/200-round non-disintegrating belt"},
        {"Name": "Uzi", "Type": "Submachine Gun", "Caliber": "9×19mm", "Weight": "3.50kg", "Range": "200m", "Velocity": "500m/s", "ROF": "600 rpm", "Origin": "Israel", "Year": "1954", "Manufacturer": "IMI", "Mechanism": "Blowback", "Feed System": "25/32/40/50-round detachable box magazine"},
        {"Name": "MP5", "Type": "Submachine Gun", "Caliber": "9×19mm", "Weight": "2.95kg", "Range": "200m", "Velocity": "400m/s", "ROF": "800 rpm", "Origin": "Germany", "Year": "1966", "Manufacturer": "Heckler & Koch", "Mechanism": "Roller-delayed blowback", "Feed System": "15/30-round detachable box magazine"},
        {"Name": "M1911", "Type": "Pistol", "Caliber": ".45 ACP", "Weight": "1.10kg", "Range": "50m", "Velocity": "250m/s", "ROF": "45 rpm", "Origin": "USA", "Year": "1911", "Manufacturer": "Colt", "Mechanism": "Short recoil, locked breech", "Feed System": "7-round detachable box magazine"},
        {"Name": "Glock 17", "Type": "Pistol", "Caliber": "9×19mm", "Weight": "0.625kg", "Range": "50m", "Velocity": "375m/s", "ROF": "Semi-automatic", "Origin": "Austria", "Year": "1982", "Manufacturer": "Glock", "Mechanism": "Short recoil, locked breech", "Feed System": "17-round detachable box magazine"},
        {"Name": "Barrett M82", "Type": "Anti-materiel rifle", "Caliber": ".50 BMG", "Weight": "13.60kg", "Range": "1830m", "Velocity": "1219m/s", "ROF": "40-60 rpm", "Origin": "USA", "Year": "1982", "Manufacturer": "Barrett", "Mechanism": "Short-recoil", "Feed System": "10-round detachable box magazine"}
    ]
    return pd.DataFrame(data)

# Load the data (Prefers CSV, falls back to Hardcoded)
df = load_data()

# --- 3. CUSTOM CSS (TACTICAL THEME) ---
st.markdown("""
    <style>
        /* Main Background and Font */
        .stApp {
            background-color: #0b1120; /* Darker slate */
            color: #e2e8f0;
            font-family: 'Segoe UI', 'Roboto', sans-serif;
        }
        
        /* Typography */
        h1, h2, h3 {
            color: #ffffff !important;
            text-transform: uppercase;
            font-family: 'Courier New', monospace;
            letter-spacing: 1px;
        }
        
        /* Sidebar Styling */
        section[data-testid="stSidebar"] {
            background-color: #020617;
            border-right: 1px solid #1e293b;
        }
        
        /* Card Container */
        .weapon-card {
            background-color: #1e293b;
            border: 1px solid #334155;
            border-radius: 8px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.5);
            transition: border-color 0.3s ease;
        }
        .weapon-card:hover {
            border-color: #06b6d4; /* Cyan hover effect */
        }

        /* Header inside card */
        .card-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            border-bottom: 1px solid #334155;
            padding-bottom: 10px;
            margin-bottom: 15px;
        }
        .weapon-name {
            font-size: 1.4rem;
            font-weight: bold;
            color: #fff;
            font-family: 'Courier New', monospace;
        }
        .weapon-type-badge {
            background-color: #0f172a;
            color: #06b6d4;
            padding: 4px 8px;
            border-radius: 4px;
            font-size: 0.7rem;
            text-transform: uppercase;
            border: 1px solid #06b6d4;
            letter-spacing: 1px;
        }

        /* Metric Labels */
        .metric-label {
            font-size: 0.7rem;
            text-transform: uppercase;
            color: #94a3b8;
            margin-bottom: 2px;
            letter-spacing: 0.5px;
        }
        .metric-value {
            font-size: 1.1rem;
            font-weight: 600;
            color: #e2e8f0;
            font-family: 'Courier New', monospace;
        }
        
        /* Section Dividers */
        .section-title {
            font-size: 0.8rem;
            color: #06b6d4;
            margin-top: 15px;
            margin-bottom: 8px;
            text-transform: uppercase;
            font-weight: bold;
            display: flex;
            align-items: center;
        }
        .section-title::after {
            content: '';
            flex: 1;
            height: 1px;
            background: #334155;
            margin-left: 10px;
        }

        /* Expander Styling */
        .streamlit-expanderHeader {
            background-color: #0f172a !important;
            border: 1px solid #334155 !important;
            color: #94a3b8 !important;
            font-family: 'Courier New', monospace;
        }
    </style>
""", unsafe_allow_html=True)

# --- 4. SIDEBAR & SEARCH LOGIC ---
st.sidebar.title("⚙️ OPS CONTROL")
st.sidebar.markdown("---")

# --- FILTER 1: CLASS (Type) ---
all_types = ["All Classes"] + sorted(list(df['Type'].unique()))
selected_type = st.sidebar.selectbox("1. CLASS", all_types)

# Filter Logic for Level 1
if selected_type != "All Classes":
    df_filtered_1 = df[df['Type'] == selected_type]
else:
    df_filtered_1 = df

# --- FILTER 2: ORIGIN (Categorical) ---
# Only show Origins available in the currently filtered list
available_origins = sorted(list(df_filtered_1['Origin'].unique()))
selected_origins = st.sidebar.multiselect(
    "2. ORIGIN", 
    available_origins,
    placeholder="All Origins"
)

# Filter Logic for Level 2
if selected_origins:
    df_filtered_2 = df_filtered_1[df_filtered_1['Origin'].isin(selected_origins)]
else:
    df_filtered_2 = df_filtered_1

# --- FILTER 3: MANUFACTURER (Categorical) ---
# Only show Manufacturers available in the currently filtered list
available_mfg = sorted(list(df_filtered_2['Manufacturer'].unique()))
selected_mfg = st.sidebar.multiselect(
    "3. MANUFACTURER", 
    available_mfg,
    placeholder="All Manufacturers"
)

# Filter Logic for Level 3
if selected_mfg:
    df_filtered_3 = df_filtered_2[df_filtered_2['Manufacturer'].isin(selected_mfg)]
else:
    df_filtered_3 = df_filtered_2

# --- FILTER 4: MODEL NAME (Specific) ---
available_names = sorted(list(df_filtered_3['Name'].unique()))
selected_names = st.sidebar.multiselect(
    "4. MODEL ID", 
    available_names,
    placeholder="All Models"
)

# Final Dataset
if selected_names:
    final_df = df_filtered_3[df_filtered_3['Name'].isin(selected_names)]
else:
    final_df = df_filtered_3

# Sidebar Stats
st.sidebar.markdown("---")
st.sidebar.metric("DEPLOYED ASSETS", len(final_df))
st.sidebar.metric("DATABASE TOTAL", len(df))
st.sidebar.markdown("---")

# CSV Download
csv = final_df.to_csv(index=False).encode('utf-8')
st.sidebar.download_button(
    "📥 EXPORT DATA (CSV)",
    csv,
    "filtered_weapon_data.csv",
    "text/csv",
    key='download-csv'
)

# --- 5. HELPER FUNCTIONS ---
def parse_metric(val_str, max_val):
    try:
        # Extract numeric part safely
        clean_str = str(val_str).replace('kg','').replace('m/s','').replace('m','').replace(',','')
        import re
        match = re.search(r"[-+]?\d*\.\d+|\d+", clean_str)
        if match:
            num = float(match.group())
            return min(num / max_val, 1.0)
        return 0.0
    except:
        return 0.0

# --- 6. MAIN DISPLAY ---
st.title("ARMORY DB // TACTICAL")

# Active Filter Display
filter_text = []
if selected_type != "All Classes": filter_text.append(f"CLASS: {selected_type}")
if selected_origins: filter_text.append(f"ORIGIN: {', '.join(selected_origins)}")
if selected_mfg: filter_text.append(f"MFG: {', '.join(selected_mfg)}")

status_msg = " // ".join(filter_text) if filter_text else "ALL SYSTEMS NOMINAL"

st.markdown(f"""
<div style="margin-bottom: 20px; color: #64748b; font-family: 'Courier New'; font-size: 0.9rem;">
    STATUS: <span style="color: #06b6d4;">{status_msg}</span> 
    <br>
    LISTING: <span style="color: #fff;">{len(final_df)} ITEMS</span>
    { "// READING FROM LOCAL CSV" if os.path.exists("weapons_500.csv") else "// SYSTEM DEFAULT DATA" }
</div>
""", unsafe_allow_html=True)

if len(final_df) == 0:
    st.warning("NO ASSETS FOUND. ADJUST FILTERS.")
else:
    # Pagination logic for performance
    ITEMS_PER_PAGE = 50 
    if len(final_df) > ITEMS_PER_PAGE:
        st.caption(f"Displaying first {min(len(final_df), 100)} results for performance...")
        final_df = final_df.head(100)

    # Use a grid for cards
    cols = st.columns(2)
    
    for idx, row in final_df.iterrows():
        col = cols[idx % 2]
        
        with col:
            # START CARD
            st.markdown(f"""
            <div class="weapon-card">
                <div class="card-header">
                    <div class="weapon-name">{row['Name']}</div>
                    <div class="weapon-type-badge">{row['Type']}</div>
                </div>
            """, unsafe_allow_html=True)
            
            # --- SECTION 1: LOGISTICS (Origin & Build) ---
            c1, c2, c3 = st.columns(3)
            with c1:
                st.markdown(f"""<div class="metric-label">ORIGIN</div><div class="metric-value">{row['Origin']}</div>""", unsafe_allow_html=True)
            with c2:
                st.markdown(f"""<div class="metric-label">YEAR</div><div class="metric-value">{row['Year']}</div>""", unsafe_allow_html=True)
            with c3:
                st.markdown(f"""<div class="metric-label">WEIGHT</div><div class="metric-value">{row['Weight']}</div>""", unsafe_allow_html=True)
            
            # --- SECTION 2: BALLISTICS (Performance) ---
            st.markdown('<div class="section-title">BALLISTICS PERFORMANCE</div>', unsafe_allow_html=True)
            
            b1, b2 = st.columns(2)
            with b1:
                st.markdown(f"""<div class="metric-label">CALIBER</div><div class="metric-value" style="color:#06b6d4;">{str(row['Caliber']).split(' ')[0]}</div>""", unsafe_allow_html=True)
            with b2:
                rof_display = str(row['ROF']).split(' ')[0] if pd.notna(row['ROF']) else "N/A"
                st.markdown(f"""<div class="metric-label" title="Rate of Fire (Rounds Per Minute)">ROF <span style="font-size:0.6em">RPM</span></div><div class="metric-value">{rof_display}</div>""", unsafe_allow_html=True)

            # Visual Bars
            st.markdown('<div style="height:10px"></div>', unsafe_allow_html=True) # Spacer
            
            st.caption(f"EFFECTIVE RANGE ({row['Range']})")
            st.progress(parse_metric(row['Range'], 2000))
            
            st.caption(f"MUZZLE VELOCITY ({row['Velocity']})")
            st.progress(parse_metric(row['Velocity'], 1300))

            # --- SECTION 3: TECHNICAL DETAILS (Expander) ---
            with st.expander("🔽 TECHNICAL SPECIFICATIONS"):
                st.markdown(f"""
                | SPECIFICATION | DETAIL |
                | :--- | :--- |
                | **Manufacturer** | {row['Manufacturer']} |
                | **Action** | {row['Mechanism']} |
                | **Full Caliber** | {row['Caliber']} |
                | **Feed System** | {row.get('Feed System', 'Standard Magazine')} |
                """)
            
            # END CARD
            st.markdown("</div>", unsafe_allow_html=True)