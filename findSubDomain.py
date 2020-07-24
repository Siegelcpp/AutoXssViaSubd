import requests

domain = input("Target : ")
# subdomain listelerini okuyoruz
content = open("Wordlists/top1k.txt", 'r').read()
# subdomainleri alt alta satırlara ayırıyoruz
subdomains = content.splitlines()

def DiscoverSub(target):
    for subdomain in subdomains:
        url = f"http://{subdomain}.{domain}"

        try:
            requests.get(url)
        except requests.ConnectionError:
            pass
        else:
            print("Discovered Subdomain [+]", url)


