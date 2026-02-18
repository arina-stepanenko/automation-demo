import requests as req
import logging


class ApiClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def _get_full_url(self, endpoint: str) -> str:
        return f'{self.base_url}{endpoint}'

    def _get_api(self, endpoint: str, params: dict=None, headers: dict=None):
        """GET-запрос"""
        url = self._get_full_url(endpoint)
        resp = req.get(url, params=params, headers=headers)
        logging.info(f"GET-запрос: {url} | params={params} | status={resp.status_code}")

        return resp

    def _post_api(self, endpoint: str, data: dict=None, json: dict=None, headers: dict=None):
        """POST-запрос"""
        url = self._get_full_url(endpoint)
        resp = req.post(url, data=data, json=json, headers=headers)
        logging.info(f"POST-запрос: {url} | data={data} | status={resp.status_code}")

        return resp

    def _put_api(self, endpoint: str, data: dict=None, json: dict=None):
        """PUT-запрос"""
        url = self._get_full_url(endpoint)
        resp = req.put(url, data=data, json=json)
        logging.info(f"PUT-запрос: {url} | data={data} | status={resp.status_code}")

        return resp

    def _delete_api(self, endpoint: str, headers: dict = None):
        """DELETE-запрос"""
        url = self._get_full_url(endpoint)
        resp = req.delete(url, headers=headers)
        logging.info(f"DELETE-запрос: {url} | headers={headers} | status={resp.status_code}")

        return resp