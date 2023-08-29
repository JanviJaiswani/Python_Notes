import multiprocessing

# Function to print a message multiple times
def print_message(message, times):
    for i in range(times):
        print(message)

if __name__ == "__main__":
    # Create two processes
    p1 = multiprocessing.Process(target=print_message, args=("Hello", 5))
    p2 = multiprocessing.Process(target=print_message, args=("World", 5))

    # Start both processes
    p1.start()
    p2.start()

    # Wait for both processes to finish
    p1.join()
    p2.join()

    print("All processes are complete.")
