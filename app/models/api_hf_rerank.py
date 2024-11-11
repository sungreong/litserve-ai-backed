from langchain_community.cross_encoders import HuggingFaceCrossEncoder
import asyncio
from concurrent.futures import ThreadPoolExecutor
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
import litserve as ls
from typing import Tuple
from dotenv import load_dotenv
import os , ast , json
from fastapi.responses import JSONResponse

load_dotenv()

class HFRerankAPI(ls.LitAPI):
    def setup(self, device: str):
        model_id = os.getenv("model_id","Dongjin-kr/ko-reranker")
        model_kwargs = ast.literal_eval(os.getenv("model_kwargs",'{"device": "cpu"}'))
        self.hf = HuggingFaceCrossEncoder(
            model_name=model_id,
            model_kwargs=model_kwargs,
        )

    def decode_request(self, request):
        return request["input"]

    def predict(self, text_pairs: List[List[str]]):
        score = self.hf.score(text_pairs)
        return score

    def encode_response(self, output):
        return {"score": output.tolist()}

if __name__ == "__main__":
    api = HFRerankAPI()
    server = ls.LitServer(api)
    server.run(port=8000)

