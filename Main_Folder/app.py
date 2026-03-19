# app.py
import streamlit as st
from dotenv import load_dotenv
import os
from pydantic import BaseModel
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import initialize_agent, AgentType, Tool
from tools import search_tool, wiki_tool, save_tool
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Structured response
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-001",temperature=0.1, google_api_key=GEMINI_API_KEY)

# Parser
parser = PydanticOutputParser(pydantic_object=ResearchResponse) 


prompt = ChatPromptTemplate.from_messages([
    ("system", """
        You are a research assistant that will help generate research papers.
        Answer the user query and use necessary tools.
        
        **CRITICAL: You MUST output ONLY valid JSON in this exact format:**
        {format_instructions}
        
        Do not include any other text, explanations, or markdown.
    """),
    ("placeholder", "{chat_history}"),
    ("human", "{query}"),
    ("placeholder", "{agent_scratchpad}"),#এজেন্টের ভেতরের চিন্তাভাবনা লিখে 
]).partial(format_instructions=parser.get_format_instructions())

# Tools for the agent
tools = [
    Tool(name="Search", func=search_tool, description="Use for searching relevant information"),
    Tool(name="Wiki", func=wiki_tool, description="Use for Wikipedia summaries"),
    Tool(name="Save", func=save_tool, description="Use for saving outputs"),
]

# Initialize agent,এজেন্টের মূল ইঞ্জিন তৈরি করে!
agent_executor = initialize_agent(
    tools=tools, 
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True 
)

# Streamlit UI#UI মানে হলো "ইউজার ইন্টারফেস" - অর্থাৎ:"অ্যাপের সেই অংশ যেটা দিয়ে ইউজার কথা বলে,ইনপুট দেয়, এবং আউটপুট দেখে"
st.title("🔬 Gemini Research Agent")
st.markdown("Enter your research topic below and get AI-powered research with real Wikipedia data!")

query = st.text_input("Enter your research query:", placeholder="e.g., Artificial Intelligence, Climate Change, Bangladesh History")

if st.button("🚀 Run Research") and query:
    with st.spinner("Researching... This may take a few seconds."):
        raw_response = agent_executor.run(query)
   
    try: 
        structured_response = parser.parse(raw_response) 
        st.success("✅ Research Complete!")
        st.json(structured_response.dict())
        
        # Display nice summary
        st.markdown("### 📊 Research Summary") 
        st.write(structured_response.summary)
        
        st.markdown("### 🔧 Tools Used")
        st.write(", ".join(structured_response.tools_used))
        
    except Exception as e:# ওয়ার্নিং মেসেজ দেখায়,Raw response দেখায় (JSON format এ না হলেও),Hardcoded way তে tools used দেখায়
        st.warning("📝 Showing research results (formatting issue):")
        st.markdown("### 🔍 Research Summary")
        st.write(raw_response)
        
        # Extract and display structured info manually
        st.markdown("### 🛠️ Tools Used")
        st.info("Search, Wiki, Save")
        st.markdown("### 📌 Research Topic")
        st.info(query)


## terminal_agent.py
# print("🔬 Gemini Research Agent (Terminal Version)")
# print("=" * 50)

# while True:
#     print("\nআপনার গবেষণার প্রশ্ন লিখুন (বা 'exit' লিখে বের হোন):")
#     query = input("👉 ")
    
#     if query.lower() in ['exit', 'quit', 'bye']:
#         print("👋 Agent বন্ধ হচ্ছে...再见!")
#         break
    
#     if query.strip():
#         print("\n🔍 গবেষণা চলছে...")
#         try:
#             raw_response = agent_executor.run(query)
            
#             # Try to parse as JSON
#             try:
#                 structured_response = parser.parse(raw_response)
                
#                 print("\n✅ গবেষণা সম্পূর্ণ!")
#                 print(f"📌 বিষয়: {structured_response.topic}")
#                 print(f"📊 সারসংক্ষেপ: {structured_response.summary}")
#                 print(f"🔧 ব্যবহৃত টুলস: {', '.join(structured_response.tools_used)}")
#                 print(f"📚 সোর্সসমূহ:")
#                 for source in structured_response.sources:
#                     print(f"   - {source}")
                    
#             except:
#                 # If JSON parse fails, show raw response
#                 print("\n📝 গবেষণা ফলাফল:")
#                 print(raw_response)
                
#         except Exception as e:
#             print(f"❌ ত্রুটি: {e}")
#     else:
#         print("❌ দয়া করে একটি বৈধ প্রশ্ন লিখুন。")