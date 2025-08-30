from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain

GOOGLE_API_KEY = "AIzaSyC8xhka56EtXXqTotKUDhilPUMz3GlS2Js"

if not GOOGLE_API_KEY or GOOGLE_API_KEY == "YOUR_API_KEY_HERE":
    raise ValueError(
        "Google API key is not set. Please replace 'YOUR_API_KEY_HERE' with your actual key."
    )

llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash-latest",
    temperature=0.7,
    google_api_key=GOOGLE_API_KEY
)

prompt_name = PromptTemplate(
    input_variables=["cuisine"],
    template="Give me only one fancy name for a {cuisine} restaurant. Just the name, no explanation or quotation marks.",
)
chain_name = LLMChain(llm=llm, prompt=prompt_name, output_key="restaurant_name")

prompt_menu = PromptTemplate(
    input_variables=["restaurant_name"],
    template="Suggest 5 popular menu items for a restaurant called '{restaurant_name}'. Return them as a single comma-separated string.",
)
chain_menu = LLMChain(llm=llm, prompt=prompt_menu, output_key="menu_items")

overall_chain = SequentialChain(
    chains=[chain_name, chain_menu],
    input_variables=["cuisine"],
    output_variables=["restaurant_name", "menu_items"],
    verbose=False,
)


def get_name_item(cuisine: str) -> dict:
    if not cuisine or not isinstance(cuisine, str):
        return {"error": "Cuisine must be a non-empty string."}

    response = overall_chain.invoke({"cuisine": cuisine})
    return response


