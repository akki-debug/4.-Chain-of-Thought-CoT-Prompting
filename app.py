import streamlit as st

# Function to simulate CoT tweet generation with reasoning
def generate_tweet(hook, value, cta):
    tweet = f"{hook} {value} {cta}"
    return tweet, len(tweet)

# Streamlit App Title
st.title("Business Tweet Generator with Chain-of-Thought (CoT) Prompting")

# Introduction: Explain the CoT Prompting Approach
st.write("""
This app uses **Chain-of-Thought (CoT)** prompting to guide you through creating engaging business tweets step-by-step.
Each tweet will consist of:
1. An attention-grabbing **Hook**,
2. A meaningful **Value statement**, and
3. A clear **Call-to-Action (CTA)**.
""")

# Step 1: Hook - Prompt for an attention-grabbing opener with example
st.subheader("Step 1: Hook")
st.write("Provide a catchy statement to grab attention.")
hook = st.text_input("Hook (e.g., 'Want to grow your business?'):")

# Provide suggestion for the hook
if not hook:
    st.info("Example: 'Want to grow your business?'")

# Step 2: Value - Prompt for the core value or message of the tweet
if hook:
    st.subheader("Step 2: Value")
    st.write("Add value by explaining how the topic is beneficial or insightful.")
    value = st.text_input("Value (e.g., 'Here’s a simple strategy that works for every business.'): ")

    # Provide suggestion for value
    if not value:
        st.info("Example: 'Here’s a simple strategy that works for every business.'")

# Step 3: Call-to-Action - Prompt for the action you want the audience to take
if hook and value:
    st.subheader("Step 3: Call-to-Action")
    st.write("What action do you want your audience to take after reading your tweet?")
    cta = st.text_input("Call-to-Action (e.g., 'Learn more by clicking here!'): ")

    # Provide suggestion for call-to-action
    if not cta:
        st.info("Example: 'Learn more by clicking here!'")

# Live preview of tweet as user inputs the text
st.subheader("Live Tweet Preview")
if hook or value or cta:
    preview = f"{hook} {value} {cta}"
    st.write(preview)

# Check length of the tweet
if hook and value and cta:
    tweet, length = generate_tweet(hook, value, cta)
    
    if length > 280:
        st.warning(f"Your tweet is {length} characters long. Twitter allows only 280 characters.")
    else:
        st.success(f"Your tweet is {length} characters long, which is within the limit.")

    # Button to finalize tweet
    if st.button("Generate Final Tweet"):
        st.subheader("Generated Tweet")
        st.write(tweet)
        st.success("Tweet generated successfully!")

# Provide guidance if steps are incomplete
if not hook:
    st.info("Start by providing a catchy hook.")
elif hook and not value:
    st.info("Now, add some valuable content related to the topic.")
elif hook and value and not cta:
    st.info("Finally, give your audience a clear call-to-action to engage with the tweet.")
