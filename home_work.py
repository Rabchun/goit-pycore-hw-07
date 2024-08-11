import datetime

class Birthday:
    def __init__(self, value):
        try:
            self.value = datetime.datetime.strptime(value, "%d.%m.%Y").date()
        except ValueError:
            raise ValueError("Невірний формат дати. Використовуйте DD.MM.YYYY")

class Record:
 

    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)

    def get_birthday(self):
        return self.birthday.value.strftime("%d.%m.%Y") if self.birthday else None
    
class AddressBook:


    def get_upcoming_birthdays(self):
        today = datetime.date.today()
        next_week = today + datetime.timedelta(days=7)
        upcoming_birthdays = []
        for record in self.data:
            if record.birthday:
                birthday_this_year = datetime.date(today.year, record.birthday.value.month, record.birthday.value.day)
                if today <= birthday_this_year <= next_week:

                    weekday = birthday_this_year.weekday()
                    if weekday >= 5:  # Вихідні
                        birthday_this_year += datetime.timedelta(days=7 - weekday)
                    upcoming_birthdays.append({"name": record.name, "birthday": birthday_this_year.strftime("%d.%m.%Y")})
        return upcoming_birthdays
    
@input_error
def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)
    if record:
        try:
            record.add_birthday(birthday)
            return f"День народження для {name} додано: {birthday}"
        except ValueError as e:
            return str(e)
    else:
        return f"Контакт {name} не знайдено"

@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if record and record.birthday:
        return f"День народження {name}: {record.get_birthday()}"
    else:
        return f"Контакт {name} не знайдено або у нього немає дати народження"


@input_error
def birthdays(args, book):
    upcoming_birthdays = book.get_upcoming_birthdays()
    if upcoming_birthdays:
        for birthday in upcoming_birthdays:
            print(f"День народження у {birthday['name']}: {birthday['birthday']}")
    else:
        print("Немає днів народжень на наступному тижні")
