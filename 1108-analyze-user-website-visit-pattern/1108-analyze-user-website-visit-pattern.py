class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        # Step 1: 按 timestamp 排序
        data = sorted(zip(timestamp, username, website))  # 排序：保证访问顺序
        user_to_websites = defaultdict(list)

        # Step 2: 记录每个用户的访问顺序
        for _, user, site in data:
            user_to_websites[user].append(site)

        # Step 3: 统计所有用户的 3-website 访问模式
        pattern_count = Counter()

        for user, sites in user_to_websites.items():
            if len(sites) < 3: 
                continue  # 跳过访问不足 3 次的用户
            
            # 生成所有 3-website 组合 (去重)
            unique_patterns = set(combinations(sites, 3))  
            for pattern in unique_patterns:
                pattern_count[pattern] += 1

        # Step 4: 找到最高频，字典序最小的模式
        return min(pattern_count.keys(), key=lambda p: (-pattern_count[p], p))  # 按频率降序 + 字典序升序