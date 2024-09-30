import streamlit as st

# Function to simulate CoT tweet generation with reasoning
def generate_tweet(hook, value, cta):
    return f"{hook} {value} {cta}"

# Streamlit App Title
st.title("Business Tweet Generator with Chain-of-Thought (CoT) Prompting")

# Introduction: Explain the CoT Prompting Approach
st.write("""
This app uses **Chain-of-Thought (CoT)** prompting to help generate business tweets that follow a logical, step-by-step structure.
We'll guide you through the process of creating:
1. An attention-grabbing **Hook**,
2. A meaningful **Value statement**, and
3. A clear **Call-to-Action (CTA)**.
""")

# Step 1: Hook - Prompt for an attention-grabbing opener
st.subheader("Step 1: Hook")
st.write("Provide a catchy statement to grab attention.")
hook = st.text_input("Hook (e.g., 'Want to boost your sales?'): ")

# Step 2: Value - Prompt for the core value or message of the tweet
if hook:
    st.subheader("Step 2: Value")
    st.write("Add value by explaining how the topic is beneficial or insightful.")
    value = st.text_input("Value (e.g., 'Here are 3 strategies that top companies use to grow faster.'): ")

# Step 3: Call-to-Action - Prompt for the action you want the audience to take
if hook and value:
    st.subheader("Step 3: Call-to-Action")
    st.write("What action do you want your audience to take after reading your tweet?")
    cta = st.text_input("Call-to-Action (e.g., 'Check out our blog for more tips!'): ")

# Generate the tweet based on the user's input
if st.button("Generate Tweet") and hook and value and cta:
    tweet = generate_tweet(hook, value, cta)
    st.subheader("Generated Tweet")
    st.write(tweet)

# Provide guidance if steps are incomplete
if not hook:
    st.info("Start by providing a catchy hook.")
elif hook and not value:
    st.info("Now, add some valuable content related to the topic.")
elif hook and value and not cta:
    st.info("Finally, give your audience a clear call-to-action to engage with the tweet.")
