import streamlit as st

#this will be the login page for our webapps.py file which is located in the week9 folder same as this login page

username_1 = "admin"
password_1 = "password"

def login():

    st.set_page_config(
        page_title="Login Page",
        page_icon="🔐",
        layout="centered",
        initial_sidebar_state="auto",
    )

    #in order to make the login title have rainbow colors we can use the following code
    st.markdown(
        """
        <h1 style="background: -webkit-linear-gradient(#00ffff, #333);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-size: 48px;
                    font-weight: bold;
                    text-align: center;">
            Login Page
        </h1>
        """,
        unsafe_allow_html=True
    )

    #what unsafe_allow_html=True does is it allows us to use HTML code in the markdown function the reason its called unsafe is
    #because using HTML code can potentially introduce security risks if the HTML code contains malicious scripts
    
    st.write("Please enter your username and password to login.")

    #create username and password input fields
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    #create a login button
    if st.button("Login"):
        #for simplicity, we will use hardcoded username and password
        if username == username_1 and password == password_1:

            st.success("Login successful!")
            st.session_state['logged_in'] = True
        else:
            st.error("Invalid username or password.")
#check if user is logged in
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False
if not st.session_state['logged_in']:
    login()
else:
    st.markdown(
        f"""
        <h2 style="background: -webkit-linear-gradient(#00ffff, #333);
                    -webkit-background-clip: text;
                    -webkit-text-fill-color: transparent;
                    font-size: 32px;
                    font-weight: bold;
                    text-align: center;">
            Welcome to Andys World! {username_1}
        </h2>
        """,
        unsafe_allow_html=True
    )
    
    #here we can redirect to the main app or show a logout button
    if st.button("Logout"):
        st.session_state['logged_in'] = False
        st.experimental_rerun()

#lets now reroute to the main app if logged in
    if st.session_state['logged_in']:
        import webapps
        webapps.app()
#now run this file to see the login page and when you log in you should see your webapps.py content