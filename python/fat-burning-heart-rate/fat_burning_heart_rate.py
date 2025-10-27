# Fat-buring heart rate
# Author: Antonio Olivares Ramirez

# This program calculates and adult's fat-burning heart rate, which is 70% of 220
# minus the person's age.
# the adult must be between the ages of 18 and 75 inclusive.

MIN_AGE = 18
MAX_AGE = 75

def get_age():
    age = int(input())
    # Code block raises error when outside of valid age range
    if age < MIN_AGE or age > MAX_AGE:
        raise ValueError("Invalid age.")
    return age

# Calculates fat burning rate based on valid age
def fat_burning_heart_rate(age):
    return 0.70 * (220 - age)
    

if __name__ == "__main__":
    # Calls get age and fat burning rate functions.
    # Handles the exception. 
    try:
        age = get_age()
        heart_rate  = fat_burning_heart_rate(age)
    
        print("Fat burning heart rate for a", (age), "year-old:", int(heart_rate), "bpm")
    
    
    except ValueError as exc:
        print(exc)
        print("Could not calculate heart rate info.")
    