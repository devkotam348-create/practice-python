###define a class result to hold result data for a test (attempt, right ,wrong). overload + operator to combine result of two tests

class Result:
    def __init__(self, attempt, right,wrong):
        self.attempt = attempt
        self.right = right
        self.wrong = wrong

    def __add__(self, others):
        return Result(self.attempt + others.attempt,
                self.right + others.right,
                self.wrong + others.wrong)
    def __str__(self):
        return f"Total attempts::{self.attempt}, Total right ::{self.right} and Total wrong ::{self.wrong}"
    
    
r = Result(4,3,1)
r1 = Result(6,4,2)

r2 = r + r1
print(r2)
