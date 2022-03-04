Feature: Veriff Me Flow

        Steps in this flow:

        1. Select configuration and settings
        2. Start process by clicking VERIFF ME
        3. Veriff is launched

        Questions & Considerations:

        * UI Automation may be overkill here. Instead, API and Component testing is preferred for these simpler checks
        * Lower level testing is better with config and setting matrices and flows since there are so many combinations
        * Full Name is an input field (infinite possibilities). What are the constraints and/or requirements for a valid Full Name?
        * How do we handle invalid inputs and settings?
        * Given our scope, I would also consider Accessibility Testing, especially after seeing the Language Dropdown is a button with a list in the wrong place...
        * Web Performance testing is out of the scope, but Pylenium would make it easy to include if we wanted as well.
        * We can use the API to create test data and setup the app state to drive the UI and test areas more easily.


    Scenario Outline: Enter valid Full Name
        Given the Full Name field is an input with no "visible" constraints
        When I enter a valid {full_name}
        Then the Veriff Me flow should start successfully

        Examples:
            | full_name     | NOTE                   |
            | Carlos Kidman | An "english" full name |
            | 张 Zhāng      | Unicode characters     |
            | Li            | 2 or fewer characters  |
            | ...           | What else?             |



    Scenario: Enter invalid Full Name
        Given the Full Name field is an input with no "visible" constraints
        When I enter an invalid {full_name}
        Then the Veriff Me flow should raise a user-friendly error

        Examples:
            | full_name                                    | NOTE                         |
            |                                              | Empty string                 |
            | " "                                          | Whitespace (ie spaces, tabs) |
            | 123                                          | Numbers (incorrect type)     |
            | UNION SELECT username, password from users-- | SQL Injection (security)     |
            | ...                                          | What else?                   |


    Scenario: Check supported languages
        Given our list of supported langauges
        Then each language should be included in the Session Language section

        Questions:
        * Where does the list of support languages come from?
        * How can I get the text for our UI for each language?


    Scenario: Check supported countries
        Given our list of supported countries
        Then each country should be included in the Document Country section (in alphabetical order)

        Questions:
        * Where does the list of support languages come from?
        * Are there differences in our flow given the country?


    Scenario: Filter countries
        Given the Document country field
        When I start typing characters
        Then the list of countries is filtered to match my input


    Scenario: Check supported document types
        Given our list of supported document types
        Then each document type should be included in the Document Type section

        Questions:
        * Where does the list of supported document types come from?


    Scenario: Launch Veriff via InContext
        Given InContext is selected
        When I start the Veriff process
        Then Veriff is launched in a popup on the current web page


    Scenario: Launch Veriff via Redirect
        Given Redirect is selected
        When I start the Veriff process
        Then Veriff is launched by redirecting the user to a new web page


    Scenario: Launch Veriff with valid configuration
        Given each setting has a non-empty, valid value
        When I start the Veriff process
        Then Veriff is launched successfully with the correct locale and country


    Scenario: Launch Veriff with invalid configuration
        Given one or more settings are empty or invalid
        When I start the Veriff process
        Then Veriff raises a user-friendly error
