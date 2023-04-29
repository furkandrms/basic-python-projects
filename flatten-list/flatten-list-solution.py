def flatten(l):
    """
    Verilen çok katmanlı listedeki elemanları tek katmanlı bir listeye düzleştirir.
    """
    # Çıktı listesini başlat
    flattened_list = []
    
    # Her öğe için
    for item in l:
        # Eğer öğe bir liste ise, listenin öğelerini düzleştir
        if type(item) == list:
            flattened_list.extend(flatten(item))
        else:
            # Eğer öğe bir liste değilse, çıktı listesine ekle
            flattened_list.append(item)
    
    return flattened_list

# Kullanıcıdan bir liste isteyin
user_input = input("Lütfen bir liste girin: ")

# Girdiyi virgüllerle ayrılmış öğelerine ayırın ve liste haline getirin
user_list = user_input.split(",")

# Elemanların türlerini uygun şekilde değiştirin
for i in range(len(user_list)):
    if user_list[i] == "None":
        user_list[i] = None
    elif user_list[i].isdigit():
        user_list[i] = int(user_list[i])
    else:
        user_list[i] = user_list[i].strip()

# Düzleştirilmiş listeyi yazdırın
flattened_list = flatten(user_list)
print("Düzleştirilmiş liste:", flattened_list)
