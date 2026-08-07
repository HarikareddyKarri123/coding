class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        # Step 1: Extract prime factors of t (only 2, 3, 5, 7 are valid for single digits)
        factors = {2: 0, 3: 0, 5: 0, 7: 0}
        temp_t = t
        for p in [2, 3, 5, 7]:
            while temp_t % p == 0:
                factors[p] += 1
                temp_t //= p
        
        # If t has prime factors other than 2, 3, 5, 7, it's impossible
        if temp_t > 1:
            return "-1"
            
        n = len(num)
        
        # Maps each digit from 1-9 to its prime factors
        digit_factors = {
            1: {2: 0, 3: 0, 5: 0, 7: 0},
            2: {2: 1, 3: 0, 5: 0, 7: 0},
            3: {2: 0, 3: 1, 5: 0, 7: 0},
            4: {2: 2, 3: 0, 5: 0, 7: 0},
            5: {2: 0, 3: 0, 5: 1, 7: 0},
            6: {2: 1, 3: 1, 5: 0, 7: 0},
            7: {2: 0, 3: 0, 5: 0, 7: 1},
            8: {2: 3, 3: 0, 5: 0, 7: 0},
            9: {2: 0, 3: 2, 5: 0, 7: 0}
        }
        
        # Robust helper to find minimal suffix string satisfying remaining factors
        def get_min_suffix(rem_2, rem_3, rem_5, rem_7):
            rem_2 = max(0, rem_2)
            rem_3 = max(0, rem_3)
            rem_5 = max(0, rem_5)
            rem_7 = max(0, rem_7)
            
            sevens = ['7'] * rem_7
            fives = ['5'] * rem_5
            
            best_len = float('inf')
            best_str = ""
            
            # Bound search range to the immediate mathematical division limit
            for n8 in range(rem_2 // 3 + 2):
                for n9 in range(rem_3 // 2 + 2):
                    # Check combinations of remainder components (r2 up to 2, r3 up to 1)
                    for r2 in range(3):
                        for r3 in range(2):
                            if 3 * n8 + r2 >= rem_2 and 2 * n9 + r3 >= rem_3:
                                leftovers = []
                                if r2 == 0 and r3 == 1: leftovers = ['3']
                                elif r2 == 1 and r3 == 0: leftovers = ['2']
                                elif r2 == 1 and r3 == 1: leftovers = ['6']
                                elif r2 == 2 and r3 == 0: leftovers = ['4']
                                elif r2 == 2 and r3 == 1: leftovers = ['2', '6']
                                
                                cand = ['8'] * n8 + ['9'] * n9 + leftovers
                                cand.sort()
                                cand_str = "".join(cand)
                                
                                # Minimize by length first, then lexicographically
                                if len(cand_str) < best_len:
                                    best_len = len(cand_str)
                                    best_str = cand_str
                                elif len(cand_str) == best_len:
                                    if cand_str < best_str or best_str == "":
                                        best_str = cand_str
                                        
            res = fives + sevens + list(best_str)
            res.sort()
            return "".join(res)

        # Step 2: Compute prefix factor accumulations
        prefix_cnt = [None] * (n + 1)
        prefix_cnt[0] = (factors[2], factors[3], factors[5], factors[7])
        
        first_zero = num.find('0')
        limit = first_zero if first_zero != -1 else n
        
        for i in range(limit):
            d = int(num[i])
            r2, r3, r5, r7 = prefix_cnt[i]
            df = digit_factors[d]
            prefix_cnt[i+1] = (r2 - df[2], r3 - df[3], r5 - df[5], r7 - df[7])
            
        # Check if the exact original number matches all divisibility rules
        if first_zero == -1:
            r2, r3, r5, r7 = prefix_cnt[n]
            if r2 <= 0 and r3 <= 0 and r5 <= 0 and r7 <= 0:
                return num
                
        # Step 3: Backtrack from right to left to find the first place to increase a digit
        for i in range(n - 1, -1, -1):
            if i > limit:
                continue
            
            curr_digit = int(num[i])
            for next_digit in range(curr_digit + 1, 10):
                r2, r3, r5, r7 = prefix_cnt[i]
                df = digit_factors[next_digit]
                
                rem_2, rem_3, rem_5, rem_7 = r2 - df[2], r3 - df[3], r5 - df[5], r7 - df[7]
                suffix = get_min_suffix(rem_2, rem_3, rem_5, rem_7)
                available_space = n - 1 - i
                
                if len(suffix) <= available_space:
                    ones_needed = available_space - len(suffix)
                    return num[:i] + str(next_digit) + ('1' * ones_needed) + suffix
                    
        # Step 4: If no same-length configuration matches, safely scale to length n + 1
        total_len = n + 1
        while True:
            suffix = get_min_suffix(factors[2], factors[3], factors[5], factors[7])
            if len(suffix) <= total_len:
                ones_needed = total_len - len(suffix)
                return ('1' * ones_needed) + suffix
            total_len += 1
