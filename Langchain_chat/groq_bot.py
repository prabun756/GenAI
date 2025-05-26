from langgraph.graph import StateGraph
from langchain_core.messages import HumanMessage, AIMessage
from groq_config import get_grqu_llm
from typing import TypedDict, List, Union

class GraphState(TypedDict):
    messages: List[Union[HumanMessage,AIMessage]]
    
def init_state() -> GraphState:
    return {"messages": []}

def chat_node(state: GraphState) -> GraphState:
    llm = get_grqu_llm()
    messages = state["messages"]
    response = llm.invoke(messages)
    return{"messages": messages + [response]}

def build_graph():
    graph = StateGraph(GraphState)
    graph.add_node("chat",chat_node)
    graph.set_entry_point("chat")
    graph.set_finish_point("chat")
    compiled = graph.compile()
    return compiled
