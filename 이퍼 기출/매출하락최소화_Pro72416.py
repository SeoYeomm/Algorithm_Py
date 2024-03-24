from collections import defaultdict

def init(links) :
    edge_dict = defaultdict(list)
    
    for a, b in links :
        edge_dict[a].append(b)
        
    return edge_dict # 팀장-팀원들 

def dfs(node, edge_dict, dp) :
    if not edge_dict[node] : # 팀원들이 없으면 
        return
    
    cnt, zero_cnt, min_val, min_diff = 0, 0, 0, float('inf')
    # 팀원들 수, 불참한 팀원의 수, 누적 값, 팀장 불참시 매출 차이 
    
    for leaf in edge_dict[node] : # leaf = 팀원들 
        dfs(leaf, edge_dict, dp)
        
        min_val += min(dp[leaf])
        cnt += 1
        
        # 해당 팀원이 불참할 경우의 수를 계산
        if dp[leaf][0] < dp[leaf][1] :
            zero_cnt += 1
            min_diff = min(min_diff, dp[leaf][1] - dp[leaf][0])
            # 팀원이 참석(1)했을 때와 불참(0)했을 때 최소 값 구하기 
            
    dp[node][1] += min_val # 팀장 참여
    dp[node][0] += min_val + min_diff if cnt == zero_cnt else min_val # 팀장 참여X

def solution(sales, links):
    dp = [[0,0]] + [[0, sale] for sale in sales]
    
    edge_dict = init(links)
    dfs(1, edge_dict, dp)
    return min(dp[1])
