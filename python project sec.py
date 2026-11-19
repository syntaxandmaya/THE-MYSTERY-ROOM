print("====================================")
print("         THE MYSTERY ROOM")
print("       CASE 001: MISSING PHONE")
print("====================================")

print("\nWELCOME, DETECTIVE!")
print("\nZaynn's phone went missing during lunch break.")
print("Three students were present near the classroom.")
print("Your mission is to solve the mystery!")

input("\nPress ENTER to read the case...")

# CASE STORY
print("\n========== CASE STORY ==========")

print("\nZaynn left his phone on his classroom desk")
print("before going to the canteen at 1:00 PM.")

print("\nWhen he returned at 1:30 PM,")
print("his phone was missing.")

input("\nPress ENTER to meet the suspects...")

# SUSPECTS
print("\n========== SUSPECTS ==========")

print("\n1. ZARA")
print("She says: I was reading a book in the library.")

print("\n2. AARON")
print("He says: I was playing in the playground.")

print("\n3. INAYAT")
print("She says: I borrowed Zaynn's notebook")
print("and returned it to his desk.")

input("\nPress ENTER to inspect the evidence...")

# EVIDENCE
print("\n========== EVIDENCE ROOM ==========")

print("\nCLUE 1:")
print("Zaynn's notebook was found on his desk.")

print("\nCLUE 2:")
print("A classroom camera showed Inayat")
print("returning the notebook at 1:20 PM.")

print("\nCLUE 3:")
print("Zaynn received a message at 1:25 PM.")
print("The message said:")
print("'I have your phone. You left it in the library.'")

print("\nCLUE 4:")
print("Zaynn checked the library and found his phone.")

input("\nPress ENTER to start the investigation...")

# INVESTIGATION
score = 0

print("\n========== DETECTIVE QUIZ ==========")

# QUESTION 1
print("\nQ1. Where did Zaynn leave his phone?")
print("A. Classroom")
print("B. Canteen")
print("C. Library")

ans = input("Your answer: ")

if ans.upper() == "A":
    print("Correct! The phone was left in the classroom.")
    score += 10
else:
    print("Incorrect! Check the case story again.")

# QUESTION 2
print("\nQ2. Who returned Zaynn's notebook?")
print("A. Zara")
print("B. Aaron")
print("C. Inayat")

ans = input("Your answer: ")

if ans.upper() == "C":
    print("Correct! Inayat returned the notebook.")
    score += 10
else:
    print("Incorrect! Check the classroom camera clue.")

# QUESTION 3
print("\nQ3. What did the message say?")
print("A. The phone was stolen.")
print("B. The phone was in the library.")
print("C. The phone was in the canteen.")

ans = input("Your answer: ")

if ans.upper() == "B":
    print("Correct! The message mentioned the library.")
    score += 10
else:
    print("Incorrect! Read Clue 3 again.")

# QUESTION 4
print("\nQ4. Was Zaynn's phone actually stolen?")
print("A. Yes")
print("B. No")

ans = input("Your answer: ")

if ans.upper() == "B":
    print("Correct! Zaynn had simply misplaced his phone.")
    score += 10
else:
    print("Incorrect! Check the final evidence.")

# FINAL REPORT
print("\n====================================")
print("          CASE REPORT")
print("====================================")

print("\nInvestigation completed!")
print("Your score:", score, "/ 40")

if score == 40:
    print("Rank: MASTER DETECTIVE!")
elif score >= 20:
    print("Rank: JUNIOR DETECTIVE!")
elif score >= 10:
    print("Rank: DETECTIVE IN TRAINING!")
else:
    print("Rank: ROOKIE DETECTIVE!")

print("\nCASE SOLVED!")
print("Zaynn's phone was found in the library.")
print("\nThank you for playing!")
print("====================================")
