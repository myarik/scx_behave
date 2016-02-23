Feature: Blog parsing

  Scenario: jessiibrownie
    When I visit url https://jessiibrownie.wordpress.com/2016/01/29/a-day-in-agua-blanca/ in file jessiibrownie.html
    Then I should see Last weekend I spent the Sunday out with the family
    Then I should see I know is a little different to what I usually post but
    And I should not see November 2013
    And I should not see ABOUT ME
    And I should not see Looks like a cool place

  Scenario: bellamorous
    When I visit url http://bellamorous.blogspot.com/2016/02/life-college.html in file bellamorous.html
    Then I should see Due to that I show you this total
    And I should see I decided to buy this pant skirt or culotte because
    And I should see SEE YOU SOON
    And I should not see Besos... Carli
    And I should not see ABOUT ME
    And I should not see BLOG ARCHIVES

  Scenario: shefinds
    When I visit url http://www.shefinds.com/2016/5-ways-to-make-the-most-of-the-money-talk-adultlife/ in file shefinds.html
    Then I should see Now before you book a boardroom
    And I should see clear financial roles and expectations
    And I should see he mistaken double charge at the grocery store
    And I should not see subscribe
    And I should not see kids
    And I should not see comments

  Scenario: thesmallthingsblog
    When I visit url http://www.thesmallthingsblog.com/2016/02/1-braid-2-ways-to-finish-the-style/ in file thesmallthingsblog.html
    Then I should see hair grow 10 inches
    And I should see messy bun on the opposite side
    And I should see if you post a pic
    And I should not see email address
    And I should not see baby
    And I should not see FAQ










