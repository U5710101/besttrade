from app.src.db.investordao import get_all_investors, get_investor_with_name
from app.src.domain.Investor import Investor

def main():
    investors = get_all_investors()
    for investor in investors:
        print(investor)



if __name__ == '__main__':
    main()