# app/server.py

import litserve as ls
from models.api_hf_text_generation import HFAPI
from models.api_hf_rerank import HFRerankAPI
from models.api_embedding import EmbeddingAPI
from utils.logger import SimpleLogger, PredictionTimeLogger
from dotenv import load_dotenv
from starlette.middleware.cors import CORSMiddleware

import os

load_dotenv()

if __name__ == "__main__":

    # Define the CORS settings
    cors_middleware = (
        CORSMiddleware,
        {
            "allow_origins": ["*"],  # Allows all origins
            "allow_methods": ["GET", "POST"],  # Allows GET and POST methods
            "allow_headers": ["*"],  # Allows all headers
        },
    )
    callbacks = [PredictionTimeLogger()]
    if os.getenv("model_type") == "text-generation":
        print("text-generation")
        api = HFAPI()
        server = ls.LitServer(
            api,
            spec=ls.OpenAISpec(),
            accelerator="auto",
            stream=True,
            middlewares=[cors_middleware],
            callbacks=callbacks,
        )
    elif os.getenv("model_type") == "embedding":
        print("embedding")
        api = EmbeddingAPI()
        server = ls.LitServer(
            api, accelerator="auto", api_path="/v1/embeddings", middlewares=[cors_middleware], callbacks=callbacks
        )
    else:
        print("rerank")
        api = HFRerankAPI()
        server = ls.LitServer(api, accelerator="auto", middlewares=[cors_middleware], callbacks=callbacks)
    server.run(port=8000)
