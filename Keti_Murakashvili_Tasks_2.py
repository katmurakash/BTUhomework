# დავალება 2 ამოცანა 1
def quiz():
    print("რომელი იმპერიის მიერ აგებულ წყალ-მომარაგების სისტემა (აკვედუკი) ფუნქიციონირებს დღესაც? ")
    print("სავარაუდო პასუხები:")
    print("1. შუმერთა")
    print("2. სელჩუკთა")
    print("3. რომის")
    print("4. მონღოლთა")
    pasuxi = "რომის"
    user_answer = input("აირჩიე პასუხი (1, 2, 3 ან 4) : ")
    if user_answer == "3" or user_answer.lower() == pasuxi.lower():
        print("სწორია!")
    else:
        print(f'არა! სწორი პასუხია {pasuxi} !')
quiz()
#2
laptops = ["Dell", "MacBook Air", "Lenovo Yoga"]
personal_computers = ["HP Pavilion Desktop", "Dell Inspiron Desktop", "Lenovo ThinkCentre"]
mobile_phones = ["iPhone 12", "Redmi Note 8", "Google Pixel 6"]
categories = {
    1: laptops,
    2: personal_computers,
    3: mobile_phones
}
def offer_products(category, budget):
    products = categories.get(category, [])
    if not products:
        print("არაა ასეთი პროდუქტი")
        return
    affordable_products = [product for product in products if product_budget.get(product, float('inf')) <= budget]
    if not affordable_products:
        print("ამ თანხაში არ გაგვაჩნია შემოთავაზება.")
        return
    print("პროდუქტები თქვენი ბიუჯეტის მიხედვით:")
    for product in affordable_products:
        print("-", product)
print("აირჩიე კატეგორია:")
print("1. ლეპტოპები")
print("2. პერსონალური კომპიუტერები")
print("3. მობილური ტელეფონები")
category_choice = int(input("ჩაწერე კატეგორიის ციფრი: "))
max_budget = float(input("შენი ბიუჯეტი: "))
product_budget = {
    "Dell": 1500,
    "MacBook Air": 1200,
    "Lenovo Yoga": 1300,
    "HP Pavilion Desktop": 800,
    "Dell Inspiron Desktop": 700,
    "Lenovo ThinkCentre": 900,
    "iPhone 12": 1000,
    "Redmi Note 8": 900,
    "Google Pixel 6": 800
}
offer_products(category_choice, max_budget)

#3
print("ქვესთი დაიწყო!")
player = input("შენი სახელი? ")
print(f"Welcome, {player}! ამ საღამოს უნდა იპოვო დაკარგული განძი.")
print("ხარ გზაჯვარდენიზე, წადი მარცხნივ ან მარჯვნივ ბნელ ტყეში.")
choice1 = input("გაყვები ბნელ გზას? (კი/არა): ")
if choice1 == "კი":
    print("შენ შეხვედი ტყეში.")
    print("ხედავ მოციმციმე ტბას.")
    print("ქვევიდან ციმციმებს, ფსკერზე რაღაც ღირებულია, იქნებ ეს განძია?.")
    choice2 = input("ჩაყვინთავ? (კი/არა): ")
    if choice2 == "კი":
        print("ღრმად ჩაისუნთქე და წყალში ჩაყვინთე")
        print("ხედავ სკივრს!")
        print("გააღებ სკივრს და აღმოაჩენ განძს.")
        print("გილოცავ!")
        print("You WIN!")
    elif choice2 == "არა":
        print("არ გარისკე.")
        print("გააგრძელე ტყეში სვლა.")
        print("გზად შეხვდი ტყის ბინადრებს, რომლებმაც სკივრამდე გზა მიგასწავლეს")
        print("სკივრი იპოვე.")
        print("ცარიელი აღმოჩნდა!")
        print("BETTER LUCK NEXT TIME HAHA, YOU LOST! ")
elif choice1 == "არა":
    print("გადაწყვიტე არ გაყოლოდი ტყისკენ მიმავალ გზას.")
    print("არჩეულ გზაზე იპოვე ციხესიმაგრე.")
    choice3 = input("გინდა შეხვიდე? (კი/არა): ")
    if choice3 == "კი":
        print("უბრალოდ მიტოვებული ციხესიმაგრეა.")
        print("YOU LOST!")
    elif choice3 == "არა":
        print("გააგრძელე გზა და იპოვე მინიშნება ")
        print("გაგრძელება იქნნება")