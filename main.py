import streamlit as st

# Set page configuration
st.set_page_config(page_title="Image Forgery Detection", layout="wide")

# Initialize session state for navigation
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Function to navigate between pages
def navigate_to(page_name):
    st.session_state.page = page_name

# Custom CSS for styling
st.markdown("""
    <style>
        /* Set background color */
        body {
            background-color: #f0f2f6;
        }
        
        /* Navigation Bar */
        .nav-buttons {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }
        .nav-buttons button {
            margin: 0 10px;
            padding: 10px 20px;
            font-size: 16px;
            border-radius: 10px;
            border: none;
            background-color: #3498db;
            color: white;
            cursor: pointer;
        }
        .nav-buttons button:hover {
            background-color: #2980b9;
        }

        /* Features Section with Black Background */
        .features-container {
            position: absolute;
            top: 100%;
            right: 5%;
            transform: translateY(-50%);
            background-color: #0E1117;  /* Black box */
            color: white; /* White text */
            padding: 20px;
            border-radius: 5px;
            text-align: center;
            width: 400px;
        }
        .features-title {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 15px;
            margin-left;
        }
        .hover-buttons {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }
        .hover-buttons button {
            background-color: #2c3e50;
            color: white;
            border: none;
            padding: 12px 15px;
            font-size: 14px;
            border-radius: 10px;
            transition: background 0.3s, transform 0.2s;
        }
        .hover-buttons button:hover {
            background-color: #34495e;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# Navigation Bar
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🏠 Home"):
        navigate_to("Home")
with col2:
    if st.button("📊 Dashboard"):
        navigate_to("Dashboard")
with col3:
    if st.button("📞 Contact"):
        navigate_to("Contact")

# Home Page
if st.session_state.page == "Home":
    st.title("Welcome to Pixelyse")
    st.write("Your go-to platfoam for Image Forgery Detection and Localisation.")
    
    # Background image
  
     
    # Explore Now button
    if st.button("🚀 Explore Now"):
        navigate_to("Dashboard")

    # Features Section with Black Box
    st.markdown("""
        <div class="features-container">
            <div class="features-title">🔹 Features</div>
            <div class="hover-buttons">
                <button>🖼 Upload image to detect forgery</button>
                <button>📌 Real-time localization of tampered regions</button>
                <button>📊 Comprehensive analysis of digital content</button>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Dashboard Page
elif st.session_state.page == "Dashboard":
    st.title("Dashboard - Upload and Detect Forgery")
    st.write("Upload an image to check for possible forgeries.")

    uploaded_image = st.file_uploader("Choose an image file", type=["jpg", "jpeg", "png"])

    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image", use_container_width=True)
        st.success("Image uploaded successfully!")

        # Detect Forgery Button
        if st.button("🔍 Detect Forgery"):
            st.info("Running forgery detection...")
            st.warning("Forgery detection logic is not implemented yet!")

# Contact Page
elif st.session_state.page == "Contact":
    st.title("📞 Contact Us")
    st.write("For any inquiries, reach out to us:")
    st.write("📧 Email: **pixelysehelp@gmail.com**")
    st.write("📍 Address: Amal Jyothi College Country")
    st.write("📞 Phone: +123 456 7890")
