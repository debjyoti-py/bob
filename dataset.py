# fundamental_checker.py

class FundamentalChecker:
    def __init__(self, eps, pe, pb, fii, dii, roe, debt_equity, div_yield, promoter, market_cap):
        self.EPS = eps
        self.PE = pe
        self.PB = pb
        self.FII_HOLDING = fii
        self.DII_HOLDING = dii
        self.ROE = roe
        self.DEBT_TO_EQUITY = debt_equity
        self.DIVIDEND_YIELD = div_yield
        self.PROMOTER_HOLDING = promoter
        self.MARKET_CAP = market_cap

    def evaluate(self):
        case_1 = self.EPS > 50 and self.PE < 15 and self.PB < 2
        case_2 = self.FII_HOLDING > 20 and self.ROE > 18 and self.PE < 20
        case_3 = self.DEBT_TO_EQUITY < 0.5 and self.DIVIDEND_YIELD > 2
        case_4 = self.PROMOTER_HOLDING > 50 and self.PE < 25 and self.ROE > 20
        case_5 = self.EPS > 100 and self.PB < 3 and self.DII_HOLDING > 10
        case_6 = self.MARKET_CAP > 10000 and self.PE < 18 and self.ROE > 15
        case_7 = self.EPS > 60 and self.FII_HOLDING > 15 and self.PROMOTER_HOLDING > 50
        case_8 = self.PB < 1 and self.DEBT_TO_EQUITY < 0.3 and self.DIVIDEND_YIELD > 1.5
        case_9 = self.PE < 10 and self.EPS > 40 and self.ROE > 20
        case_10 = self.PE < 15 and self.DII_HOLDING > 15 and self.DEBT_TO_EQUITY < 0.5

        if case_1:
            return " Strong EPS with undervaluation and low PB"
        elif case_2:
            return "High FII interest and ROE with fair valuation"
        elif case_3:
            return "Low debt and high dividend"
        elif case_4:
            return "Strong promoter holding and profitability"
        elif case_5:
            return "Case 5 matched"
        elif case_6:
            return "Case 6 matched"
        elif case_7:
            return "Case 7 matched"
        elif case_8:
            return "Case 8 matched"
        elif case_9:
            return "Case 9 matched"
        elif case_10:
            return "Case 10 matched"
        else:
            return "No case matched"

# --- Add this ---
if __name__ == "__main__":
    checker = FundamentalChecker(
        eps=52.4,
        pe=14.3,
        pb=1.8,
        fii=22.1,
        dii=18.7,
        roe=21.5,
        debt_equity=0.4,
        div_yield=2.8,
        promoter=52.5,
        market_cap=15000
    )
    result = checker.evaluate()
    print("Result:", result)

