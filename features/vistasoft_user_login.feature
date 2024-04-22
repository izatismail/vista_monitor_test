@f_login
Feature: User login
  User story:
    As a user, I can login to VSM using my email and password. When I have
    logged in successfully, I should see the VSM homepage.

  Scenario: Navigate to login page via homepage
    Given I am on the VSM homepage
    When I click on the Login button
    Then I should be on the "Dürr Dental ID" login page


  @login_page
  Scenario: Successful login (positive testing)
    Given I am already on the "Dürr Dental ID" login page
    When I enter "VSM_EMAIL" as the email and "VSM_PWD" as the password
    And I submit the login form
    Then I should be redirected to the VSM dashboard