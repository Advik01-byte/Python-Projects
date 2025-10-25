import cowsay as cow
import time

start_time = time.perf_counter()

# Print a cow saying "Good Mooooorning!"
cow.cow("Good Mooooorning!")

# Print a dragon saying "Python is awesome!"
cow.dragon("Python is awesome!")

# Print a turtle saying "Keep calm and code on!"
cow.turtle("Keep calm and code on!")

end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Time taken by above code is {elapsed_time}")
