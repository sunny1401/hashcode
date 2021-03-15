# Given n processes, each process has a unique PID (process id) and its PPID (parent process id).
#
# Each process only has one parent process, but may have one or more children processes. This is just like a tree
# structure. Only one process has PPID that is 0, which means this process has no parent process. All the PIDs will
# be distinct positive integers.
#
# We use two list of integers to represent a list of processes, where the first list contains PID for each process
# and the second list contains the corresponding PPID.
#
# Now given the two lists, and a PID representing a process you want to kill, return a list of PIDs of processes that
# will be killed in the end. You should assume that when a process is killed, all its children processes will be
# killed. No order is required for the final answer.

import copy
from typing import List


def killProcess(pid: List[int], ppid: List[int], kill: int) -> List[int]:
    process_dict = dict()
    for i in range(len(pid)):
        if ppid[i] not in process_dict:
            process_dict[ppid[i]] = {pid[i]}
        else:
            process_dict[ppid[i]].add(pid[i])

    if kill in process_dict[0]:
        return pid

    simple_process_set = set(pid)
    result = set()
    if kill not in process_dict:
        return [kill]
    else:
        result.add(kill)
        simple_process_set.remove(kill)
        v = process_dict[kill]
        while (v and len(v)):
            temp = set()
            for i in v:
                result.add(i)
                simple_process_set.remove(i)
                val = process_dict.get(i)
                if val:
                    for j in val:
                        temp.add(j)
            v = temp

        return list(result)
