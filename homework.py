import random
slotssymbols=["Cherry","Cherry","Lemon","Lemon","Orange","Orange","Bell","Seven"]
slot1=random.choice(slotssymbols)
slot2=random.choice(slotssymbols)
slot3=random.choice(slotssymbols)
print(slot1,slot2,slot3)
if(slot1==slot2==slot3):print("Jackpot!!!")