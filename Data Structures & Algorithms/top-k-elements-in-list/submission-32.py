
def top_k(nums: list, k: int) -> list:
    counts = defaultdict(int)
    for n in nums:
        counts[n] += 1
    return [n for n, _ in sorted(counts.items(), key=lambda x: -x[1])[:k]]