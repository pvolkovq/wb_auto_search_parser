BASE_HEADERS = {
  'accept': '*/*',
  'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
  'deviceid': 'site_4928d798e3694c94b87179895970a3fa',
  'priority': 'u=1, i',
  'referer': 'https://www.wildberries.ru/catalog/0/search.aspx?search=%D0%B0%D0%B2%D1%82%D0%BE%D0%BC%D0%BE%D0%B1%D0%B8%D0%BB%D1%8C',
  'sec-ch-ua': '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36',
  'x-queryid': 'qid597299835177029583220260403131752',
  'x-requested-with': 'XMLHttpRequest',
  'x-spa-version': '14.4.0',
  'x-userid': '0',
  'Cookie': '_wbauid=5972998351770295832; x_wbaas_token=1.1000.f26cfbb0466a4ac5af5d7ef753e9bc64.MTV8ODQuMjIuMTMzLjExMXxNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0KSBBcHBsZVdlYktpdC81MzcuMzYgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMTQ2LjAuMC4wIFNhZmFyaS81MzcuMzZ8MTc3NjQzMDExMXxyZXVzYWJsZXwyfGV5Sm9ZWE5vSWpvaUluMD18MHwzfDE3NzU4MjUzMTF8MQ==.MEYCIQCjQDW8yVkYO/ny59RABwjjrZMOKoC9V66Lrb/P7AASfQIhAKomL8dZHSPava5OIBHZQTdU32UjJ6kO8sVJXPXGn6yb'
}
BASE_PAYLOAD = {}
BASE_URL = "https://www.wildberries.ru/__internal/u-search/exactmatch/ru/common/v18/search?ab_testing=false&appType=1&curr=rub&dest=-1255987&hide_vflags=4294967296&inheritFilters=false&lang=ru&query={0}&resultset=catalog&sort=popular&spp=30&suppressSpellcheck=false{1}"
PRODUCT_URL = "https://www.wildberries.ru/catalog/{0}/detail.aspx"

REQUEST_TIMING_RANGE = (0.1, 0.5)
SEMAPHORE_VALUE = 4

class ResponseType:
    JSON = "json"
    TEXT = "text"

PRODUCT_COLUMNS = ["name", "brand", "supplier", "price_regular", "price_discount", "url", "collected_at"]