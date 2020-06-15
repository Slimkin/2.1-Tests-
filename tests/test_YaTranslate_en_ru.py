import unittest
from YaTranslate_en_ru import translate_en_ru


class YaTranslateEnRuTestCase(unittest.TestCase):
    def test_translation_request(self):
        source_text = 'corn'
        result = translate_en_ru(source_text)
        self.assertEqual(result['text'][0], 'кукуруза')

    def test_request_problems(self):
        source_text = 'mouse'
        result = translate_en_ru(source_text)
        self.assertEqual(result['code'], 200)

    @unittest.expectedFailure
    def test_target_language_is_not_ru(self):
        source_text = 'maulwurf'
        result = translate_en_ru(source_text)
        self.assertEqual(result['text'][0], 'крот')



if __name__ == '__main__':
    unittest.main()