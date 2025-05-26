import streamlit as st
from langchain_core.messages import HumanMessage
from groq_bot import build_graph, init_state

st.set_page_config(page_title="Chat Bot using langgraph", layout="centered")
st.title("LangGraph + Chat Bot")

if 'state' not in st.session_state or 'graph' not in st.session_state:
    st.session_state.graph = build_graph()
    st.session_state.state = init_state()

# 💬 Show previous chat history
for msg in st.session_state.state['messages']:
    role = "user" if isinstance(msg, HumanMessage) else "ai"
    st.chat_message(role).write(msg.content)

# 🔍 Get user input
user_inp = st.chat_input("Ask something")

if user_inp:
    # Show the new user message
    st.chat_message("user").write(user_inp)

    # Add user message to state
    st.session_state.state['messages'].append(HumanMessage(content=user_inp)) 

    # Invoke the graph
    result = st.session_state.graph.invoke(st.session_state.state)

    # Get AI response and show it
    ai_msg = result['messages'][-1]
    st.chat_message('ai').write(ai_msg.content)

    # Save new state
    st.session_state.state = result

if st.button("Send balloons!"):
    st.balloons()


    
    
    
    
    
    
    
    
# import streamlit as st
# from langchain_core.messages import HumanMessage
# from groq_bot import build_graph, init_state

# st.set_page_config(page_title="Chat Bot using langgraph", layout="centered")
# st.title("LangGraph + Chat Bot")


# if 'state' not in st.session_state  or 'graph' not in st.session_state:
#         st.session_state.graph = build_graph()
#         st.session_state.state = init_state()
#         st.session_state.chat_history = []
# user_inp = st.chat_input("ask something")

# if user_inp:
#     st.chat_message("user").write(user_inp)
#     st.session_state.state['messages'].append(HumanMessage(content=user_inp)) 
#     print("Graph type:", type(st.session_state.graph))
#     result = st.session_state.graph.invoke(st.session_state.state)
#     ai_msg = result['messages'][-1]
#     st.chat_message('ai').write(ai_msg.content)
#     st.session_state.state = result