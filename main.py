class User:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} TL yatırıldı. Güncel bakiye: {self.balance} TL")
        else:
            print("Geçersiz miktar. Lütfen pozitif bir değer girin.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"{amount} TL çekildi. Güncel bakiye: {self.balance} TL")
        else:
            print("Yetersiz bakiye veya geçersiz miktar.")

    def check_balance(self):
        print(f"{self.name} adlı kullanıcının güncel bakiyesi: {self.balance} TL")


class Bank:
    def __init__(self):
        self.users = {}

    def create_account(self, name, account_number, initial_balance=0):
        if account_number in self.users:
            print("Bu hesap numarası zaten kullanımda. Lütfen başka bir hesap numarası girin.")
        else:
            new_user = User(name, account_number, initial_balance)
            self.users[account_number] = new_user
            print(f"{name} için hesap oluşturuldu. Hesap Numarası: {account_number}, Başlangıç Bakiyesi: {initial_balance} TL")

    def find_account(self, account_number):
        return self.users.get(account_number, None)


def main():
    bank = Bank()

    while True:
        print("\nBanka İşlemleri:")
        print("1. Hesap Aç")
        print("2. Para Yatır")
        print("3. Para Çek")
        print("4. Bakiye Kontrolü")
        print("5. Çıkış")

        choice = input("Seçiminiz: ")

        if choice == "1":
            name = input("İsim: ")
            account_number = input("Hesap Numarası: ")
            try:
                initial_balance = float(input("Başlangıç Bakiyesi: "))
                bank.create_account(name, account_number, initial_balance)
            except ValueError:
                print("Lütfen geçerli bir miktar girin.")
        elif choice == "2":
            account_number = input("Hesap Numarası: ")
            user = bank.find_account(account_number)
            if user:
                try:
                    amount = float(input("Yatırılacak Tutar: "))
                    user.deposit(amount)
                except ValueError:
                    print("Lütfen geçerli bir miktar girin.")
            else:
                print("Hesap Bulunamadı.")
        elif choice == "3":
            account_number = input("Hesap Numarası: ")
            user = bank.find_account(account_number)
            if user:
                try:
                    amount = float(input("Çekilecek Tutar: "))
                    user.withdraw(amount)
                except ValueError:
                    print("Lütfen geçerli bir miktar girin.")
            else:
                print("Hesap Bulunamadı.")
        elif choice == "4":
            account_number = input("Hesap Numarası: ")
            user = bank.find_account(account_number)
            if user:
                user.check_balance()
            else:
                print("Hesap Bulunamadı.")
        elif choice == "5":
            print("Banka sisteminden çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")


if __name__ == "__main__":
    main()
