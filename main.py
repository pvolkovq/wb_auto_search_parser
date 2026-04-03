import asyncio
import httpx
import random
import pandas as pd
import urllib.parse as up
from typing import Union
from datetime import datetime
from constants import BASE_HEADERS, BASE_PAYLOAD, BASE_URL, REQUEST_TIMING_RANGE, ResponseType, SEMAPHORE_VALUE, PRODUCT_URL, PRODUCT_COLUMNS

collected_data = pd.DataFrame(columns=PRODUCT_COLUMNS)
semaphore = asyncio.Semaphore(SEMAPHORE_VALUE)
user_query = up.quote(input("Введите запрос: "))


async def main():
    total_pages = await get_total_pages(user_query) + 1
    tasks = [collect_data(i, semaphore) for i in range(1, total_pages)]
    await asyncio.gather(*tasks)
    collected_data.to_excel("./result.xlsx", index=False)
    
async def get_total_pages(user_query: str) -> int:
    total_pages = 0
    url = BASE_URL.format(user_query, "")
    response = await get_data("GET", url, BASE_HEADERS, BASE_PAYLOAD, ResponseType.JSON)
    if "total" in response.keys():
        total_pages = response.get("total") // 100
    return total_pages

async def collect_data(i, semaphore) -> None:
    url = BASE_URL.format(user_query, f"&page={i}")
    async with semaphore:
        print(f"Page {i} is collecting")
        response = await get_data("GET", url, BASE_HEADERS, BASE_PAYLOAD, ResponseType.JSON)
        products = response.get("products")
        if products:
            for product in products:
                sku = {
                    "name": product.get("name"),
                    "brand": product.get("brand"),
                    "supplier": product.get("supplier"),
                    "url": PRODUCT_URL.format(product.get("id")),
                    "collected_at": datetime.now().isoformat(),
                }
                if "sizes" in product:
                    sku["price_regular"] = product["sizes"][0]["price"].get("basic")
                    sku["price_discount"] = product["sizes"][0]["price"].get("product")
                collected_data.loc[len(collected_data)] = sku

async def get_data(method: str, url: str, headers: dict, data: dict, response_type: str) -> Union[dict, None]:
    attempts, max_attempts = 1, 10
    await asyncio.sleep(random.uniform(*REQUEST_TIMING_RANGE))
    while attempts < max_attempts:
        async with httpx.AsyncClient() as client:
            response = await client.request(method=method, url=url, headers=headers, data=data)
            if response:
                if response_type == ResponseType.JSON:
                    return response.json()
                elif response_type == ResponseType.TEXT:
                    return response.text
            else:
                attempts += 1
    return None

if __name__ == "__main__":
    asyncio.run(main())
