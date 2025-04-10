import pathlib 
file = pathlib.Path("mindenKarakter")
text = []
n = 129979 #111411  129979

for i in range(0,n):
    if 0xD800 <= i <= 0xDFFF:
        continue
    try:
        text.append(f"{chr(i)} - {i}")
        try:
            if i % 100 == 0:
                print(f"{i / n * 100:.2f}%")
        except:
            pass
    except:
        pass
file.write_text(" ,".join(text))
print(" ,".join(text))