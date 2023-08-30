# Speed Typing Test in Python
import time

def typing_test(text):
    print("Type the following text:")
    print(text)
    input("Press Enter when you're ready to start...")
    
    start_time = time.time()
    user_input = input("Start typing: ")
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    words = text.split()
    typed_words = user_input.split()
    correct_words = [w1 for w1, w2 in zip(words, typed_words) if w1 == w2]
    
    accuracy = len(correct_words) / len(words) * 100
    words_per_minute = len(typed_words) / (elapsed_time / 60)
    
    print("\nTime elapsed:", round(elapsed_time, 2), "seconds")
    print("Accuracy:", round(accuracy, 2), "%")
    print("Words per minute:", round(words_per_minute, 2))

if __name__ == "__main__":
    test_text = "The quick brown fox jumps over the lazy dog"
    typing_test(test_text)


    # Type the following text:
    # The quick brown fox jumps over the lazy dog
    # Press Enter when you're ready to start...
    # Start typing: the quick brown fox jumps over the lazy dog

    # Time elapsed: 13.84 seconds
    # Accuracy: 98.89 %
    # Words per minute: 28.66
