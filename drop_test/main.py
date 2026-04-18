from pathlib import Path

def min_num_drops(n: int, h: int) -> int:
    if n == 0:
        return int("inf")
    if h == 0:
        return 0

    dp = [0] * (n + 1)
    t = 0

    while dp[n] < h:
        t += 1
        new_dp = [0] * (n + 1)
        for i in range(1, n + 1):
            new_dp[i] = dp[i - 1] + 1 + dp[i]
        dp = new_dp
    return t

def main():
    data = Path("input.txt").read_text(encoding="utf-8")
    for line in data.splitlines():
        line = line.strip()
        if not line:
            continue
        n_str, h_str = line.split(",")
        n, h = int(n_str.strip()), int(h_str.strip())
        print(min_num_drops(n, h))


if __name__ == "__main__":
    main()
