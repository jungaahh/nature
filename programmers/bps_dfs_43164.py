from collections import defaultdict


def solution(tickets):
    airports=defaultdict(list)
    needed_node=list()
    for src,tgt in tickets:
        airports[src].append(tgt)
    
    for air in airports.keys():
        airports[air].sort()

    needed_node.append(tickets[0])
    while needed_node:



if __name__=="__main__":
    tickets=[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
    answer=solution(tickets)
    print(answer)