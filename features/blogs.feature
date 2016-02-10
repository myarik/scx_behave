Feature: Blog parsing

  Scenario: jessiibrownie
    When I visit url https://jessiibrownie.wordpress.com/2016/01/29/a-day-in-agua-blanca/ in file 1.html
    Then I should see Last weekend I spent the Sunday out with the family
    Then I should see I know is a little different to what I usually post but
    And I should not see November 2013
    And I should not see ABOUT ME
    And I should not see Looks like a cool place

  Scenario: bellamorous
    When I visit url http://bellamorous.blogspot.com/2016/02/life-college.html in file 2.html
    Then I should see Due to that I show you this total
    And I should see I decided to buy this pant skirt or culotte because
    And I should see SEE YOU SOON
    And I should not see Besos... Carli
    And I should not see ABOUT ME
    And I should not see BLOG ARCHIVES