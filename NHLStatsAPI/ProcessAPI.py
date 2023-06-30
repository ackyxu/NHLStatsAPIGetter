import  requests

class ProcessAPI:
    
	def __init__(self, url:str) -> None:
		response: requests.Response
		self.__getRequest(url)

	def __getRequest(self, url: str):

		self.response = requests.get(url)

	
	def getText(self):
		return self.response.text
	
	def getStatusCode(self):
		return self.response.status_code
	
	def getJSON(self):
		return self.response.json()
