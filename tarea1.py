harina=int(input("cuantos gramos de harina vas a usar?"))
agua_tazas=int(input("cuantas tazas de agua vas a usar?"))
agua_gramos=agua_tazas*250
masa=harina+agua_gramos
arepas=masa//50
print('vas a tener',masa,'g de masa, que son aproximadamente',arepas,'arepas')