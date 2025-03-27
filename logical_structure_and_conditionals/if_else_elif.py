
age = 3

"""
If conditional structure in C

if(age < 18){
    printf("Underage");
}else if (age == 18){
    printf("Of age");
}else (age < 18){
    printf("Of age");
}

"""

if age < 21:
    print("Underage")
elif age == 18:
    print("Is 18 years old")
else:
    print("Of age")
