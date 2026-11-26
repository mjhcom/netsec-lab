import sys
from analyzer import analyze_log
if len(sys.argv) < 2:
    print("用法：python main.py 【日志文件路径】")
    sys.exit(1)
filepath = sys.argv[1]
top_ip, top_count, fail_count = analyze_log(filepath)
if top_ip:
    print(f"【{filepath}】Top IP:{top_ip}, Count:{top_count}，登录失败:{fail_count}")
else:
    print(f"没有分析出结果，失败登录：{fail_count}")