#1.list of Superheros representing the justice league
justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]

# Step 1: Count the number of members
print("Initial Justice League:", justice_league)
print("Number of members:", len(justice_league))

#2.Batman recruited Batgirl and Nightwing as new members
# Add new members to the list
justice_league.append("Batgirl")
justice_league.append("Nightwing")

print("After adding Batgirl and Nightwing:", justice_league)

#3.wonder women is now lwader of the league
# Remove Wonder Woman and insert at the beginning
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")

print("After making Wonder Woman the leader:", justice_league)

#4.Separate Aquaman and flash with Another Hero
# Remove Green Lantern from the end (since it's currently last)
justice_league.remove("Green Lantern")

# Find the positions of Aquaman and Flash
index_flash = justice_league.index("Flash")
index_aquaman = justice_league.index("Aquaman")

# Insert Green Lantern between them
# We want to insert at the position just after Aquaman
justice_league.insert(index_aquaman + 1, "Green Lantern")

print("After placing Green Lantern between Aquaman and Flash:", justice_league)

#5.Replace the Entire Justice League with a New Team
#["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
# Replace the entire list with a new team
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]

print("After replacing with new team:", justice_league)

#6.Sort Alphabetically and Identify the New Leader
# Sort the list alphabetically
justice_league.sort()

print("After sorting alphabetically:", justice_league)
print("The new leader is:", justice_league[0])
