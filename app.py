import streamlit as st

# Set up the webpage title and layout
st.set_page_config(page_title="Merit Calculator", page_icon="🎓")

# 1. Header Section
st.title("🎓 University Merit Calculator")
st.write("Welcome! Let's calculate your official university aggregate.")
st.markdown("---")

# 2. University Selection (Added ITU and PUCIT)
uni_choice = st.selectbox(
    "Which University are you targeting?",
    ("FAST", "COMSATS", "NUST", "UET", "ITU", "PUCIT")
)

# 3. Academic Marks (Hardcoded for ICS Students for better UI)
st.subheader("📚 Academic Details")
col1, col2 = st.columns(2)

# Hardcoded constants
M_total = 1200.0
F_total = 560.0

with col1:
    M_mar = st.number_input("Matric Obtained Marks (out of 1200)", min_value=0.0, max_value=M_total, step=1.0)

with col2:
    F_mar = st.number_input("FSc/ICS Part-1 Obtained Marks (out of 560)", min_value=0.0, max_value=F_total, step=1.0)

# Calculate standard percentages 
M_Per = (M_mar / M_total) * 100 if M_total > 0 else 0
F_Per = (F_mar / F_total) * 100 if F_total > 0 else 0

# 4. Entry Test Details
st.subheader("📝 Entry Test Details")
Merit = 0.0

if uni_choice == "FAST":
    test_type = st.radio("Which test did you take?", ("FAST NU Test", "NTS NAT"))
    E_t = st.number_input("Enter Test Marks (out of 100)", min_value=0.0, max_value=100.0, step=1.0)
    E_Per = E_t # Already out of 100
    
    if test_type == "FAST NU Test":
        # FAST NU Test Formula
        Merit = (F_Per * 0.50) + (E_Per * 0.50)
    else:
        # FAST NTS NAT Formula
        Merit = (M_Per * 0.10) + (F_Per * 0.40) + (E_Per * 0.50)

elif uni_choice == "COMSATS":
    E_t = st.number_input("Enter NTS NAT Marks (out of 100)", min_value=0.0, max_value=100.0, step=1.0)
    # COMSATS Formula
    Merit = (M_Per * 0.10) + (F_Per * 0.40) + (E_t * 0.50)

elif uni_choice == "NUST":
    E_t = st.number_input("Enter NET Marks (out of 200)", min_value=0.0, max_value=200.0, step=1.0)
    E_Per = (E_t / 200) * 100
    # NUST Formula
    Merit = (M_Per * 0.10) + (F_Per * 0.15) + (E_Per * 0.75)

elif uni_choice == "UET":
    E_t = st.number_input("Enter ECAT Marks (out of 400)", min_value=0.0, max_value=400.0, step=1.0)
    E_Per = (E_t / 400) * 100
    # UET Formula 
    Merit = (M_Per * 0.25) + (F_Per * 0.45) + (E_Per * 0.30)

elif uni_choice == "ITU":
    E_t = st.number_input("Enter ITU Test / NTS NAT Marks (out of 100)", min_value=0.0, max_value=100.0, step=1.0)
    # ITU Formula (Same as COMSATS: 50% Test, 40% Inter, 10% Matric)
    Merit = (M_Per * 0.10) + (F_Per * 0.40) + (E_t * 0.50)

elif uni_choice == "PUCIT":
    E_t = st.number_input("Enter PU Admission Test Marks (out of 100)", min_value=0.0, max_value=100.0, step=1.0)
    # PUCIT Formula (25% Entry Test + 75% Academic [1/4th Matric + Inter])
    academic_obtained = (M_mar / 4) + F_mar
    academic_total = (M_total / 4) + F_total
    academic_merit = (academic_obtained / academic_total) * 75
    test_merit = (E_t / 100) * 25
    Merit = academic_merit + test_merit

# 5. The Output Section
st.markdown("---")
if st.button("Calculate My Merit 🚀", type="primary"):
    
    # Show a big green success box with the result
    st.success(f"### ✅ Your Official {uni_choice} Merit is: {round(Merit, 2)}%")
    
    # 6. Suggestion Engine inside an expander
    with st.expander("See Admission Chances & Suggestions"):
        if Merit >= 85:
            st.info("Excellent! You have a highly secure chance for CS/SE at top campuses.")
        elif Merit >= 78:
            st.info("Great score! You have a solid chance at COMSATS, ITU, PUCIT, and regional campuses.")
        elif Merit >= 70:
            st.info("Good score. You can comfortably secure IT/Engineering seats at UET or general BS programs.")
        elif Merit >= 60:
            st.info("You meet the baseline criteria to apply for general BS programs.")
        else:
            st.warning("Your aggregate is a bit low for top-tier CS programs. Keep pushing!")

# 7. The Developer Signature 
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: grey;'>"
    "Thank you for using my services 💞🩵<br>"
    "<b>Regards, M. Hamza</b>"
    "</div>", 
    unsafe_allow_html=True
)
