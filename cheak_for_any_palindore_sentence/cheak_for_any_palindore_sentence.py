text_ = input("input yout text:-------")
text = list(text_)

new_list_for_lower_alphabets_only = []

for i in text:
    if i.isalpha():
        new_list_for_lower_alphabets_only.append(i.lower())

if new_list_for_lower_alphabets_only == new_list_for_lower_alphabets_only[-1::-1]:
    print(text_,"----->  True")
else:
    print(text_,"----->  False")