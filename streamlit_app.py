import streamlit as st

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
mport streamlit as st

st.title("buy your wallet!!")

number = st.number_input("Enter the quantity of wallets, $20 each",min_value=0, max_value=10, step=1, key="wallets")
price_of_wallet = number*20

if "button_press" not in st.session_state:
    st.session_state.button_press = False

if st.button("Customise your wallet"):
    st.session_state.button_press = True
    
amount_of_wallet = number
if amount_of_wallet > 0 and st.session_state.button_press:
    choice = st.selectbox("Select one material", ["leather", "nylon", "canvas"])

    if choice == "leather":
        st.write("For leather add $50")
        price_of_wallet += 50
    elif choice == "nylon":
        st.write("For nylon add $25")
        price_of_wallet += 25
    else:
        st.write("Canvas adds $0")

    st.button("Purchase")

st.write("Your total =", price_of_wallet)
