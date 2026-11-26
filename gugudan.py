dan = int(input("출력할 단을 입력하세요: "))

print(f"--- {dan}단 ---")
for num in range(1, 10):
  print(f"{dan} x {num} = {dan * num}")