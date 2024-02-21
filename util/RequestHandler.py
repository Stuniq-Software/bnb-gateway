import requests
from .logger import CustomLogger

class RequestHandler:
    service_name: str
    service_url: str
    _logger: CustomLogger

    def __init__(self, service_name: str, service_url: str):
        self.service_name = service_name
        self.service_url = service_url
        self._logger = CustomLogger(f"RequestHandler-{service_name}")
    
    def get(self, path: str, headers: dict = None, params: dict = None):
        url = f"{self.service_url}{path}"
        self._logger.info(f"GET {url}")
        response = requests.get(url, headers=headers, params=params)
        self._logger.info(f"Response: {response.status_code}")
        return response
    
    def post(self, path: str, headers: dict = None, data: dict = None):
        url = f"{self.service_url}{path}"
        self._logger.info(f"POST {url}")
        response = requests.post(url, headers=headers, json=data)
        self._logger.info(f"Response: {response.status_code}")
        return response
    
    def put(self, path: str, headers: dict = None, data: dict = None):
        url = f"{self.service_url}{path}"
        self._logger.info(f"PUT {url}")
        response = requests.put(url, headers=headers, json=data)
        self._logger.info(f"Response: {response.status_code}")
        return response
    
    def delete(self, path: str, headers: dict = None, data: dict = None):
        url = f"{self.service_url}{path}"
        self._logger.info(f"DELETE {url}")
        response = requests.delete(url, headers=headers, json=data)
        self._logger.info(f"Response: {response.status_code}")
        return response
    
    def patch(self, path: str, headers: dict = None, data: dict = None):
        url = f"{self.service_url}{path}"
        self._logger.info(f"PATCH {url}")
        response = requests.patch(url, headers=headers, json=data)
        self._logger.info(f"Response: {response.status_code}")
        return response
    
    
    