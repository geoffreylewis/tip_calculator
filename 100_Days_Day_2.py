##################
# Tip Calculator #
##################

# Greeting
print("Welcome to the \"Tip Calculator\".  Do you dislike having to calculate the tip in your head after eating out somewhwere and then figuring out how much you REALLY will be dropping on the meal?\n")
print("Well, I got you covered.\n")

# Questions
bill_before_tip = int(input("First question: What's the total damage (before or after tax, your choice)?  *NOTE: Only type the number and not the \"$\" sign, please.\n"))
people_splitting = int(input("Second question: How many people are splitting the bill including yourself?  *NOTE: Only type a number and not a word, please.\n"))
tip_possibility = int(input("Third and final question: Do you want to leave 15%, 20%, or 25% tip?  *NOTE: Only type the number and not the \"%\" sign, please.\n"))

# New Calculated Values
share_of_bill = round(bill_before_tip / people_splitting, 2)
tip = round((tip_possibility / 100) * share_of_bill, 2)
total_damage = round(share_of_bill + tip, 2)

# Tip and Total Bill (using f-String)
print()
print(f"Well, your share of the bill is ${share_of_bill}; with a tip of ${tip} added on, the total damage looks to be ${total_damage} when this meal is said and done.  ...Lucky you.")