'''Ваша задача написать функцию get_domain_name, которая принимает строку url, извлекает из нее доменное имя и возвращает его в качестве строки

get_domain_name("http://google.com") => "google"
get_domain_name("http://google.co.jp") => "google"
get_domain_name("www.xakep.ru") => "xakep"
get_domain_name("https://youtube.com") => "youtube"
get_domain_name("https://www.asos.com") => "asos"
get_domain_name("http://www.lenovo.com") => "lenovo"
URL может начинаться с протоколов http://  https:// или с www. URL, начинающиеся с протоколов http://  https://, могут также содержать www.

Ваша задача написать только определение функции get_domain_name'''

def domain_name(url:str) -> str:
    url = url.replace('http://', '')
    url = url.replace('www.', '')
    url = url.replace('https://', '')
    return url.split('.')[0]
    