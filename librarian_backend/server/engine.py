import os
import random
import re
import time
from llmware.retrieval import Query
from llmware.library import Library
from llmware.configs import LLMWareConfig
from llmware.prompts import HumanInTheLoop, Prompt

def execute_query(library_path, query):
    try:
        # existing code
        prompter = Prompt().load_model("gpt-3.5-turbo-instruct", from_hf=False, api_key="")    
        lib = Library().create_new_library(str(random.randint(0, 9999)))
        lib.add_files(library_path)
        embedding_model = "mini-lm-sbert"
        lib.install_new_embedding(embedding_model_name=embedding_model, vector_db="faiss")
        os.environ["TOKENIZERS_PARALLELISM"] = "false"
        query_results = Query(lib).text_query(query, result_count=10)
        prompter.add_source_query_results(query_results)
        responses = prompter.prompt_with_source(query, prompt_name="default_with_context", temperature=0.3)
        for response in responses:
            if 'llm_response' in response:
                print (" > LLM response:\n" + response["llm_response"])
            # print (" > LLM evidence:\n" + response["evidence"])
        if 'llm_response' in response:
            return response["llm_response"] #, response["evidence"]
        else:
            return "I'm not too sure. I couldn't find enough context in your library."
    except Exception as e:
        return "An error occurred while processing your query. Please try again with a more specific question. " + e