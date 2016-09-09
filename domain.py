from urllib.parse import urlparse


# get sub-domain name (subdomain.example.com)
def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except:
        return ""


# get domain name (example.com)
def get_domain_name(url):
    try:
        results = get_sub_domain_name(url).split(".")
        return results[-2] + "." + results[-1]
    except:
        return ""
