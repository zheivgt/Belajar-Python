#Mengatur Format String
print ("Mengatur Format String")

#menggunakan posisi default
default_order = "{}, {} dan {}".format("Budi", "Galih", "Ratna")
print("\n--- Urutan default ---")
print(default_order)
print("\n")

#menggunakan argument posisi
positional_order = "{1}, {0} dan {2}".format("Budi", "Galih", "Ratna")
print ("\n--- Urutan berdasarkan posisi ---")
print(positional_order)