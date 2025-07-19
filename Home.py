import streamlit as st

st.set_page_config(
    page_title="Michael Emeakayi Memorial Foundation",
    layout="centered",
)

# --- HERO Section ---
st.image(
"https://your_image_link_here.jpg",
    caption="High Chief Michael Emeakayi",
    use_column_width=True
)

st.title("Michael Emeakayi Memorial Foundation")
st.subheader("Honouring Legacy. Empowering Generations.")

st.write("""
The Michael Emeakayi Memorial Foundation is a registered non-profit organisation established in loving memory of High Chief Michael Emeakayi — a distinguished farmer, philanthropist, and community leader from Umuohi, Okija. His legacy continues to impact lives across generations.
""")

# --- Vision & Mission ---
st.header("Our Vision")
st.write("""
To build a self-reliant, educated, and empowered society through integrated grassroots programmes in education, agriculture, and digital skills.
""")

st.header("Our Mission")
st.write("""
To deliver transformative, community-led initiatives that promote academic excellence, agricultural innovation, and digital empowerment for young people and families in underserved communities.
""")

# --- Who We Are ---
st.header("Who We Are")
st.write("""
Founded in April 2025 by his children, the Foundation is dedicated to advancing local development in Umuohi and beyond. We focus on youth, education, and sustainable livelihoods through our diverse programmes.
""")

# --- Core Initiatives with Images ---
st.header("Our Core Initiatives")

col1, col2 = st.columns(2)

with col1:
    st.image("https://your_scholarship_image_link.jpg", caption="Scholarship Awards", use_column_width=True)
with col2:
    st.subheader("📚 Academic Scholarship Awards")
    st.write("""
    Celebrating academic excellence among primary and secondary school students, with a focus on STEM, business, and agriculture subjects.
""")

col1, col2 = st.columns(2)

with col1:
    st.image("https://your_agriculture_image_link.jpg", caption="Agricultural Empowerment", use_column_width=True)
with col2:
    st.subheader("🌾 Agricultural Empowerment Programme")
    st.write("""
    Hands-on training and support for students in climate-smart farming techniques, with annual awards and produce shared with vulnerable families.
""")

col1, col2 = st.columns(2)

with col1:
    st.image("https://your_it_image_link.jpg", caption="IT Skills Training", use_column_width=True)
with col2:
    st.subheader("💻 IT Skills Training (Launching 2026)")
    st.write("""
    Digital literacy and foundational tech education to prepare students for the digital economy, starting with a dedicated IT training centre.
""")

# --- Flagship Event ---
st.header("Our Flagship Event")
st.write("""
Each year, the Foundation hosts the Annual Harvest, Award Presentation, and Fundraising Event. This unified celebration brings together students, educators, families, and supporters to honour excellence, distribute scholarships and harvests, and raise funds for future programme cycles.
""")

# --- Board of Trustees ---
st.header("Board of Trustees")

trustees = [
    {
"name": "Hope Chizoba Emeakayi Okafor",
"role": "Founder & Chairperson",
"bio": "Researcher and community advocate based in the UK, leading the vision and coordination of the Foundation."
    },
    {
"name": "Kenneth Okwuchukwu Emeakayi",
"role": "Trustee & Patron",
"bio": "A respected elder statesman and community leader with a long history of public service, mentorship, and advocacy."
    },
    {
"name": "Chisom Francisca Emeakayi",
"role": "Trustee & Secretary",
"bio": "Responsible for administrative coordination and record-keeping of all Foundation activities and meetings."
    },
    {
"name": "Angelina Mmachukwu Emeakayi",
"role": "Trustee, Matron & Wife of the Late High Chief Michael Emeakayi",
"bio": "A pillar of strength in the Umuohi community and lifelong partner to the late Chief. Provides moral and intergenerational guidance."
    },
    {
"name": "Victor Nnamdi Emeakayi",
"role": "Trustee & IT Programme Coordinator",
"bio": "Leads the IT Skills Training Programme, supports overall programme oversight and strategic planning, and champions digital literacy initiatives."
    },
]

for trustee in trustees:
    st.subheader(f"{trustee['name']} — {trustee['role']}")
    st.write(trustee["bio"])

# --- Donate Button ---
st.header("Support Our Mission")
if st.button("💖 Donate Now"):
    st.write("Redirecting to donation page...")
    st.markdown("[Click here to donate](https://your_donation_link.com)")

# --- Volunteer Sign-Up Form ---
st.header("Volunteer Sign-Up")

with st.form("volunteer_form"):
    name = st.text_input("Full Name")
    email = st.text_input("Email Address")
    phone = st.text_input("Phone Number (Optional)")
    message = st.text_area("Tell us how you'd like to help")

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.success(f"Thank you {name}! We will get back to you soon.")

st.info("© 2025 Michael Emeakayi Memorial Foundation")
