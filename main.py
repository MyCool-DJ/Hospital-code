empty = 25
new_patients = 23

if new_patients <= empty:
    empty = empty - new_patients
    print(f"{empty} rooms are empty")
