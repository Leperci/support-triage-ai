# llm_test.py

from model import llama3_response, granite_response, mixtral_response

def call_all_models(system_prompt, user_prompt):
    print("=== Llama3 Response ===")
    try:
        r1 = llama3_response(system_prompt, user_prompt)
        import json
        print(r1.model_dump_json(indent=2))


    except Exception as e:
        print("Llama3 Error:", e)

    print("\n=== Granite Response ===")
    try:
        r2 = granite_response(system_prompt, user_prompt)
        print(r2.model_dump_json(indent=2))  # For Pydantic 2+

    except Exception as e:
        print("Granite Error:", e)

    print("\n=== Mixtral Response ===")
    try:
        r3 = mixtral_response(system_prompt, user_prompt)
        print(r3.model_dump_json(indent=2))  # For Pydantic 2+

    except Exception as e:
        print("Mixtral Error:", e)

if __name__ == "__main__":
    system_prompt = (
        "You are an AI support assistant. Your job is to analyze a customer message, "
        "categorize the issue, assess sentiment (0–100), summarize it, and suggest the next step. "
        "Respond in structured JSON format only."
    )
    user_prompt = "I was charged twice for the same subscription. Can someone fix this?"

    call_all_models(system_prompt, user_prompt)
