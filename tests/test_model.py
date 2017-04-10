from context import models

from models import model


import unittest

class test_Rooms(unittest.TestCase):
    def setUp(self):
        self.room = model.Room(20, 'new_room')
        self.room1 = model.Room(6, 'new_room1')
        self.livingspace = model.LivingSpace('orange')
        self.office = model.Office('manjaro')

    def test_Room_instance(self):
        self.assertIsInstance(self.room, model.Room)
        self.assertIsInstance(self.room1, model.Room)

    def test_Room_max_occupation(self):
        self.assertEqual(20, self.room.max_occupants)

    def test_Room_name(self):
        self.assertEqual('new_room1', self.room1.name)
        self.room1.name = "changedname"
        self.assertEqual('changedname', self.room1.name)

    def test_office_ocupants(self):
        self.assertEqual(6, self.office.max_occupants)

    def test_livingspace_ocupants(self):
        self.assertEqual(4, self.livingspace.max_occupants)

    def test_sublclass_Room(self):
        self.assertTrue(issubclass(model.Office, model.Room))
        self.assertTrue(issubclass(model.LivingSpace, model.Room))

    def test_room_current_population(self):
        self.assertEqual(self.room.current_population, 0)


class test_person(unittest.TestCase):
    def setUp(self):
        self.person1 = model.Person("person1")
        self.person2 = model.Person("person2")

        self.fellow1 = model.Fellow("fellow1")
        self.fellow2 = model.Fellow("fellow2", True)

        self.staff1 = model.Staff("staff1")
        self.staff2 = model.Staff("staff2")

        self.office = model.Office("testme")
        self.office1 = model.Office("HR")

        self.livingspace = model.Office('Orange')
        self.livingspace1 = model.Office('manjaro')

        self.fellow2.office = self.office1
        self.fellow2.livingspace = self.livingspace


    def test_person_instance(self):
        new_person = model.Person("new_person")
        self.assertIsInstance(new_person, model.Person)

    def test_add_office(self):
        self.person1.office = self.office
        self.staff2.office = self.office1
        self.fellow1.office = self.office

        self.assertEqual([self.person1.office, self.fellow1.office], [self.office, self.office])
        self.assertEqual(self.staff2.office, self.office1)

    def test_remove_office(self):
        self.person1.remove_office()
        self.assertEqual(self.person1.office, None)

    def test_is_allocated_office(self):
        self.assertEqual(self.person1.is_allocated_office(), False)

    def test_number_of_person(self):
        self.assertEqual(model.Person.number_of_person, 11)

    def test_number_of_staff(self):
        self.assertEqual(model.Staff.number_of_staff, 2)

    def test_fellow_add_living(self):
        self.assertEqual(self.fellow2.livingspace, self.livingspace)

    def test_fellow_is_allocated_living(self):
        self.assertEqual(self.fellow2.is_allocated_living(), True)
        self.assertNotEqual(self.fellow1.is_allocated_living(), True)

    def test_number_of_fellow(self):
        self.assertEqual(model.Fellow.number_of_fellows, 2)

    def test_fellow_wants_living(self):
        self.assertEqual(self.fellow2.wants_living, True)
