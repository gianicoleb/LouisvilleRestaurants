import csv
import matplotlib.pyplot as plt

# Load data from CSV file
with open('restaurant_data.csv') as f:
    reader = csv.DictReader(f)
    restaurants = list(reader)

# Get user's zip code
user_zip = input("Enter your zip code: ")

# Calculate average score for all restaurants and for each zip code
all_scores = [int(r['Score']) for r in restaurants]
zip_scores = {}
for r in restaurants:
    if r['Zip'] not in zip_scores:
        zip_scores[r['Zip']] = [int(r['Score'])]
    else:
        zip_scores[r['Zip']].append(int(r['Score']))
zip_avgs = {zip_code: sum(scores) / len(scores) for zip_code, scores in zip_scores.items()}
user_avg_score = sum(zip_scores.get(user_zip, [])) / len(zip_scores.get(user_zip, []))

# Create bar chart comparing scores
fig, ax = plt.subplots()
ax.bar(zip_avgs.keys(), zip_avgs.values())
ax.set_title('Average Scores of Restaurants by Zip Code')
ax.set_xlabel('Zip Code')
ax.set_ylabel('Score')
ax.axhline(y=user_avg_score, color='red', linestyle='--', label='Your Zip Code')
ax.legend()
plt.show()
