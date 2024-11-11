from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline , TextStreamer
from langchain_huggingface.llms import HuggingFacePipeline
import litserve as ls
import os , ast
class HFAPI(ls.LitAPI):
    def setup(self, device):
        model_id = os.getenv("model_id","gpt2")
        pipeline_kwargs = ast.literal_eval(os.getenv("pipeline_kwargs",'{}'))
        if device == 'cpu':
            device = -1
        self.hf = HuggingFacePipeline.from_model_id(
            model_id=model_id,
            task="text-generation",
            device=device,
            pipeline_kwargs=pipeline_kwargs,
        ).bind(skip_prompt=True)

    def predict(self, prompt):
        for chunk in self.hf.stream(prompt):
            yield chunk

if __name__ == "__main__":
    api = HFAPI()
    server = ls.LitServer(api, spec=ls.OpenAISpec())
    server.run(port=8000)