from model import load_model
from prompt_template import prompt_template
from langchain_core.output_parsers import StrOutputParser


llm = load_model()
prompt = prompt_template()
chain= prompt | llm | StrOutputParser()

def generate_script(topic):
    response = chain.stream({
        "topic": topic
    })
    script = ""
    for chunk in response:
        script += chunk
    return script

print(generate_script(topic = "Large Language Models"))