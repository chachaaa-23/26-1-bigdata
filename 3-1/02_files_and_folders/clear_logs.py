import os
import shutil

# Make one logs folder inside the example folder.
base_dir = os.path.dirname(__file__)
work_dir = os.path.join(base_dir, "_generated")
logs_dir = os.path.join(work_dir, "logs")
old_log_path = os.path.join(logs_dir, "old.log")

# Make an old log file first.
os.makedirs(logs_dir, exist_ok=True)

#with 문: 내부 구문 실행 후 자동 닫힘. 
with open(old_log_path, "w", encoding="utf-8") as f:
    f.write("Old log")

print(os.path.exists(old_log_path))

print()

# Clear the whole logs folder.
shutil.rmtree(logs_dir)

# Make a new empty logs folder.
os.makedirs(logs_dir)

print(os.path.exists(logs_dir))
print(os.listdir(logs_dir))
