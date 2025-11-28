import streamlit as st
import base64

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(page_title="Pricing Calculator", layout="wide")

# ---------------- BASE64 IMAGE UTILITY ---------------- #
def get_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

def get_base64_image(image_path):
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()
    return encoded

# ---------------- HEADER IMAGE (BANNER ATAS) ---------------- #
img_header = get_base64("GTS Google form.png")  # pastikan file ada di folder yang sama

st.markdown(
    f"""
    <div style="display:flex; justify-content:center; margin-bottom:25px;">
        <img src="data:image/png;base64,{img_header}"
        style="width:100%; max-width:2500px; border-radius:22px; box-shadow:0px 5px 16px rgba(0,0,0,0.18);" />
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- CUSTOM CSS THEME (SENADA HEADER) ---------------- #
st.markdown(
    """
    <style>

    /* Background gradient senada header (teal + mint) */
    .stApp {
        background: linear-gradient(to bottom right, #00C9A7, #028090, #006D77);
    }

    /* Hapus overlay bawaan saat input */
    input, div[data-baseweb="input"] {
        background-color: white !important;
        transition: none !important;
        animation: none !important;
    }

    /* Title besar & jelas */
    .big-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        color: white;
        margin-bottom: 20px;
        text-shadow: 0px 2px 6px rgba(0,0,0,0.22);
    }

    /* Box hasil keputusan (biar kebaca) */
    .decision-box {
        text-align: center;
        font-size: 30px;
        font-weight: 800;
        color: white;
        padding: 14px;
        border-radius: 14px;
        margin-top: 18px;
        background: rgba(0,0,0,0.32);
        text-shadow: 0px 2px 4px rgba(0,0,0,0.2);
        border-left: 5px solid #FFFFFF;
    }

    /* Styling button + hover tanpa delay */
    .stButton button {
        background-color: white;
        color: #006D77;
        font-weight: 800;
        font-size: 18px;
        border-radius: 14px;
        padding: 12px 32px;
        border: 2px solid #006D77;
        transition: 0.2s ease;
    }

    .stButton button:hover {
        background-color: #006D77;
        color: white;
        border: 2px solid white;
    }
    
    /* Mengubah label st.number_input jadi putih */
    div[data-testid="stNumberInput"] label {
        color: white !important;
        font-size: 20px !important;
        font-weight: 800 !important;
    }

    /* Tulisan placeholder/caption di number input juga putih */
    div[data-testid="stNumberInput"] div[data-baseweb="input"] input::placeholder {
        color: #FFFFFF99 !important; /* putih agak transparan biar elegan */
    }

    /* Pastikan background input tetap putih */
    

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------- TITLE SECTION ---------------- #
st.markdown('<div class="big-title">Pricing Calculator</div>', unsafe_allow_html=True)

# ---------------- INPUT SECTION ---------------- #
col1, col2 = st.columns(2)

with col1:
    siswa = st.number_input("Jumlah Siswa", value=0, step=1)
    rombel = st.number_input("Jumlah Rombongan Belajar", value=0, step=1)
    sesi = st.number_input("Jumlah Sesi", value=0, step=1)
    tryout = st.number_input("Jumlah Tryout Premium", value=0, step=1)

with col2:
    tmb = st.number_input("Jumlah Tes Minat Bakat Premium", value=0, step=1)
    rubel = st.number_input("Jumlah Ruangbelajar", value=0, step=1)
    kitab = st.number_input("Jumlah Kitab", value=0, step=1)
    base_price = st.number_input("Proposal Harga per Siswa", value=0, step=1)

# ---------------- PERHITUNGAN ---------------- #
total_deal = siswa * base_price

# Cost Reguler
total_fee_guru = (sesi * rombel) * 150000
modul_bahan_ajar = siswa * 10000
operational_cost = siswa * 17500 
supplement_cost = (sesi * rombel) * 15000

# Non RGP Cost
to_prem = (siswa * tryout) * 15000
tmb_cost = (tmb * siswa) * 35000 
kitab_cost = kitab * 250000
rubel_cost = rubel * 400000
after_sales = siswa * 15000

# Total Cost
total_cost = (((total_fee_guru + modul_bahan_ajar + operational_cost + supplement_cost) * 1.4) +
              (to_prem + tmb_cost + kitab_cost + rubel_cost + after_sales))

gross_margin = total_deal - total_cost
margin_percentage = (gross_margin / total_deal) * 100 if total_deal > 0 else 0

# Agent Incentive Logic
if total_deal >= 0 and total_deal <= 50000000:
    agent_insentive_unit = 0.02
    bonus = 0
    synergy_percentage = 0.02
elif total_deal > 50000000 and total_deal <= 100000000:
    agent_insentive_unit = 0.02
    bonus = 500000
    synergy_percentage = 0.03
elif total_deal > 100000000 and total_deal <= 150000000:
    agent_insentive_unit = 0.02
    bonus = 1000000
    synergy_percentage = 0.04
elif total_deal > 150000000 and total_deal <= 200000000:
    agent_insentive_unit = 0.02
    bonus = 1500000
    synergy_percentage = 0.04
elif total_deal > 200000000 and total_deal <= 250000000:
    agent_insentive_unit = 0.02
    bonus = 2000000
    synergy_percentage = 0.45
elif total_deal > 250000000 and total_deal <= 300000000:
    agent_insentive_unit = 0.02
    bonus = 2500000
    synergy_percentage = 0.45
elif total_deal > 300000000 and total_deal <= 1000000000:
    agent_insentive_unit = 0.02
    bonus = 3000000
    synergy_percentage = 0.05
else:
    agent_insentive_unit = 0.0
    bonus = 0
    synergy_percentage = 0

agent_insentive = agent_insentive_unit * total_deal
synergy = synergy_percentage * total_deal
cogs = total_fee_guru + modul_bahan_ajar + operational_cost + supplement_cost + to_prem + tmb_cost + kitab_cost + rubel_cost + after_sales
real_margin = total_deal - cogs - agent_insentive - bonus - synergy
real_margin_percentage = (real_margin / total_deal) * 100 if total_deal > 0 else 0

# ---------------- CALCULATE BUTTON ONLY OVERLAY ---------------- #
if st.button("Calculate Price"):

    overlay_css = """
    <style>
    .stButton button:active {
        background-color: #00C9A7 !important;
        filter: brightness(0.8);
    }
    </style>
    """
    st.markdown(overlay_css, unsafe_allow_html=True)

    # Decision
    if 55 < real_margin_percentage < 60:
        decision = "The margin is negotiable, review suggested⚠️"
    elif real_margin_percentage >= 60:
        decision = "Your request has been accepted✅"
    else:
        decision = "Your request has been rejected❌"

    # Show Result Card
    st.markdown(
        f'<div class="decision-box">{decision}</div>',
        unsafe_allow_html=True
    )

    # Detail calculation output
    st.markdown(
        f"""
        <div style="background:rgba(0,0,0,0.28); border-radius:14px; padding:22px; margin-top:22px; color:white;">
            <h3 style="color:white;">📊 Hasil Perhitungan</h3>
            <p><b>Jumlah Siswa:</b> {siswa}</p>
            <p><b>Jumlah Rombongan Belajar:</b> {rombel}</p>
            <p><b>Jumlah Sesi:</b> {sesi}</p>
            <p><b>Jumlah Tryout Premium:</b> {tryout}</p>
            <p><b>Jumlah Tes Minat Bakat Premium:</b> {tmb}</p>
            <p><b>Jumlah Ruangbelajar:</b> {rubel}</p>
            <p><b>Jumlah Kitab:</b> {kitab}</p>
            <p><b>Proposal Harga per Siswa:</b> {base_price}</p>
        </div>
        """,
        unsafe_allow_html=True
    )
