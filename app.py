import streamlit as st
import time

# 1. Page Configuration
st.set_page_config(page_title="SME AI Research Hub", layout="centered")

# Custom CSS for the Professional Dashboard Look
st.markdown("""
    <style>
    .main { background-color: #f4f7f9; }
    .stButton>button {
        width: 100%; border-radius: 4px; height: 3.5em;
        background-color: #004a99; color: white; font-weight: bold; border: none;
    }
    .stButton>button:hover { background-color: #003366; color: white; border: none; }
    h1 { color: #002b5c; font-family: 'Helvetica Neue', Arial, sans-serif; }
    h3 { color: #004a99; border-bottom: 1px solid #dee2e6; padding-bottom: 10px; margin-top: 30px; }
    
    /* Metrics Styling for Analysis Tab */
    .metric-container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #e0e6ed;
        margin-bottom: 15px;
    }
    .metric-label {
        font-size: 13px;
        color: #6c757d;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    .metric-value {
        font-size: 28px;
        color: #004a99;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("SME AI Adoption & Integration Hub")
st.write("A research-backed platform for AI diagnostic and strategic implementation.")

# Define Tabs
tab1, tab2, tab3 = st.tabs(["Readiness Scorecard", "Comparative Analysis", "Adoption Framework"])

# --- TAB 1: READINESS SCORECARD ---
with tab1:
    st.markdown("### Organizational Readiness Diagnostic")
    st.write("Evaluate your business based on the six strategic pillars of AI readiness.")
    
    st.markdown("#### 1. Organizational Profile")
    data_status = st.radio("Is your business data (invoices, logs, etc.) digital?", 
                           ["Mostly Paper/Manual", "Some Digital (Excel)", "Fully Digital/Cloud"])
    staff_skill = st.slider("Staff AI Skill Level (1 = Low, 10 = High)", 1, 10, 5)

    st.markdown("#### 2. Project & Use-Case Definition")
    task_frequency = st.selectbox("How often is the task performed?", ["Daily (High)", "Weekly (Medium)", "Monthly (Low)"])
    task_risk = st.select_slider("What is the risk if a mistake is made?", options=["Low", "Medium", "High"])

    st.markdown("#### 3. Resources & Integration")
    budget_status = st.selectbox("Dedicated budget for AI subscriptions:", 
                                 ["No Budget", "Low (Under $30/mo)", "Moderate (Over $50/mo)"])
    integration_ready = st.radio("Can your current software connect to cloud apps?", 
                                 ["No/Unknown", "Yes, we use cloud-connected tools"])

    score = 0
    if data_status == "Fully Digital/Cloud": score += 15
    elif data_status == "Some Digital (Excel)": score += 7
    if staff_skill > 6: score += 10
    if task_frequency == "Daily (High)": score += 10
    if task_risk == "Low": score += 10
    elif task_risk == "Medium": score += 5
    if budget_status == "Moderate (Over $50/mo)": score += 10
    if integration_ready == "Yes, we use cloud-connected tools": score += 10

    if st.button("Evaluate Organizational Readiness"):
        with st.spinner("Analyzing profile..."):
            time.sleep(1)
            st.divider()
            if data_status == "Mostly Paper/Manual":
                st.error("RECOMMENDATION: PHASE 1 - READINESS ASSESSMENT")
                st.write("Priority: Digital Migration. Move records to cloud systems before adopting AI.")
            elif score >= 30 and task_risk != "High":
                st.success("RECOMMENDATION: PHASE 4 - PILOT IMPLEMENTATION")
                st.write("Priority: Controlled Integration. Start a 30-day 'Human-in-the-Loop' pilot project.")
            elif score >= 15:
                st.warning("RECOMMENDATION: PHASE 2 - USE-CASE SELECTION")
                st.write("Priority: Experimental Testing. Identify low-risk, high-frequency tasks.")
            else:
                st.info("RECOMMENDATION: PHASE 1 - PREPARATION")
                st.write("Priority: Personnel Upskilling. Invest in staff technical training.")

# --- TAB 2: COMPARATIVE ANALYSIS ---
with tab2:
    st.markdown("### Research Analysis: AI vs. Traditional Methods")
    st.write("A comprehensive evaluation of over 30 SMEs comparing emerging AI technologies against established manual methodologies.")

    # 1. Introduction & Demographics
    st.markdown("#### 1. Demographic Overview")
    st.markdown("""
    * **Global Reach:** 83.8% of respondents are based in India, with additional participation from the UAE, Australia, Oman, and the UK.
    * **Scale:** The study primarily covers Micro Enterprises (38.7%) and Small Enterprises (32.3%).
    * **Maturity:** 45.2% of businesses currently utilize a 'Hybrid' model, while 32.3% remain strictly 'Traditionalists'.
    """)

    # 2. Performance Metrics
    st.markdown("#### 2. Performance Metrics of AI-Based Services")
    st.markdown("""
    * **Operational Speed:** 71.4% of users rated task completion as 'Fast' or 'Very Fast'.
    * **The Accuracy Gap:** Only 57.1% reported high accuracy, highlighting a need for verification.
    * **Time Efficiency:** 85.7% of participants identified significant 'Time Savings' as a primary benefit.
    * **Economic Impact:** 64.3% found AI to be more cost-effective in the long-term compared to manual labor.
    """)

    # 3. The Traditional Perspective & Barriers
    st.markdown("#### 3. Barriers to AI Adoption")
    st.markdown("""
    * **Trust Preference:** 64.3% of respondents believe traditional manual methods are more accurate for high-stakes tasks.
    * **The Technical Gap:** 60.0% cite a lack of technical skills or internal IT support as the primary hurdle.
    * **Awareness:** 50.0% report a lack of specific knowledge regarding relevant AI use-cases.
    * **Future Intent:** Despite barriers, 80.0% expressed interest in adopting AI in the future.
    """)

    # 4. Strategic Requirements
    st.markdown("#### 4. Requirements for Successful Integration")
    st.markdown("""
    * **Training:** 57.1% require specialized staff training to demystify AI tools.
    * **Integration Support:** 57.1% need assistance bridging legacy systems with cloud AI tools.
    * **Strategic Roadmaps:** 35.7% identified a need for a clear, step-by-step adoption framework.
    """)

    st.divider()
    st.info("**Conclusion:** The 'Trust Deficit' (64.3%) remains the largest obstacle. Integration must prioritize human-led verification to leverage the 78.6% speed advantage found in AI.")

# --- TAB 3: ADOPTION FRAMEWORK ---
with tab3:
    st.markdown("### SME AI Adoption Framework")
    st.write("A structured 5-Phase strategic roadmap for transitioning to verified AI integration.")

    with st.expander("Phase 1: Readiness Assessment"):
        st.write("Audit and digitize internal records. Ensure infrastructure is cloud-ready.")
    
    with st.expander("Phase 2: Use-Case Selection"):
        st.write("Prioritize high-frequency, low-risk tasks to minimize operational disruption.")
    
    with st.expander("Phase 3: Platform Choice"):
        st.write("Select scalable, plug-and-play SaaS solutions over custom developments.")
    
    with st.expander("Phase 4: Pilot Implementation (Human-in-the-Loop)"):
        st.write("The verification stage. Run AI and manual methods in parallel to build trust.")
    
    with st.expander("Phase 5: Upskilling & Scaling"):
        st.write("Address the 57% demand for training by conducting staff workshops.")

st.markdown("---")
st.caption("Strategic Research Hub - Presented by Varun Krishna M")