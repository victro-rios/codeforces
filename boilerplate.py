import sys
import threading

def main():
    input = sys.stdin.readline

    t = int(input())  # number of test cases
    for _ in range(t):
        solve(input)

def solve(input):
    # Example: read n and an array of size n
    n = int(input())
    arr = list(map(int, input().split()))

    # Your solution here
    print(f"Example output: {arr}")

if __name__ == "__main__":
    threading.Thread(target=main).start()