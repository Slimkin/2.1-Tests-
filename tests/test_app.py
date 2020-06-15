import unittest
from unittest.mock import patch
import json
from os import path
import app

documents = []
directories = {}


@patch('app.documents', documents, create=True)
@patch('app.directories', directories, create=True)
class SecretaryAppTestCase(unittest.TestCase):
    def setUp(self):
        current_path = path.abspath('.')
        p_dirs = path.join(current_path, 'fixtures', 'directories.json')
        p_docs = path.join(current_path, 'fixtures', 'documents.json')

        with open(p_dirs, 'r', encoding='utf8') as dirs:
            directories.update(json.load(dirs))
        with open(p_docs, 'r', encoding='utf8') as docs:
            documents.extend(json.load(docs))


    def test_update_data(self):
        app.update_date()
        self.assertGreater(len(documents), 0)
        self.assertGreater(len(directories), 0)


    def test_add_new_shelf(self):
        start_len = (len(directories))
        test_value = '12'
        self.assertNotIn(test_value, directories.keys())
        app.add_new_shelf(test_value)
        self.assertNotEqual(start_len, len(directories))


    def test_move_doc_to_shelf(self):
        doc = '2207 876234'
        test_shelf = '3'
        self.assertIn(doc, [document['number'] for document in documents])
        with patch('app.input', side_effect=[doc, test_shelf]):
            app.move_doc_to_shelf()
        self.assertIn(doc, directories[test_shelf])


    def test_add_new_doc(self):
        with patch('app.input',
                   side_effect=['4705 118098', 'passport', 'Ivanov Ivan', '1']):
            result = app.add_new_doc()
        self.assertIn('4705 118098', directories['1'])
        self.assertEqual(result, '1')

if __name__ == '__main__':
    unittest.main()