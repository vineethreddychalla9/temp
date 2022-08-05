def bayes_theorem(p_f,p_f_and_a):
    p_a_given_f = (p_f_and_a / p_f)
    return p_a_given_f
p_f = float(input('Enter value of P(F): '))
p_f_and_a = float(input('Enter value of P(F^A): '))
result = bayes_theorem(p_f,p_f_and_a)
print('Result P(A|F) = %.2f%%' % (result*100))

'''
Output:
Enter value of P(F): 20
Enter value of P(F^A): 3
Result P(A|F) = 15.00%
'''