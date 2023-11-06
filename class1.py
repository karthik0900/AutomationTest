class Reversing_values:
    def __init__(self, input_name, input_number, ):
        self.input_number = input_number
        self.input_name = input_name

    def r_name(self):
        rev_name = self.input_name[::-1]
        print(rev_name)

    def r_number(self):
        num = int(self.input_number)
        reversed_num = 0

        while num > 0:
            last_digit = num % 10

            reversed_num = reversed_num * 10 + last_digit

            num = num // 10

        print(reversed_num)


s1 = Reversing_values("python automation", 345)

s1.r_number()
s1.r_name()
