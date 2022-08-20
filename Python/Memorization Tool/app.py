from db_module import Flashcard, session
import sys


class App:

    def main_menu(self):
        print('1. Add flashcards\n2. Practice flashcards\n3. Exit')
        option = self.test_user_input(3)
        print()
        if option == 1:
            self.add_card_menu()
        elif option == 2:
            self.practice_cards()
        elif option == 3:
            self.bye()

    def add_card_menu(self):
        while True:
            print('1. Add a new flashcard\n2. Exit')
            option = self.test_user_input(2)
            print()
            if option == 1:
                self.create_new_card()
                print()
            elif option == 2:
                break

    def read_card_data_from_user(self, what_to_ask):
        while True:
            print(what_to_ask)
            data = input()
            if data.strip() != '':
                return data

    def create_new_card(self):
        question = self.read_card_data_from_user('Question:')
        answer = self.read_card_data_from_user('Answer:')
        self.add_card_to_db(question, answer)

    def add_card_to_db(self, question, answer):
        card = Flashcard(question=question, answer=answer)
        session.add(card)
        session.commit()

    def update_card_menu(self, question, answer):
        card = session.query(Flashcard).\
            filter(Flashcard.question == question).first()
        print('press "d" to delete the flashcard:\n'
              'press "e" to edit the flashcard:')
        action = self.test_user_input_words('d', 'e')

        if action == 'd':
            self.delete_card(card)
            print()
        elif action == 'e':
            self.edit_card(card, question, answer)
            print()

    def delete_card(self, card):
        session.delete(card)
        session.commit()

    def take_user_new_data(self, *args):
        print(f'\ncurrent {args[0]}: {args[1]}\n'
              f'please write a new {args[0]}:')
        data = input()
        if data == '':
            return args[1]
        return data

    def edit_card(self, card, question, answer):
        new_question = self.take_user_new_data('question', question)
        new_answer = self.take_user_new_data('answer', answer)
        card.question = new_question
        card.answer = new_answer
        session.commit()

    def practice_cards(self):
        cards = session.query(Flashcard).all()

        if len(cards) == 0:
            print('There is no flashcard to practice!\n')
        else:
            for card in cards:
                print(f'Question: {card.question}\n'
                      f'press "y" to see the answer:\n'
                      f'press "n" to skip:\n'
                      f'press "u" to update:')
                action = self.test_user_input_words('y', 'n', 'u')
                print()
                if action == 'y':
                    print(f'Answer: {card.answer}')
                    self.compare_answers(card)
                elif action == 'u':
                    self.update_card_menu(question=card.question,
                                          answer=card.answer)

    def compare_answers(self, card):
        print('press "y" if your answer is correct:\n'
              'press "n" if your answer is wrong:')
        option = self.test_user_input_words('y', 'n')
        if option == 'y':
            if card.box + 1 == 4:
                session.delete(card)
            else:
                card.box += 1
        else:
            card.box = 1
        session.commit()

    def test_user_input(self, end):
        try:
            option = input()
            option = int(option)
            assert 0 < option < end + 1
        except (ValueError, AssertionError):
            print(f'\n{option} is not an option')
        else:
            return option

    def test_user_input_words(self, *options):
        while True:
            option = input()
            if option not in options:
                print(f'\n{option} is not an option')
            else:
                return option

    def bye(self):
        print('Bye!')
        sys.exit()

    def run(self):
        while True:
            self.main_menu()
