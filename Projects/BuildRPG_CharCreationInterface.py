full_dot = '●'
empty_dot = '○'
refresh=0

def create_character(name="ハルジオン",strength=1,intel=2,charisma=4):

    #Char Name verification
    if not isinstance(name,str):
        return("The character name should be a string")
    if not name:
        return("The character should have a name")
    if len(name) > 10:
        return("The character name is too long")
    if " " in name:
        return("The character name should not contain spaces")

    #Char stats verification
    if not (isinstance(strength,int) and isinstance(intel,int) and isinstance(charisma,int)):
        return("All stats should be integers")
    if strength  < 1 or intel  < 1 or charisma  < 1:
        return("All stats should be no less than 1")
    if strength  > 4 or intel  > 4 or charisma  > 4:
        return("All stats should be no more than 4")
    if strength + intel + charisma != 7:
        return("The character should start with 7 points")


    #Final Output
    return(f"""{name}
STR {(full_dot)*strength}{(empty_dot)*(10-strength)}
INT {(full_dot)*intel}{(empty_dot)*(10-intel)}
CHA {(full_dot)*charisma}{(empty_dot)*(10-charisma)}""")

input_name = input("Enter your character's name: ")
input_strength = int(input("Enter your character's strength (1-4): "))
input_intel = int(input("Enter your character's intelligence (1-4): "))
input_charisma = int(input("Enter your character's charisma (1-4): "))
print(create_character(input_name,input_strength,input_intel,input_charisma))
print("""


""")
name = "Bill"


print(f"""
{name}
STR {(full_dot+" ")*7}"

""")

print(" What is the role of a Data Analyst")
user_role = "Data Analyst"
weekly_hours = 35
project_name = "Alpha"

# Notice the f sits right before the triple quotes
dashboard_summary = f"""
--- WEEKLY REPORT ---
Role: {user_role}
Hours logged: {weekly_hours} hours
Current Target: Project {project_name.upper()}
---------------------
"""

print(dashboard_summary)

