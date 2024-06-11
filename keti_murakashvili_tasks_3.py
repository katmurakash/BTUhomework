#დავალება 3, ამოცანა 1
def triple_input():
    a = input("ჩაწერე ინფორმაცია გასამმაგებისთვის : ")
    tripledtext = a * 3
    print(f"გასამმაგებული : {tripledtext}")
triple_input()

#დავალება 3, ამოცანა 2
def momxmareblis_wona():
    wona = int(input("ჩაწერე მომხმარებლის წონა : "))
    mtvariswona = wona / 6
    print(f"მთვარის გრავიტაციის დროს წონა : {mtvariswona}")
momxmareblis_wona()

#დავალება 3, ამოცანა 3
def calculator():
    user_input = input("ჩაწერე გამოსახულება : (მაგ: 2 * 6) :  ")
    parts = user_input.split()
    if len(parts) != 3:
        return "გთხოვთ ჩაწეროთ 3 ელემენტიანი გამოსახულება მაგალითის მსგავსად"
    num1_str, operator, num2_str = parts
    try:
        num1=float(num1_str)
        num2=float(num2_str)
    except ValueError:
        return "გთხოვთ ჩაწეროთ რიცხვები"
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "ნულზე გაყოფა არ შეიძლება"
        else:
            return num1 / num2
    elif operator == '^':
        return num1 ** num2
    else:
        return "გთხოვთ შეიტანოთ მისაღები ოპერატორი (+, -, *, /, ^)"
pasuxi = calculator()
print(pasuxi)






