from vllm import LLM, SamplingParams
import litserve as ls

class VLLMLlamaAPI(ls.LitAPI):
    def setup(self, device):
        model_id = os.getenv("model_id","meta-llama/Meta-Llama-3-8B-Instruct")
        model_kwargs = ast.literal_eval(os.getenv("model_kwargs",'{}'))
        self.llm = LLM(
            model=model_id, 
            **model_kwargs
            )


    def predict(self, prompt, context):

        sampling_params = SamplingParams(
            temperature=context.get("temperature",0.8), 
            top_p=context.get("top_p",0.95), 
            max_tokens=context.get("max_tokens",100),
            stop=context.get("stop",None),
            seed=context.get("seed",None),
            repetition_penalty=context.get("repetition_penalty",1.15),
            frequency_penalty=context.get("frequency_penalty",0),
            presence_penalty=context.get("presence_penalty",0),
        )
        outputs =  self.llm.generate(prompt, sampling_params)
        yield outputs[0].outputs[0].text


if __name__ == "__main__":
    api = VLLMLlamaAPI()
    server = ls.LitServer(api, spec=ls.OpenAISpec())
    server.run(port=8000)
