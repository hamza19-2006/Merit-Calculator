import streamlit as st

# Set up the webpage title and layout
st.set_page_config(page_title="Merit Calculator", page_icon="🎓")

# 1. Header Section
st.title("🎓 University Merit Calculator")
st.write("Welcome! Let's calculate your official university aggregate.")
st.markdown("---")

# 2. University Selection (Dropdown menu instead of typing 1-4)
uni_choice = st.selectbox(
    "Which University are you targeting?",
    ("FAST", "COMSATS", "NUST", "UET")
)

# 3. Academic Marks (Using columns to make it look clean)
st.subheader("📚 Academic Details")
col1, col2 = st.columns(2)

with col1:
    M_mar = st.number_input("Matric Obtained Marks", min_value=0.0, step=1.0)
    M_total = st.number_input("Matric Total Marks", min_value=1.0, value=1100.0, step=1.0)

with col2:
    F_mar = st.number_input("FSc/ICS Part-1 Obtained Marks", min_value=0.0, step=1.0)
    F_total = st.number_input("FSc/ICS Part-1 Total Marks", min_value=1.0, value=510.0, step=1.0)

# Calculate percentages safely
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
        Merit = (F_Per * 0.50) + (E_Per * 0.50)
    else:
        Merit = (M_Per * 0.10) + (F_Per * 0.40) + (E_Per * 0.50)

elif uni_choice == "COMSATS":
    E_t = st.number_input("Enter NTS NAT Marks (out of 100)", min_value=0.0, max_value=100.0, step=1.0)
    Merit = (M_Per * 0.10) + (F_Per * 0.40) + (E_t * 0.50)

elif uni_choice == "NUST":
    E_t = st.number_input("Enter NET Marks (out of 200)", min_value=0.0, max_value=200.0, step=1.0)
    E_Per = (E_t / 200) * 100
    Merit = (M_Per * 0.10) + (F_Per * 0.15) + (E_Per * 0.75)

elif uni_choice == "UET":
    E_t = st.number_input("Enter ECAT Marks (out of 400)", min_value=0.0, max_value=400.0, step=1.0)
    E_Per = (E_t / 400) * 100
    Merit = (M_Per * 0.25) + (F_Per * 0.45) + (E_Per * 0.30)

# 5. The Output Section
st.markdown("---")
if st.button("Calculate My Merit 🚀", type="primary"):
    
    # Show a big green success box with the result
    st.success(f"### ✅ Your Official {uni_choice} Merit is: {round(Merit, 2)}%")
    
    # 6. Suggestion Engine inside an expander (dropdown)
    with st.expander("See Admission Chances & Suggestions"):
        if Merit >= 85:
            st.info("Excellent! You have a highly secure chance for CS/SE at top campuses.")
        elif Merit >= 78:
            st.info("Great score! You have a solid chance at COMSATS, UET, and regional campuses.")
        elif Merit >= 70:
            st.info("Good score. You can comfortably secure IT/Engineering seats at UET.")
        elif Merit >= 60:
            st.info("You meet the baseline criteria to apply for general BS programs.")
        else:
            st.warning("Your aggregate is a bit low for top-tier CS programs. Keep pushing!")
    # 6. The Developer Signature (Replaces the exit loop)
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: grey;'>"
        "Thank you for using my services 💞🩵<br>"
        "<b>Regards, M. Hamza</b>"
        "</div>", 
        unsafe_allow_html=True
    )        