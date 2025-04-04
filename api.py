from abc import ABC, abstractmethod
from google import genai


class Api(ABC):
    #return text response from apis
    @abstractmethod
    def ask(text):
        pass

class GeminiApi(Api):
    def __init__(self,API_KEY,model = "gemini-2.0-flash"):
        super().__init__()
        self.model = model
        self.gemi = genai.Client(api_key=API_KEY)


    def ask(self,query: str):
        try:
            gemresponse = self.gemi.models.generate_content(model="gemini-2.0-flash",contents= query,)
            return gemresponse.text
        except Exception as e:
            return e
        