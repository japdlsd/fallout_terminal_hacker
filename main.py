import sys
import itertools
import logging
import functools

@functools.lru_cache()
def dist(a, b):
    assert(len(a) == len(b))
    res = 0
    for i in range(len(a)):
        if a[i] == b[i]: res += 1
    return res

def average_shrinking(words):
    if len(words) == 0: return None
    res = {word: None for word in words}
    for chosen_word in words:
        counts = []
        for target_word in words:
            target_dist = dist(target_word, chosen_word)
            eradicated_words_count = len([word for word in words if dist(word, chosen_word) != target_dist])
            counts.append(eradicated_words_count)
        res[chosen_word] = sum(counts)/len(counts)
    return res


def next_step(words):
    if len(words) == 0: return None
    av_shrinking = average_shrinking(words)
    logging.debug(str(av_shrinking))
    best_pos = words[0]
    for word in words:
        if av_shrinking[best_pos] < av_shrinking[word]:
            best_pos = word
    return best_pos

def main():
    logging.basicConfig(level=logging.DEBUG)

    words = []
    buffer = "____"
    while True:
        buffer = input()
        if buffer == "": break
        words.append(buffer.strip())

    buffer = "____"
    while True:
        step = next_step(words)
        print("STEP: \"{}\"".format(step))
        if buffer == "y": return
        target_dist = int(input("dist: "))
        words = [word for word in words if dist(word, step) == target_dist]


if __name__ == "__main__":
    main()