facebook = input("Does the person have a Facebook account? (yes/no): ").lower() == 'yes'
twitter = input("Does the person have a Twitter account? (yes/no): ").lower() == 'yes'
instagram = input("Does the person have an Instagram account? (yes/no): ").lower() == 'yes'

# Check if the person can be a good influencer
if facebook + twitter + instagram >= 2:
    print("This person can be a good influencer!")
else:
    print("This person may not have enough social media presence to be a good influencer.")