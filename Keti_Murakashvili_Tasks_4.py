# Tasks 4 - 1
def info():
    first_name = input("Enter Name: ")
    last_name = input("Enter Lastname: ")
    age = input("Enter Age: ")
    return [first_name, last_name, age]
user1 = info()
user2 = info()
user3 = info()
consumer_info = [user1, user2, user3]
user_index = int(input("ჩაწერე ინდექსი x (0, 1, or 2): "))
user = consumer_info[user_index]
print(f"Name: {user[0]}")
print(f"Lastname: {user[1]}")
print(f"Age: {user[2]}")

#2
actors_info = [
    {"სახელი": "სკარლეტ", "გვარი": "იოჰანსონი", "ასაკი": 39, "ფილმები": ["Avengers", "Lost in Translation", "Lucy"]},
    {"სახელი": "მერილ", "გვარი": "სტრიპი", "ასაკი": 74, "ფილმები": ["The Iron Lady", "Mamma Mia!", "Kramer vs. Kramer"]},
    {"სახელი": "ტომ", "გვარი": "ჰენკსი", "ასაკი": 67, "ფილმები": ["Forrest Gump", "Saving Private Ryan", "Cast Away"]}
]
def find_actor(name):
    for actor in actors_info:
        if actor["სახელი"] == name or actor["გვარი"] == name:
            return actor
    return None
user_input = input("შემოიტანე მსახიობის სახელი ან გვარი: ")
actor_found = find_actor(user_input)
if actor_found:
    print(f"სახელი: {actor_found['სახელი']} {actor_found['გვარი']}")
    print(f"ასაკი: {actor_found['ასაკი']}")
    print("ფილმები: " + ", ".join(actor_found["ფილმები"]))
else:
    print("ეს მსახიობი სიაში არ იძებნება.")

#3
def unique_list():
    input_list = input("შემოიტანე ელემენტები: ").split()
    unique_set = set(input_list)
    unique_list = list(unique_set)
    return unique_list
print("უნიკალური სია:", unique_list())

#4
def tuple1():
    set1_input = input("pirveli setis elementebi: ")
    set1 = set(set1_input.split())
    set2_input = input("meore setis elementebi: ")
    set2 = set(set2_input.split())
    combined_set = set1.union(set2)
    combined_tuple = tuple(combined_set)
    return combined_tuple
result = tuple1()
print("gaertianebuli:", result)

#5
def carieliaa(dictionary):
    return len(dictionary) == 0
input_dict = input("shemoitane elementebi (key1:value1): ")
if input_dict:
    dict_elements = input_dict.split()
    user_dict = {k: v for k, v in (element.split(':') for element in dict_elements)}
else:
    user_dict = {}
if carieliaa(user_dict):
    print("carielia.")
else:
    print("araa carieli.")  #mgoni ase unda iyos ¿

#6
def mtvleli(input_string):
    char_count = {}
    for char in input_string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
input_string = input("chawere striqoni: ")
character_count = mtvleli(input_string)
print("simbolobis raodenoba:", character_count)
