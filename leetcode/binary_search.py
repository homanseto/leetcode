

def first_true(pred, n):
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if pred(mid):
            right = mid
        else:
            left = mid + 1
    return left  # first index where pred is True

arr = [0,1,2,3,4,5,6,7,8]
pred = lambda i: arr[i] > 5
print(first_true(pred, len(arr)))  # Output: 6 (arr[6]=6)


def first_true_inclusive_2(pred, n):
    left, right = 0, n-1
    ans = n  # default if none true
    while left <= right:
        mid = (left + right) // 2
        if pred(mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans

arr = [1,3,5,7,9]
pred = lambda i: arr[i] >= 5
print(first_true_inclusive_2(pred, len(arr)))  # 2

def last_false_3(pred, n):
    left, right = -1, n
    while right - left > 1:
        mid = (left + right) // 2
        if pred(mid):
            right = mid
        else:
            left = mid
    return left  # last false index

arr = [1,3,5,7,9]
pred = lambda i: arr[i] >= 5
print(last_false_3(pred, len(arr)))  # 1 (arr[1]=3, last false)


def binary_search_boundary(arr, target):
    """Return first index i such that arr[i] >= target (lower bound)."""
    n = len(arr)
    left, right = 0, n
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left  # insertion point

# Test
arr = [2, 4, 6, 8, 10]
print(binary_search_boundary(arr, 5))  # 2 (arr[2]=6)
print(binary_search_boundary(arr, 10)) # 4
print(binary_search_boundary(arr, 1))  # 0
print(binary_search_boundary(arr, 12)) # 5 (past end)

def monthly_interest_min_repayment_in_range_of_years(load_amount, monthly_interest_rate, years):
    """Calculate minimum months to repay a loan."""
    total_months = years * 12
    left, right = 0, load_amount  
    while left < right:
        mid = (left + right)// 2
        remaining = load_amount 
        for _ in range(total_months):
            remaining = remaining * monthly_interest_rate 
            remaining -= mid
            if remaining <= 0:
                break
        if remaining <= 0:
            right = mid 
        else:
            left = mid +1
    return right

print(monthly_interest_min_repayment_in_range_of_years(20000000, 1.0015, 30))  

def min_monthly_payment(loan_amount, monthly_interest_rate, years):
    """Return the minimum constant monthly payment to repay the loan within given years."""
    total_months = years * 12
    # Upper bound: paying the full loan in the first month (ignoring interest) is enough.
    # A safer upper bound: loan_amount * (1+rate)^total_months, but loan_amount works because
    # paying it all in month 1 always pays off the loan regardless of interest.
    low, high = 0, loan_amount
    best = high  # fallback if something goes wrong

    while low < high:
        mid = (low + high) // 2
        remaining = loan_amount
        # Simulate months
        for _ in range(total_months):
            remaining = remaining * (1 + monthly_interest_rate) - mid
            if remaining <= 0:
                break
        if remaining <= 0:
            # Payment is enough, try smaller
            best = mid
            high = mid
        else:
            low = mid + 1
    return best

# Example:
# loan = 20,000,000, monthly interest = 0.15% -> multiplier 1.0015, years = 30
print(min_monthly_payment(20000000, 0.0015, 30))   # Note: 0.0015, not 1.0015


def min_monthly_payment_formula(loan_amount, monthly_multiplier, years):
    r = monthly_multiplier - 1.0          # convert to decimal (e.g., 1.0015 → 0.0015)
    n = years * 12
    if r == 0:
        return (loan_amount + n - 1) // n   # no interest, simple division ceiling
    # Compute (1+r)^n using fast exponentiation (or math.pow)
    factor = (1 + r) ** n                  # or pow(1+r, n)
    payment = loan_amount * (r * factor) / (factor - 1)
    # Return ceiling as integer (since you must pay at least that much)
    return int(payment) + (1 if payment % 1 > 1e-9 else 0)

# Example usage
print(min_monthly_payment_formula(20000000, 1.0015, 30))  # Output: about 69400


# 
