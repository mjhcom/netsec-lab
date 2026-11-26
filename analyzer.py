import os
import re
def analyze_log(filepath):
    ip_counts = {}
    fail_count = 0
    try:
        with open(filepath, 'r', encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
                match = re.search(pattern, line)
                if match:
                    ip = match.group()
                    ip_counts[ip] = ip_counts.get(ip, 0) + 1
                if "Failed" in line:
                    fail_count += 1
        sorted_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)
        if sorted_ips:
            return sorted_ips[0][0], sorted_ips[0][1], fail_count
        return None, None, fail_count
    except Exception as e:
        print(f"分析{filepath}出错：{e}")
        return None, None, fail_count