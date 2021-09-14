class indoara:
    def transformaIndoAra(self, num):
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        numbers = list(num)
        indo_num = 0
        teste = ''
        for i in range(1,len(syb)):


            print(i + 1)
            if ((i + 1) == len(numbers)):
                teste = numbers[i] + numbers[i + 1]
            else:
                teste = numbers[i]


            if (teste in syb):
                print("in " + teste)
                num = num.replace(teste, '')
                indo_num += val[syb.index(teste)]
            elif (numbers[i] in syb):
                print("number:  " + numbers[i])
                num = num.replace(numbers[i], '')
                print(val[syb.index(numbers[i])])
                indo_num += val[syb.index(numbers[i])]

        return indo_num
