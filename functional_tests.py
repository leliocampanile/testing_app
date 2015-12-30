from selenium import webdriver
import unittest

# nel file dei test funzionali bisogna aggiungere la descrizione del testcase
# ovvero della story che vogliamo testare

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # test homepage
        self.browser.get('http://localhost:8000')

        # test il title della pagina
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        self.fail('Finish test!')

        # descriviamo nei commenti i test che dobbiamo ancora implementare
        # che rappresentano la nostra story

        # invitiamo ad inserire un item To-Do
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # digita "scrivo qualcosa" in una text box
        inputbox.send_keys('scrivo qualcosa')

        # una volta premuto enter la pagina si aggiorna ed ora la page list
        # diventa: "1: scrivo qualcosa" è un item della To-Do list
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: scrivo qualcosa' for row in rows))
        # la textbox è ancora presente per inserire alri item
        # scriviamo nella text box "un altro item"

        # la pagina di aggiorna di nuovo ed ora sono presenti 2 item nella lista

        # la lista dovrebbe restare li anche per una successiva consultazione
        # il sito dovrebbe generare una url unica dove trovare la propria lista

if __name__ == '__main__':
    unittest.main(warnings='ignore')
