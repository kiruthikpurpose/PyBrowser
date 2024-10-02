import requests

def fetch_url(url):
    """
    Fetch the content of a URL.
    :param url: The URL to fetch.
    :return: The content of the URL as a string.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None
