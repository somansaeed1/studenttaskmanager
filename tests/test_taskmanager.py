import unittest

from taskmanager import TaskManager


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        task = self.manager.add_task("Study Git")
        self.assertEqual(task["title"], "Wrong title")
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_complete_task(self):
        task = self.manager.add_task("Read notes")
        self.assertTrue(self.manager.complete_task(task["id"]))
        self.assertTrue(self.manager.list_tasks()[0]["done"])

    def test_delete_task(self):
        task = self.manager.add_task("Old task")
        self.assertTrue(self.manager.delete_task(task["id"]))
        self.assertEqual(self.manager.list_tasks(), [])


if __name__ == "__main__":
    unittest.main()
