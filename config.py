# config.py
from dotenv import load_dotenv
load_dotenv()

import os
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams



CREDENTIALS = {
    "url": os.getenv("WATSONX_URL"),
    "api_key": os.getenv("WATSONX_APIKEY"),
    "project_id": os.getenv("WATSONX_PROJECT_ID")
}

PARAMETERS = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 256,
}

LLAMA3_MODEL_ID = "meta-llama/llama-3-2-11b-vision-instruct"
GRANITE_MODEL_ID = "ibm/granite-3-8b-instruct"
MIXTRAL_MODEL_ID = "mistralai/mistral-large"
