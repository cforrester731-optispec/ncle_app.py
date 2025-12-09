import streamlit as st

# --- APP CONFIGURATION ---
st.set_page_config(page_title="NCLE Ultimate Study Guide", page_icon="👁️")

# --- DATA: QUIZ QUESTIONS ---
questions = [
    {
        "question": "You change an RGP Base Curve from 7.50mm to 7.40mm. The original power was -3.00D. Using SAM FAP, what is the new power?",
        "options": ["-2.50D", "-3.00D", "-3.50D", "-4.00D"],
        "answer": "-3.50D",
        "explanation": "SAM: Steeper Add Minus. 7.50 -> 7.40 is steeper by 0.10mm. 0.10mm change = 0.50D change. Add -0.50D to -3.00D = -3.50D."
    },
    {
        "question": "A soft toric lens mark rotates 10 degrees to the LEFT. The original axis is 180. Using LARS, what is the new axis?",
        "options": ["170", "010", "190", "160"],
        "answer": "010",
        "explanation": "LARS: Left Add, Right Subtract. 180 + 10 = 190. In axis notation, 190 is the same as axis 010."
    },
    {
        "question": "A patient has a spectacle Rx of -12.00D. What is the approximate contact lens power (Vertex Distance)?",
        "options": ["-10.50D", "-12.00D", "-13.50D", "-11.00D"],
        "answer": "-10.50D",
        "explanation": "Minus lenses become WEAKER as they get closer to the eye. A -12.00D spec Rx usually vertices to around -10.50D or -10.75D."
    },
    {
        "question": "Which illumination is best for viewing the Endothelium to check for polymegathism?",
        "options": ["Optic Section", "Specular Reflection", "Diffuse Illumination", "Sclerotic Scatter"],
        "answer": "Specular Reflection",
        "explanation": "Specular Reflection uses the mirror-like reflection of the light to view the endothelial cells."
    },
    {
        "question": "What is the 'Magic Number' for converting Radius (mm) to Diopters (D)?",
        "options": ["337.5", "1.337", "44.00", "550"],
        "answer": "337.5",
        "explanation": "Formula: 337.5 / Radius (mm) = Diopters (D)."
    }
]

# --- APP LAYOUT ---
st.title("👁️ NCLE Ultimate Study Trainer")
st.markdown("Master the math and buzzwords for the CLRE/NCLE Basic Exam.")

# Initialize session state for score
if 'score' not in st.session_state:
    st.session_state.score = 0
if 'count' not in st.session_state:
    st.session_state.count = 0

# Sidebar for Navigation
mode = st.sidebar.radio("Select Mode:", ["Study Guide", "Practice Quiz"])

if mode == "Study Guide":
    st.header("The Cheat Sheet Formulas")
    
    st.subheader("1. SAM FAP (RGP Base Curves)")
    st.info("**S**teeper **A**dd **M**inus | **F**latter **A**dd **P**lus\n\nRule: 0.10mm BC change = 0.50D Power change.")
    
    st.subheader("2. LARS (Toric Rotation)")
    st.info("**L**eft **A**dd | **R**ight **S**ubtract\n\nImagine the lens is a clock face. Rotation towards 5 o'clock is LEFT.")
    
    st.subheader("3. Vertex Distance")
    st.warning("Only for Rx > +/- 4.00D\n\n* Plus becomes Stronger (needs more +)\n* Minus becomes Weaker (needs less -)")

elif mode == "Practice Quiz":
    st.header("Pop Quiz")
    
    # Loop through questions
    for i, q in enumerate(questions):
        st.subheader(f"Question {i+1}")
        st.write(q["question"])
        
        # Unique key for each radio button to prevent state issues
        user_choice = st.radio(f"Select an answer for Q{i+1}:", q["options"], key=f"q{i}")
        
        if st.button(f"Check Answer {i+1}", key=f"btn{i}"):
            if user_choice == q["answer"]:
                st.success(f"Correct! {q['answer']}")
                st.write(f"**Why:** {q['explanation']}")
            else:
                st.error(f"Incorrect. The correct answer is {q['answer']}")
                st.write(f"**Why:** {q['explanation']}")
        st.markdown("---")