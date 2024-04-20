##################
# Tip Calculator #
##################

# Greeting
print("Welcome to the \"Tip Calculator\".  Do you dislike having to calculate the tip in your head after eating out somewhwere and then figuring out how much you REALLY will be dropping on the meal?\n")
print("Well, I got you covered.\n")

# Questions
bill_before_tip = input("First question: What's the total damage (before or after tax, your choice)?  *NOTE: Only type the number and not the \"$\" sign, please.\n")
people_splitting = input("Second question: How many people are splitting the bill including yourself?  *NOTE: Only type a number and not a word, please.\n")
tip_possibility = input("Third and final question: Do you want to leave 15%, 20%, or 25% tip?  *NOTE: Only type the number and not the \"%\" sign, please.\n")

# Tip and Total Bill
print()
print("Well, your share of the bill is $''; with a tip of $'' added on, the total damage looks to be $''.  ...Lucky you.")