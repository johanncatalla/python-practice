apples = int(input(" how many apples are bought? "))

dozen = apples // 12   #floor division to find ints
indiv = apples % 12    # modulus to find remaining 
hm1 = dozen * 100      #hm stands for "how many" 
hm2 = indiv * 10
sum = hm1 + hm2

print("That is %d dozens and %d pieces" % (dozen , indiv))
print("The total amount is P%d" % sum)