# -*- coding: utf-8 -*-
# @Time    : 2020-06-25 11:37
# @Author  : liudongyang
# @FileName: schedule.py
# @Software: PyCharm
# 任务调度
import threading

from make_data import MakeData
from save_data import SaveFile


def main(beg, end):
    savedata = SaveFile()
    makedata = MakeData()
    orgs = []
    relations = []
    ptxns = []
    dtxns = []
    txns = []
    stifs = []
    sign = 0
    all_data = ["orgs", "relations", "ptxns", "dtxns", "txns", "stifs"]
    all_table_name = ["t_stan_org", "t_stan_relation", "t_stan_ptxn", "t_stan_dtxn", "t_stan_txn", "t_stan_stif"]
    for num in range(beg, end):
        t_stan_org = makedata.make_stan_org()
        orgs.append(t_stan_org)
        t_stan_relation = makedata.make_stan_relation()
        relations.append(t_stan_relation)
        t_stan_ptxn = makedata.make_stan_ptxn()
        ptxns.append(t_stan_ptxn)
        t_stan_dtxn = makedata.make_stan_dtxn()
        dtxns.append(t_stan_dtxn)
        t_stan_txn = makedata.make_stan_txn()
        txns.append(t_stan_txn)
        t_stan_stif = makedata.make_stan_stif()
        stifs.append(t_stan_stif)
        sign += 1
        # print(sign)
        # print(t_stan_relation)
        if sign % 1000 == 0:  # 符合条件，多线程存储
            print('存储数据')
            threads = []
            for ind, dat in enumerate(all_data):
                if len(eval(dat)):
                    print(dat)
                    thr = threading.Thread(target=savedata.write_to_csv,args=(eval(dat), all_table_name[ind]))
                    thr.start()
                    threads.append(thr)
                    # savedata.write_to_csv(eval(dat), all_table_name[ind])

            for t in threads:
                t.join()
            sign = 0

            for data in all_data:  # 清空已写入数据
                eval(data).clear()

    if sign > 0:
        print('存储剩余数据')
        threads = []
        for ind, dat in enumerate(all_data):
            if eval(dat):
                thr = threading.Thread(target=savedata.write_to_csv, args=(eval(dat), all_table_name[ind]))
                thr.start()
                threads.append(thr)
                # savedata.write_to_csv(eval(dat), all_table_name[ind])

        for t in threads:
            t.join()
        sign = 0

        for data in all_data:  # 清空已写入数据
            eval(data).clear()