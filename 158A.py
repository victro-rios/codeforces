import sys
import threading

def main():
    input = sys.stdin.readline

    line = str(input())
    n_str, k_str = line.split(' ');
    n = int(n_str)
    k = int(k_str)
    nums_str = str(input()).split(' ')
    nums = [-1]
    for num in nums_str:
        nums.append(int(num))
    print(get_participants_passing(n, k, nums))

def get_participants_passing(n, k, participant_scores):
    participants_passing = 0
    min_threshold = participant_scores[k]
    for participant_score in participant_scores:
        if participant_score > 0 and participant_score >= min_threshold:
            participants_passing += 1
    return participants_passing


if __name__ == "__main__":
    threading.Thread(target=main).start()