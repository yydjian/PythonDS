import torch
print(torch.__version__)
print(torch.cuda.is_available())  # Vérifie si CUDA est dispo


import torch

# Création d’un tenseur 1D (vecteur)
a = torch.tensor([1.0, 2.0, 3.0])

# Création d’un autre vecteur
b = torch.tensor([4.0, 5.0, 6.0])

# Addition élément par élément
somme = a + b

# Multiplication élément par élément
produit = a * b

# Produit scalaire
dot = torch.dot(a, b)

# Affichage
print("a :", a)
print("b :", b)
print("Somme :", somme)
print("Produit :", produit)
print("Produit scalaire :", dot)


