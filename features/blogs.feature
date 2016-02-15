Feature: Style coalition

  Scenario: reset page
    When I visit url https://test.stylecoalition.com/reset
    Then I should see Forgot your password?
    And I should see Enter your email address below and we’ll send you a link to reset your password.

    When I send reset form
    Then I should see This field is required.

    When I fill email by qwerty
    And I send reset form
    Then I should see Enter a valid email address.

    When I fill email by qwerty@qwerty.com
    And I send reset form
    Then I should see The e-mail address is not assigned to any user account

    When I fill email by a.homenko@synergetica.net
    And I send reset form
    Then I should see We've sent you an email with instructions on how to reset your password.