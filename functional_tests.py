from selenium import webdriver
import unittest

# nel file dei test funzionali bisogna aggiungere la descrizione del testcase
# ovvero della story che vogliamo testare

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicity_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # test homepage
        self.browser.get('http://localhost:8000')

        # test il title della pagina
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish test!')

        # descriviamo nei commenti i test che dobbiamo ancora implementare
        # che rappresentano la nostra story

        # invitiamo ad inserire un item To-Do

        # digita "scrivo qualcosa" in una text box

        # una volta premuto enter la pagina si aggiorna ed ora la page list
        # diventa: "1: scrivo qualcosa" è un item della To-Do list

        # la textbox è ancora presente per inserire alri item
        # scriviamo nella text box "un altro item"

        # la pagina di aggiorna di nuovo ed ora sono presenti 2 item nella lista

        # la lista dovrebbe restare li anche per una successiva consultazione
        # il sito dovrebbe generare una url unica dove trovare la propria lista

if __name__ == '__main__':
    unittest.main(warnings='ignore')
