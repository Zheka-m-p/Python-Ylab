def domain_name(url):
    s = url.split('://')
    if 'http' in s[0]:
        ans = s[1].split('.')
    else:
        ans = s[0].split('.')
    if ans[0] != 'www':
        return ans[0]
    else:
        return ans[1]
