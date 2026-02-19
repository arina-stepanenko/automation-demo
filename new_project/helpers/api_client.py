import requests
import logging


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.session()

    def _get_full_url(self, endpoint: str) -> str:
        return f'{self.base_url}{endpoint}'

    def _get_api(self, endpoint: str, params: dict=None):
        """GET-запрос"""
        url = self._get_full_url(endpoint)
        resp = self.session.get(url, params=params)
        logging.info(f"GET-запрос: {url} | params={params} | status={resp.status_code}")

        return resp

    def _post_api(self, endpoint: str, data: dict=None):
        """POST-запрос"""
        url = self._get_full_url(endpoint)
        resp = self.session.post(url, data=data)
        logging.info(f"POST-запрос: {url} | data={data} | status={resp.status_code}")

        return resp

    def _put_api(self, endpoint: str, data: dict=None):
        """PUT-запрос"""
        url = self._get_full_url(endpoint)
        resp = self.session.put(url, data=data)
        logging.info(f"PUT-запрос: {url} | data={data} | status={resp.status_code}")

        return resp

    def _delete_api(self, endpoint: str, headers: dict = None):
        """DELETE-запрос"""
        url = self._get_full_url(endpoint)
        resp = self.session.delete(url, headers=headers)
        logging.info(f"DELETE-запрос: {url} | headers={headers} | status={resp.status_code}")

        return resp