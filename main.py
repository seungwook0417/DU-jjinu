import logging
import os
import time

from DU.Config import *
import json

from DU.DUParser import ce_get_list
from DU.telegram import send_telegram

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
)

def hakgwa_json(content):
    data = get_hakgwa()
    for i in data['hakgwa']:
        if content == i['name']:
            url = i['url']
            haksa = i['haksa']
            etc = i['etc']
    return url, haksa, etc

def work(element):
    try:
        config = get_config()
        logging.info(element[1] + " 데이터를 가져왔습니다.")
        telegram_subject = element[0]
        telegram_url = element[1]
        send_telegram(config, telegram_subject, telegram_url)
        logging.info(element[1] + " 데이터를 보냈습니다.")
    except Exception as e:
        logging.error(e)
    pass


def paser(content, firstrun):
    config = get_config()
    memory = []

    memory_max = config["store_cnt"]
 
    if os.path.exists("./data/"+content+".json"):
        memory = json.load(open("./data/"+content+".json", 'r', encoding="utf-8"))
        logging.info("json 로드 성공...")
        if firstrun == True:
            return

    url, haksa, etc = hakgwa_json(content)
    current_list = ce_get_list(url,haksa) + ce_get_list(url,etc)

    for e in current_list:
        if e not in memory:
            if firstrun != True:
                work(e)
                logging.info(" 완료 3초 대기...")
                time.sleep(3)
            memory.append(e)

    logging.info(" 페이지 완료 10초 대기...")
    time.sleep(10)

    if len(memory) > memory_max:
        memory = memory[len(memory) - memory_max:]
        logging.info("memory.json을 정리했습니다.")

    logging.info("memory.json 덤프 중...")
    json.dump(memory, open("./data/"+content+".json", "w", encoding="utf-8"), ensure_ascii=False)

    logging.info("끝났습니다.")

def main():
    data = ['비호생활관','정보보호영재교육원']
    config = get_config()
    for i in data:
        paser(i,config["first_run"])
        time.sleep(10)

if __name__ == '__main__':
    while True:
        main()
        time.sleep(600)

