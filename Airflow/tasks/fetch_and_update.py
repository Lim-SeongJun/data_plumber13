import asyncio
from utils.tdata_api import fetch_tdata
from utils.kakao_api import update_address

def fetch_and_update_address():
    """
    TDATA API에서 데이터를 가져오고, 주소를 업데이트하는 함수.
    """
    tdata_json = fetch_tdata()
    updated_data = asyncio.run(update_address(tdata_json))
    return updated_data