from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.1 )

messages= [
    HumanMessage("Hello, how are you?"),
    SystemMessage("Translate the following text English to French"),
]

if __name__ == "__main__":
    response=model.invoke(messages)
    print(response)
    print(response.content)

