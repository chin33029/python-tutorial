import module_one
import module_two

if __name__ == "__main__":

    customers = ['Dean', 'Ricky', 'Samuel', 'Rahul']
    for customer in customers:
        module_one.check_balance(customer)
    # module_one.function_one()
    # module_two.function_one()

    # for i in range(5):
    #     module_two.function_two()