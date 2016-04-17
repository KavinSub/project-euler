digits = set("123456789")
def all_digits(a, b, p):
    s_a = str(a)
    s_b = str(b)
    s_p = str(p)
    return (set(s_a) | set(s_b) | set(s_p)) == digits and (len(s_a) + len(s_b) + len(s_p)) == 9

if __name__ == '__main__':
    product = 0
    product_set = set()
    for a in range(1, 10000):
        for b in range(1, 10000):
            p = a * b
            if p < 98765:        
                if all_digits(a, b, p):
                    product_set.add(p)
        if a % 100 == 0:
            print(a)
    print(sum(product_set))    