import time
import random


words = []
WORDS = 20

for word in open("words.txt"):
    if word:
        words.append(word.replace("\n", ""))

if __name__ == "__main__":

    challenge_words = random.choices(words, k=WORDS)


    print("Hello, let's find out how fast you type.")
    print("Type in the words as they appear")
    input("Press enter to begin")
    print("Starting in...")
    for i in range(0, 3):
        print(3 - i)
        time.sleep(1)

    response_words = []
    failures = 0
    
    start = (int(time.time()))
    
    for i in range(len(challenge_words)):
        word_chunk = challenge_words[i:i+2 if i != len(challenge_words) - 1 else None]
        print("\033[90m", end="")
       
        if len(word_chunk) == 2:
            print(word_chunk[0])
            response = input(word_chunk[1] + "\033[A\r\033[93m")
        else:
            response = input(word_chunk[0] + "\r\033[93m")

        if (response == challenge_words[i]):
            print("\033[92m", end="")
        else:
            print("\033[91m", end="") 
            failures += 1

        print("\033[A\r" + response)

    
    end = (int(time.time()))
    diff = end-start

    print("\033[97mYour time was: %s seconds" % (diff))
    print("With %s failures, that gives a wpm of: %d" % (failures, (WORDS - failures) / diff * 60 ))

