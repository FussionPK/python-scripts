import sys
import requests

def urls(out_file):
    # Read URLs from standard input
    url2 = sys.stdin.read().splitlines()

    res_urls = []
    bad_urls = []

    for url in url2:
        try:
            # Use HEAD request to check if the URL is accessible
            response = requests.head(url, allow_redirects=True)

            # Check for successful responses (200, 301, 302)
            if response.status_code in [200, 301, 302]:
                res_urls.append(url)
            else:
                bad_urls.append(url)
        except requests.exceptions.MissingSchema:
            bad_urls.append(url)
        except requests.exceptions.ConnectionError:
            bad_urls.append(url)
        except Exception as e:
            # Catch all other exceptions
            print(f"Error checking URL {url}: {e}")
            bad_urls.append(url)

    # Write valid URLs to the output file
    with open(out_file, 'w') as file:
        file.write('\n'.join(res_urls))

    print(f"Saved {len(res_urls)} valid URLs to {out_file}")
    if bad_urls:
        print(f"Encountered {len(bad_urls)} bad URLs: {bad_urls}")

if __name__ == "__main__":
    out_file = 'New_urls.txt'
    urls(out_file)