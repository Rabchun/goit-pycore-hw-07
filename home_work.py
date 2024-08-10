class Record:


    def add_birthday(self, birthday):
        if self.birthday:
            raise ValueError("Birthday already exists")
        self.birthday = Birthday(birthday)


def get_upcoming_birthdays(book):
    today = datetime.date.today()
    next_week = today + datetime.timedelta(days=7)
    birthdays = []
    for record in book.data.values():
        if record.birthday and today <= record.birthday.value < next_week:
            birthdays.append((record.name.value, record.birthday.value))
    return birthdays

@input_error
def add_birthday(args, book):
    name, birthday, *_ = args
    record = book.find(name)
    if record is None:
        print(f"Contact {name} not found.")
        return
    record.add_birthday(birthday)
    print(f"Birthday added for {name}: {birthday}")

@input_error
def show_birthday(args, book):
    name, *_ = args
    record = book.find(name)
    if record is None:
        print(f"Contact {name} not found.")
        return
    print(f"Birthday for {name}: {record.birthday.value}")

@input_error
def birthdays(args, book):
    birthdays = get_upcoming_birthdays(book)
    if birthdays:
        print("Upcoming birthdays:")
        for name, birthday in birthdays:
            print(f"{name}: {birthday}")
    else:
        print("No upcoming birthdays.")


if __name__ == "__main__":

    elif command == "add-birthday":
        add_birthday(args, book)

    elif command == "show-birthday":
        show_birthday(args, book)

    elif command == "birthdays":
        birthdays(args, book)