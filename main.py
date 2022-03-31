print("Hello World")
print("Kui sooritate ostu, mis on rohkem või võrdne 5000$, saate lisa soodustust!!")
kauba_valik = input("Sisestage kaup, mida soovite osta: ")
kauba_kogus = int(input("Sisestage kauba kogus: "))
asukoht = input("Sisestage State(ut, nv, tx, al, ca): ").upper()

if asukoht == "UT":
    asukoht = 0.0685
elif asukoht == "NV":
    asukoht = 0.08
elif asukoht == "TX":
    asukoht = 0.0625
elif asukoht == "AL":
    asukoht = 0.04
elif asukoht == "CA":
    asukoht = 0.0825