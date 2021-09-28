from github import Github

repo = Github("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").get_repo("Gustry/test_stale")
gh_release = repo.get_release(id="3.22.0")
print(gh_release, gh_release.tag_name, gh_release.upload_url)

result = gh_release.update_release(
    name="Bob",
    message="Hello",
    draft=False,
    prerelease=False,
)

print(result)
#

import urllib.request

url = 'https://packages.3liz.org/pub/lizmap/release/3.5/lizmap-web-client-3.5.0-rc.2.zip'
urllib.request.urlretrieve(url, '/tmp/bob.zip')

result = gh_release.upload_asset(
    path="/tmp/bob.zip",
    # label="ZIP Package",
    # content_type="zip",
    # name="Bob again",
)
