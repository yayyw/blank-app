import streamlit as st

st.title("buy your wallet!!")

number = st.number_input("Enter the quantity of wallets, $20 each",min_value=0, max_value=10, step=1, key="wallets")
price_of_wallet = number*20

#discount price for tiered pricing 

for i in range(number):
    st.subheader("Wallet " + str(i + 1))
    customise = ['size', 'material', 'engraving'] #add colours appeal to more ages bro idk anymore, list
    
    st.write('customisations available:')
    for item in customise: #for loop
        st.write(item)

    customise_key = "customise_pressed_" + str(i)
    engraving_key = "engraving_pressed_" + str(i)
    
    if "customise_pressed" not in st.session_state: #visibility of button
        st.session_state.customise_pressed = False
    if "engraving_pressed" not in st.session_state:
        st.session_state.engraving_pressed = False

    if st.button("Customise your wallet"):
        st.session_state.customise_pressed = True #when button pressed

    amount_of_wallet = number
    if amount_of_wallet > 0 and st.session_state.customise_pressed:
        st.image('https://pngimg.com/uploads/wallet/wallet_PNG77078.png', caption =None, width = 100) 
        size = st.selectbox("Select a size", ["small", "medium", "large"], key="size" + str(i)) #reyna's code + for loop for customers to customise each wallet
        if size == "medium":
            st.write("For medium add $10")
            price_of_wallet += 10
        elif size == "large":
            st.write("For large add $20")
            price_of_wallet += 20
        else:
            st.write("small adds $0")
        
        choice = st.selectbox("Select one material", ["leather", "nylon", "canvas"] + str(i))
        
        if choice == "leather":
            st.write("For leather add $50")
            price_of_wallet += 50
        elif choice == "nylon":
            st.write("For nylon add $25")
            price_of_wallet += 25
        else:
            st.write("Canvas adds $0")
    
        if st.button("Add engraving" + str(i)):
            st.session_state.engraving_pressed = True

        if st.session_state.engraving_pressed:
            st.write("Engraving adds $10")
            engraving_text = st.text_input("What would you like engraved?", key="engraving_text" +str(i))
            price_of_wallet += 10

st.write("Your total =", price_of_wallet)

st.button("Purchase")


