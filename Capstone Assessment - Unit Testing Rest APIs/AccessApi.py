
import requests
import json


class AccessApi:
    """
    Class AccessApi is used to abstract lower level access to course required API

    Attributes
    ----------
    url : str
        A valid website used to hold the courses json filesS

    Methods
    -------
    url_active()
        returns True if the url is currently responding without errors, and False if not.

    get_end_point(endpoint)
        returns the json output of the GET request

    """
    def __init__(self, url):
        """
        Parameters
        ----------
        url: str
           a valid website forexample: http://google.com
        """
        self.url = url
        

    @property
    def url(self) -> str:
        #print("Getting...")
        return self._url


    @url.setter
    def url(self, url: str):
        #print("Setting...")
        self._url = url
        

    def url_active(self) -> bool:
        r = requests.get(self._url)
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError:
            # Implement error type determiner?
            print("HTTP error encountered. Error type:", r)
            return False
        print("URL is actively working...")
        return True
        
       
    def get_end_point(self, end_point:str) -> dict:
        """
            Parameters
            ----------
            end_point: str
               a valid endpoint on a website  "api/sites/master.json"
        """
        url_with_endpoint = str(self._url + end_point)
        r = requests.get(url_with_endpoint)
        request_content = json.loads(r.text)
        return request_content
        
      
    def get_status_code(self, end_point:str) -> int:
        """
            Parameters
            ----------
            end_point: str
               a valid endpoint on a website  "api/sites/master.json"
        """
        url_with_endpoint = str(self._url + end_point)
        r = requests.get(url_with_endpoint)
        request_status = r.status_code
        return request_status


    def get_elapsed_time(self, end_point:str) -> float:
        """
            Parameters
            ----------
            end_point: str
               a valid endpoint on a website  "api/sites/master.json"
        """
        url_with_endpoint = str(self._url + end_point)
        r = requests.get(url_with_endpoint)
        request_time = r.elapsed.total_seconds()
        return request_time

"""
Test Code:

reference = AccessApi("https://raw.githubusercontent.com/cengage-ide-content/")

reference.url_active()

end_point = "APItesting/main/getBillingInfo.json"

reference.get_end_point(end_point)

print(reference.get_status_code(end_point))

print(reference.get_elapsed_time(end_point))
"""
