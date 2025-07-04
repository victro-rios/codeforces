import sys
import threading

def main():
    input = sys.stdin.readline

    num_lines = int(input())  # number of test cases
    lines = []
    for _ in range(num_lines):
        lines.append(str(input()))
    print(get_result(num_lines, lines))

def get_result(num_lines, lines):
    result = 0
    for i in range(num_lines):
        line = lines[i]
        if line.find('+') > -1:
            result += 1
        elif line.find('-') > -1:
            result -= 1
    return result
        

if __name__ == "__main__":
    threading.Thread(target=main).start()