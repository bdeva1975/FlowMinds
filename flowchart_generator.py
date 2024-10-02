import streamlit as st
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up OpenAI client
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY"),
)

def generate_response(prompt):
    """Generate a response using OpenAI's API"""
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that provides informative answers."},
            {"role": "user", "content": prompt}
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content

def generate_mermaid_flowchart(response):
    """Generate a more complex Mermaid flowchart based on the response"""
    flowchart_prompt = f"""
    Based on the following response, create a detailed Mermaid flowchart that illustrates the main steps, concepts, and their relationships:

    {response}

    Provide only the Mermaid flowchart code, without any additional explanation.
    Use the following format and guidelines:
    1. Start with 'flowchart TD' for a top-down flowchart
    2. Define all nodes before using them in connections. Use descriptive IDs and labels, e.g.:
       A([Start])
       B[Process 1]
       C{{"Decision 1"}}
    3. Use various node shapes to represent different types of steps:
       - Rectangles for processes: id[Process]
       - Diamonds for decisions: id{{"Decision"}}
       - Rounded rectangles for start/end: id([Start/End])
       - Circles for connections: id((Connection))
    4. After defining all nodes, connect them with arrows and descriptive labels, e.g.:
       A --> B
       B --> C
       C -->|Yes| D
       C -->|No| E
    5. Use subgraphs to group related processes if necessary:
       subgraph title
         content
       end
    6. Add colors to nodes for better visualization, e.g., 'style C fill:#f9f,stroke:#333,stroke-width:4px'
    7. Limit the flowchart to at most 15-20 nodes for clarity, focusing on the most important steps
    8. Ensure each element (node definition, connection, style) is on a new line for better readability
    9. Use double quotes for labels or descriptions containing spaces

    Example:
    flowchart TD
        A([Start])
        B[Process 1]
        C{{"Decision 1"}}
        D[Process 2]
        E[Process 3]
        F((Connection 1))
        G[Process 4]
        H([End])

        A --> B
        B --> C
        C -->|Yes| D
        C -->|No| E
        D --> F
        E --> F
        F --> G
        G --> H
        
        subgraph sub1 [Subprocess]
            I[Step 1]
            J[Step 2]
            I --> J
        end
        
        B --> sub1
        sub1 --> G
        
        style C fill:#f96,stroke:#333,stroke-width:4px
        style F fill:#f96,stroke:#333,stroke-width:4px
    """
    
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": "You are a helpful assistant that creates detailed Mermaid flowcharts."},
            {"role": "user", "content": flowchart_prompt}
        ],
        model="gpt-3.5-turbo",
    )
    return chat_completion.choices[0].message.content

# Streamlit app
st.title("AI-Powered Complex Flowchart Generator")

st.write("""
This application uses OpenAI's API to generate responses to your questions and create detailed flowcharts based on those responses.
It can handle complex processes and relationships. Enter a question or topic below to get started!
""")

# User input
user_input = st.text_input("Enter your question or topic:", "Explain the process of machine learning model development and deployment")

if st.button("Generate Response and Flowchart"):
    with st.spinner("Generating response and flowchart..."):
        # Generate response
        response = generate_response(user_input)
        
        # Display response
        st.subheader("Generated Response:")
        st.write(response)
        
        # Generate and display flowchart
        flowchart = generate_mermaid_flowchart(response)
        st.subheader("Generated Mermaid Flowchart Code:")
        st.text(flowchart)
        
        st.write("""
        To visualize this flowchart:
        1. Copy the code above
        2. Go to https://mermaid.live/
        3. Paste the code into the left panel
        4. The flowchart will be rendered in the right panel
        
        Note: If the flowchart is too complex to render, try removing some nodes or simplifying the relationships.
        """)

# Add some information about the app
st.sidebar.title("About")
st.sidebar.info(
    "This app uses OpenAI's API to generate informative responses and create "
    "detailed flowcharts based on user input. The flowcharts are generated "
    "using Mermaid syntax and can represent complex processes and relationships. "
    "To visualize the flowchart, follow the instructions provided below the generated code."
)

# Footer
st.markdown("---")
st.markdown("Powered by OpenAI and Streamlit")