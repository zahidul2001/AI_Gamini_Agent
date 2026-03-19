# tools.py
import json
from typing import Dict
import wikipediaapi

# ----------------------
# Search Tool
# ----------------------
def search_tool(query: str) -> str:

    # Example simulated search result
    simulated_results = [
        f"Research paper about {query}",
        f"Latest news on {query}", 
        f"Academic study: {query}"
    ]
    return f"Search results for '{query}': {simulated_results}"


#Wikipedia থেকে Verified Data,Clean Summary Format,Up-to-date Information,English, Bengali, etc
def wiki_tool(topic: str) -> str:
    
    try:
        # Wikipedia API setup #wikipediaapi.Wikipedia() এর মাধ্যমে আমরা Wikipedia এর বিভিন্ন Options Select করতে পারি
        wiki_wiki = wikipediaapi.Wikipedia(
            user_agent='GeminiResearchAgent/1.0 (md.salahuddin@example.com)',
            language='en',
            extract_format=wikipediaapi.ExtractFormat.WIKI
        )
        
        # Page fetch করুন
        page = wiki_wiki.page(topic)
        
        if page.exists():
            # Summary return করুন (first 500 characters)jodi sumarry barite chi tokhon 500 ar jaygay 10000 diya dimo
            if len(page.summary) > 500:
                summary = page.summary[0:500] + "..."
            else:
                summary = page.summary
                
            return f"Wikipedia Summary for '{topic}': {summary}"
        else:
            return f"Wikipedia page not found for '{topic}'. Try different keywords or check spelling."
            
    except Exception as e:
        return f"Error accessing Wikipedia API: {str(e)}"


# Save Tool #Save Tool হলো এজেন্টের "মেমোরি বক্স" যে:,সমস্ত গবেষণার ফলাফল সুরক্ষিতভাবে ফাইলে জমা রাখে

def save_tool(data: Dict) -> str:
    """
    Save Tool: Agent output save করার function
    """
    try:#
        # Save data to a JSON file
        with open("saved_research.json", "a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")
        return "Data saved successfully!"
    except Exception as e:
        return f"Error saving data: {e}"