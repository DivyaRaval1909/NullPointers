import google.generativeai as genai

genai.configure(api_key="AIzaSyA2gwUX6u-Ql-zWj70paKAUlB1zqQe0ILc") 


model = genai.GenerativeModel("gemini-pro")

def generate_gemini_content(prompt):
    """Generates content using the Google Gemini model.

    Args:
        prompt: The input prompt for content generation.

    Returns:
        The generated content as a string.
    """
   
    response = model.generate_content(contents=[prompt]) 
    return response.text


title = generate_gemini_content(f"Generate a title for this summary:\n{final_summary}")


topics = generate_gemini_content(f"Extract 10 diverse and distinct key topics from this summary, one liner and smaller:\n{final_summary}")


topics_list = topics.split("\n")


ai_content_dict = {}
for topic in topics_list[0:]:  
    ai_content_dict[topic] = generate_gemini_content(f"Write a 100-word explanation on: {topic}")
