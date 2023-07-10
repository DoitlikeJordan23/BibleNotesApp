import unittest
from io import StringIO
from Bible_notes.py import add_verse, search_verses

class BibleNotesAppTestCase(unittest.TestCase):
    def setUp(self):
        self.saved_stdout = sys.stdout
        self.out = StringIO()
        sys.stdout = self.out

    def tearDown(self):
        sys.stdout = self.saved_stdout

    def test_add_verse(self):
        # Simulate user input for testing
        input_values = ['John', '3', '16', 'God is love', 'Man is sinful', 'God loves mankind']
        expected_output = "Verse added successfully!\n"

        # Patch the input() function to return predefined input values
        with patch('builtins.input', side_effect=input_values):
            add_verse()

        # Get the printed output
        actual_output = self.out.getvalue()

        # Assert that the output matches the expected output
        self.assertEqual(actual_output, expected_output)

        # TODO: Add further assertions if needed, such as checking if the verse is written to the CSV file correctly

    def test_search_verses(self):
        # Simulate user input for testing
        input_values = ['God']
        expected_output = (
            "\nBook: John\n"
            "Chapter: 3\n"
            "Verse: 16\n"
            "God: God is love\n"
            "Man: Man is sinful\n"
            "Relationship: God loves mankind\n\n"
        )

        # Patch the input() function to return predefined input values
        with patch('builtins.input', side_effect=input_values):
            # Create a temporary CSV file with test data
            with open("Bible_notes.csv", "w") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['John', '3', '16', 'God is love', 'Man is sinful', 'God loves mankind'])

            search_verses()

        # Get the printed output
        actual_output = self.out.getvalue()

        # Assert that the output matches the expected output
        self.assertEqual(actual_output, expected_output)

    # TODO: Add more test cases for different scenarios and functionalities

if __name__ == '__main__':
    unittest.main()
