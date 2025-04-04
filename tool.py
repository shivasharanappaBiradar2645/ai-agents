import wikipedia

def search_wikipedia(query: str, sentences= 5)->str:
    return  wikipedia.summary(query, sentences=sentences )

wikipedia_tool_description = """

Tool: search_wikipedia
Description: Searches Wikipedia and returns a summary of the topic
Input: A search query string
Example: To learn about Python programming, use: search_wikipedia("Python programming language")
"""