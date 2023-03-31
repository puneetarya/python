from box import Phone, Charger, Earphones, Box

phone_case_contents = []
phone_case_contents.append(Phone(200))
phone_case_box = Box(phone_case_contents)

big_box_contents = []
big_box_contents.append(phone_case_box)
big_box_contents.append(Charger(10))
big_box_contents.append(Earphones(10))
big_box = Box(big_box_contents)

print("Total price: " + str(big_box.return_price()))