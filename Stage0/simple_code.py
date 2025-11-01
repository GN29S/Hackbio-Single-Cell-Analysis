# Define the team profile data
team_profile = [
    ["Ghizal Niko", "@Ghizal N.", "Germany", "Reading", "Munich University", "lacZ gene", "ATGACCATGATTACGGATTC"],
    ["Vilvian Anunda", "@Vil", "Kenya", "Cooking", "University of Nairobi", "tfdA gene", "ATGACGCTGACCTTCCATGA"],
    ["Rama Vijaya Jhowry", "@Rama Jhowry", "Indonesia", "Tasting food", "IPB University", "ggox gene", "ATGAAGAACTATCCTCTCCAG"],
    ["Onyinye Vivian", "@xoxo, Vivianne", "Nigeria", "Watching movies", "FUTO", "HBB gene", "ATGGTGCACCTGACTCCTGA"],
    ["Sreenidhi Vasudevan", "@Sreenidhi Vasudevan", "India", "Drawing", "Anna University", "SMN1 gene", "GCACCCGCGGGTTTGCTATG"],
    ["Akash Madhusudhan", "@V.S.Akash", "India", "Carnatic Music", "Anna University", "HMGCR gene", "ATGGCCCGCGGGCGCGCGG"],
    ["Temitope Olajide", "@Temitope Olajide", "Liberia", "Reading", "William V.S. Tubman University", "F8 gene", "ATCGCTGTGATGTTTTGACC"]
]

# Function to print a single team member's profile
def print_team_member_profile(member_data):
    """Prints the name, slack username, country, hobby, affiliation, and gene DNA sequence for a team member."""
    name = member_data[0]
    slack_username = member_data[1]
    country = member_data[2]
    hobby = member_data[3]
    affiliation = member_data[4]
    gene_sequence = member_data[6] # Accessing the gene DNA sequence at index 6

    print(f"Name: {name}")
    print(f"Slack Username: {slack_username}")
    print(f"Country: {country}")
    print(f"Hobby: {hobby}")
    print(f"Affiliation: {affiliation}")
    print(f"Gene DNA Sequence: {gene_sequence}")
    print("-" * 20) # Print a separator for readability

# Main section to iterate through the team profile and print each member's information
if __name__ == "__main__":
    for team_member in team_profile:
        print_team_member_profile(team_member)
