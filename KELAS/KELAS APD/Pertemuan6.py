import os
os.system('cls' if os.name == 'nt' else 'clear')

hewan = {"gajah", "harimau", "zebra","monyet", "ayam"}
print(hewan) 
info = {
    "nama": "Nuril Akmal",
    "umur": 19,
    "asal": "Samarinda",
    "status": True
     
}
print(info)
print(info["nama"])
print(info["umur"])
for key in info:
    print(f'{key} : {info[key]}')
    
    

                            
