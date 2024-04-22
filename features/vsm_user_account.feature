@f_dashboard
Feature: My user account
  User story:
    As a user after login, I want to check my username and email by going to
    “My user account”. I should see “My user account” in the right panel and be
    able to verify my username and email.

  Scenario: Correct user account information
    Given I am on the VSM dashboard page
    When I click on the profile button
    And I click on the "My user account"
    Then I should see "My user account" page
    And I should see correct name and email address