# global variable
multiplier_amount = 1000000

def calculate_gains(amount_inv=0.0, total_gains=0.0, total_amount=0.0):
    # Calculating the return gains of an investment.
    

    # base amount gain margin
    gain_margin = 0.001
    total_gains = 0
    total_amount = 0

    if amount_inv > 1000:

        # check whether the invested amount is greater than the multiplier amount
        if amount_inv >= multiplier_amount:
            # gather the value of the division
            multiplier = (amount_inv//multiplier_amount)/100
            #print(multiplier)

            # update the `gain_margin` by the multiplier mod
            gain_margin += multiplier
            #print(gain_margin)

        # calculate the total amount of gains
        total_gains = amount_inv * gain_margin
        #print(total_gain)

        # calculate the total amount plus the gain margin
        total_amount = amount_inv + total_gains

    # return the gains, the full amount and the gain margin
    return total_gains, total_amount, gain_margin

calculate_gains(amount_inv=2000000)
