import requests
import time
from requests import RequestException, TooManyRedirects, HTTPError, ConnectionError, Timeout

def fetch(url, headers=None, retries=5):
    for attempt in range(retries + 1):
        try:
            response = requests.get(url, headers=headers, timeout=5)

            if response.status_code in (429, 403):
                retry_after = response.headers.get("Retry-After")

                if retry_after and retry_after.isdigit():
                    wait = int(retry_after)
                else:
                    wait = 2 ** attempt

                if attempt == retries:
                    print("Rate limit exceeded. Max retries reached.")
                    return None

                print(f"Rate limited. Retrying in {wait} seconds...")
                time.sleep(wait)
                continue

            response.raise_for_status()
            profile_response = response.json()
            return profile_response

        except Timeout:
            print("Request timed out")

        except ConnectionError:
            print("Network problem (DNS failure, refused connection)")

        except HTTPError as e:
            print(f"HTTP error: {e.response.status_code}")
            return None

        except TooManyRedirects:
            print("Too many redirects")
            return None

        except RequestException as e:
            print(f"Unexpected error: {e}")
            return None

    return None