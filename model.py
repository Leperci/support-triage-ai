# model.py
from langchain_ibm import ChatWatsonx
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from pydantic import BaseModel, Field
from config import PARAMETERS, CREDENTIALS, LLAMA3_MODEL_ID, GRANITE_MODEL_ID, MIXTRAL_MODEL_ID

class AIResponse(BaseModel):
    category: str = Field(description="The category of the issue (e.g., billing, technical, account, complaint, shipping)")
    sentiment: int = Field(description="Sentiment score from 0 (very negative) to 100 (very positive)")
    summary: str = Field(description="A short summary of the customer's issue")
    next_step: str = Field(description="Suggested next action to handle this issue")

json_parser = JsonOutputParser(pydantic_object=AIResponse)

def initialize_model(model_id):
    return ChatWatsonx(
        model_id=model_id,
        url=CREDENTIALS["url"],
        project_id=CREDENTIALS["project_id"],
        api_key=CREDENTIALS["api_key"],  # <--- here
        params=PARAMETERS
    )

llama3_llm = initialize_model(LLAMA3_MODEL_ID)
granite_llm = initialize_model(GRANITE_MODEL_ID)
mixtral_llm = initialize_model(MIXTRAL_MODEL_ID)

llama3_template = PromptTemplate(
    template='''<|begin_of_text|><|start_header_id|>system<|end_header_id|>
{system_prompt}\n{format_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>
{user_prompt}<|eot_id|><|start_header_id|>assistant<|end_header_id|>
''',
    input_variables=["system_prompt", "format_prompt", "user_prompt"]
)

granite_template = PromptTemplate(
    template="<|system|>{system_prompt}\n{format_prompt}\n<|user|>{user_prompt}\n<|assistant|>",
    input_variables=["system_prompt", "format_prompt", "user_prompt"]
)

mixtral_template = PromptTemplate(
    template="<s>[INST]{system_prompt}\n{format_prompt}\n{user_prompt}[/INST]",
    input_variables=["system_prompt", "format_prompt", "user_prompt"]
)

def get_ai_response(model, template, system_prompt, user_prompt):
    chain = template | model | json_parser
    response_dict = chain.invoke({
        'system_prompt': system_prompt,
        'user_prompt': user_prompt,
        'format_prompt': json_parser.get_format_instructions()
    })
    return AIResponse(**response_dict)  # <- Wrap it into your Pydantic model


def llama3_response(system_prompt, user_prompt):
    return get_ai_response(llama3_llm, llama3_template, system_prompt, user_prompt)

def granite_response(system_prompt, user_prompt):
    return get_ai_response(granite_llm, granite_template, system_prompt, user_prompt)

def mixtral_response(system_prompt, user_prompt):
    return get_ai_response(mixtral_llm, mixtral_template, system_prompt, user_prompt)


