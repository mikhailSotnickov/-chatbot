import pickle
import os


class User:  # класс пользователь
    def __init__(self):
        self.location = dict()
        self.is_have_location = False

        # self.places_is_first = {0: True, 1: True, 2: True, 3: True, 4: True, 5: True, 6: True}
        self.places_count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        self.saw_counter = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

        self.all_places = []
        self.food = []
        self.museums = []
        self.parks = []
        self.cinemas = []
        self.shops = []

    def new_arr(self):
        new_arr = []
        for d in self.food:
            dict_new = d['venue']
            dict_new['id_event'] = 'опрос_04'
            new_arr.append(dict_new)
        for d in self.museums:
            dict_new = d['venue']
            dict_new['id_event'] = 'опрос_01'
            new_arr.append(dict_new)
        for d in self.parks:
            dict_new = d['venue']
            dict_new['id_event'] = 'опрос_02'
            # dict_new['random'] = random.random()
            new_arr.append(dict_new)
        for d in self.cinemas:
            dict_new = d['venue']
            dict_new['id_event'] = 'опрос_03'
            # dict_new['random'] = random.random()
            new_arr.append(dict_new)
        for d in self.shops:
            dict_new = d['venue']
            dict_new['id_event'] = 'опрос_00'
            # dict_new['random'] = random.random()
            new_arr.append(dict_new)
        new_arr = sorted(new_arr, key=lambda new_arr: new_arr['distance'])
        print(new_arr)

    def add_setting(self, arr):
        self.opros = arr


users_list = dict()  # список всех пользователей


# ключ - id пользователя, значение - класс с информацией о пользователе


def get_users():  # получить пользователя по uid
    global users_list
    if os.path.getsize('users.dat') > 0:
        users_list = pickle.load(open('users.dat', 'rb'))
    else:
        users_list = {}
    return users_list


def get_user(uid):  # получить пользователя по uid
    global users_list
    users_list = get_users()
    return users_list[uid]


def save_users():
    global users_list
    pickle.dump(users_list, open('users.dat', 'wb'))


def add_user(uid):
    global users_list
    users_list = get_users()

    new_user = User()  # создаем нового пользователя
    users_list[uid] = new_user

    pickle.dump(users_list, open('users.dat', 'wb'))


def main():
    pass


if __name__ == '__main__':
    main()
