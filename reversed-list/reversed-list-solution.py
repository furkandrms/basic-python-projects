def reverse_list(lst):
    """
    Verilen listedeki elemanları tersine döndürür ve içindeki listelerin elemanlarını da tersine döndürür.
    """
    reversed_lst = []
    for item in lst:
        if type(item) == list:
            reversed_lst.append(reverse_list(item))
        else:
            reversed_lst.append(item)
    return list(reversed(reversed_lst))

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

# Liste elemanlarını tersine çevirin ve yazdırın
reversed_list = reverse_list(user_list)
print("Tersine çevrilmiş liste:", reversed_list)
