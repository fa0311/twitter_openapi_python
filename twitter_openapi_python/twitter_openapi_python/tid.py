import bs4
import requests
from x_client_transaction import ClientTransaction
from x_client_transaction.utils import generate_headers, get_ondemand_file_url, handle_x_migration


def get_tid():
    session = requests.Session()
    session.headers = generate_headers()  # type: ignore
    home_page_response = handle_x_migration(session=session)
    home_page = session.get(url="https://x.com")
    home_page_response = bs4.BeautifulSoup(home_page.content, "html.parser")
    ondemand_file_url = get_ondemand_file_url(response=home_page_response)
    ondemand_file = session.get(url=ondemand_file_url)  # type: ignore
    ondemand_file_response = bs4.BeautifulSoup(ondemand_file.content, "html.parser")
    ct = ClientTransaction(home_page_response=home_page_response, ondemand_file_response=ondemand_file_response)
    return ct
