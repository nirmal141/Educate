import requests
class LocalLLM:
    def __init__(self, device="npu"):
        self.device = device
        self.api_base = "http://127.0.0.1:1234"
        # Initialize embedding model
    

    def generate(self, prompt, max_length=512):
        # If vector store exists, retrieve relevant context
        response = requests.post(
            f"{self.api_base}/v1/chat/completions",
            json={"messages": [{"role": "user", "content": prompt}], "temperature": 0.7, "max_tokens": max_length}
        )
        
        if response.status_code == 200:
            return response.json()['choices'][0]['message']['content']
        else:
            raise Exception(f"Error: {response.status_code}, {response.text}")
